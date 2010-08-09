$(document).ready(function() {
  var private = $("input[name='private']");
  var passcode = $('<label>Passcode<input type="text" name="passcode" ' +
                 '/></label>');
  if (private.attr("checked")) {
    private.click();
  }
  private.click(function(a) {
    if (this.checked) {
      $("input[name='private']").parent().after(passcode);
    }
    else {
      passcode.detach();
    }
  });
  if ("{{ simplified }}".length) {
    var clip = new ZeroClipboard.Client();
    clip.setHandCursor(true);
    ZeroClipboard.setMoviePath('/static/js/ZeroClipboard.swf');
    clip.setText("{{ simplified }}");
    clip.glue($("p.clipboard")[0]);
    clip.addEventListener('onComplete', function() {
      $("p.clipboard").hide().html("Copied!").fadeIn();
    });
  }
});
