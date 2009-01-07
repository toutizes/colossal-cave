function ajax(url, callback) {
  var request = new XMLHttpRequest();
  request.open("GET", url, true);
  request.onreadystatechange = function() {
    if (request.readyState == 4 && request.status == 200) {
      callback(request.responseText);
    }
  }
  request.send(null);
}

function getKeyCode(event) {
  var key = 0;
  var is_control = false;
  if (!event) {
    event = window.event;
  }
  if (event.which) {
    key = event.which;
    is_control = event.ctrlKey;
  }
  return is_control ? (key & 0x1f) : key;
}

function windowHeight() {
  if (typeof(window.innerHeight) == 'number') {
    // Non IE
    return window.innerHeight;
  } else if (document.documentElement && document.documentElement.clientHeight) {
    // IE 6+ in 'standards compliant mode'
    return document.documentElement.clientHeight;
  } else if (document.body && document.body.clientHeight) {
    // IE 4 compatible
    return document.body.clientHeight;
  } else {
    return 0;
  }
}