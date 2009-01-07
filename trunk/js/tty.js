// This is a singleton (because of the input keypress callback.)
var the_terminal = null;

function initTerminal(input, output, height, enter_callback) {
  if (the_terminal != null) {
    alert("Terminal already initialized!");
  } else {
    the_terminal = new Terminal(input, output, height, enter_callback);
  }
  return the_terminal;
}

function Terminal(input, output, height, enter_callback) {
  // Public interface

  // Replace the terminal contents with 'lines'.
  this.replaceLines = function(lines) {
    var length = lines.length;
    if (length > this.height) {
      lines = lines.slice(length - this.height);
    } else if (length < this.height) {
      var pad = new Array(this.height - length);
      for (var i = 0; i < pad.length; i++) {
	pad[i] = "";
      }
      lines = pad.concat(lines);
    }
    this.output.innerHTML = lines.join("<br>");
  };

  // Queue lines to be appended to the terminal output.
  this.queueLines = function(lines) {
    this.pending_lines = this.pending_lines.concat(lines);
    if (this.adder_timeout == null) {
      this.scrollLines_();
    }
  };

  // Private methods

  // Return the lines on the screen.
  this.screenLines_ = function() {
    return this.output.innerHTML.split("<br>");
  }

  // Append 'lines' to the terminal output and scroll them up.
  this.appendLines_ = function(lines) {
    if (lines.length > 0) {
      this.replaceLines(this.screenLines_().concat(lines));
    }
  }

  // Scroll lines up.  Repeat.  Called from a timeout callback.
  this.scrollLines_ = function() {
    if (this.pending_lines.length == 0) {
      clearTimeout(this.adder_timeout);
      this.adder_timeout = null;
    } else {
      this.appendLines_([this.pending_lines.shift()]);
      var terminal = this;
      this.adder_timeout =
        setTimeout(function() { terminal.scrollLines_(); }, 200);
    }
  };

  // Flush the queued output.
  this.flushLines_ = function() {
    if (this.adder_timeout != null) {
      clearTimeout(this.adder_timeout);
      this.adder_timeout = null;
    }
    if (this.pending_lines.length > 0) {
      var linesLeft = this.pending_lines;
      this.pending_lines = [];
      this.appendLines_(linesLeft);
    }
  };

  // Handles a keyPress in the input field.
  this.onKeyPress = function(event) {
    this.flushLines_();
    if (getKeyCode(event) == 13) {
      var input_line = this.input.value;
      this.input.value = "";
      this.enter_callback(input_line);
      this.input.focus();
    }
  }

  this.input = input;
  this.output = output;
  this.height = height;
  this.enter_callback = enter_callback;

  this.adder_timeout = null;
  this.pending_lines = [];

  this.input.setAttribute("onKeyPress",
                          "the_terminal.onKeyPress(event);");
  this.input.focus();
  this.replaceLines([]);

  the_terminal = this;
}
