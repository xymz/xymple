try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import distutils.cmd
import os.path

def required_packages():
    with open("REQUIREMENTS") as file:
        for line in file:
            package = line.split()[:-1]
            if len(package) == 3:
                yield " ".join(package[:-1])
                continue
            try:
                __import__(package[-1])
            except ImportError:
                yield " ".join(package[:-1])


class initialize(distutils.cmd.Command):
    user_options = []

    def initialize_options(self):
        self.root = self.record = None

    def finalize_options(self):
        pass

    def run(self):
        easy_install = self.distribution.get_command_class("easy_install")
        cmd = easy_install(self.distribution, args="x", root=self.root,
                           record=self.record)
        cmd.ensure_finalized()
        cmd.always_copy_from = "."
        cmd.args = list(required_packages())
        cmd.run()
        print "creating database..."
        import xymple.db.db
        import xymple.db.models
        xymple.db.db.init_db()
        print "created"


setup(name="xymple",
      packages=["xymple"],
      package_dir={"xymple": "xymple"},
      cmdclass=dict(initialize=initialize))
