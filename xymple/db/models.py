import re
import db
from sqlalchemy import Column, Integer, Text

class Pair(db.Base):
    __tablename__ = "xymples"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(Text, nullable=False)
    passcode = Column(Text, nullable=True)

    @property
    def uid(self):
        return self.id

    @staticmethod
    def fromuid(uid):
        return db.session.query(Pair).filter_by(id=int(uid, 16)).first()
    
    @staticmethod
    def fromurl(url, passcode=None):
        if not re.match("http://", url):
            if not re.match("https://", url):
                url = "http://" + url
        pair = db.session.query(Pair).filter_by(url=url, 
                                                    passcode=passcode).first()
        if pair:
            return pair
        pair = Pair(url=url, passcode=passcode)
        db.session.add(pair)
        db.session.commit()
        pair = db.session.query(Pair).filter_by(url=url,
                                                    passcode=passcode).first()
        return pair
