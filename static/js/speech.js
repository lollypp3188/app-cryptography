// If you modify this array, also update default language / dialect below.
const langs = [
  ['English', ['en-US', 'United States']],
  ['Українська', ['uk-UA']],
];

for (let i = 0; i < langs.length; i++) {
  select_language.options[i] = new Option(langs[i][0], i);
}
// Set default language / dialect.
select_language.selectedIndex = 0;
updateCountry();
select_dialect.selectedIndex = 0;
showInfo('info_start');

function updateCountry() {
  for (let i = select_dialect.options.length - 1; i >= 0; i--) {
    select_dialect.remove(i);
  }
  let list = langs[select_language.selectedIndex];
  for (let i = 1; i < list.length; i++) {
    select_dialect.options.add(new Option(list[i][1], list[i][0]));
  }
  select_dialect.style.visibility = list[1].length == 1 ? 'hidden' : 'visible';
}


let final_transcript = '';
let recognizing = false;
let ignore_onend;
let start_timestamp;

start_button.style.display = 'inline-block';
let recognition = new webkitSpeechRecognition();
recognition.continuous = true;
recognition.interimResults = true;

recognition.onstart = function() {
  recognizing = true;
  showInfo('info_speak_now');
  start_button.innerHTML = 'click to stop record'
};

recognition.onerror = function(event) {
  if (event.error == 'no-speech') {
    start_button.innerHTML = 'error no-speech'
    showInfo('info_no_speech');
    ignore_onend = true;
  }
  if (event.error == 'audio-capture') {
    start_button.innerHTML = 'error audio-capture'
    showInfo('info_no_microphone');
    ignore_onend = true;
  }
  if (event.error == 'not-allowed') {
    if (event.timeStamp - start_timestamp < 100) {
      showInfo('info_blocked');
    } else {
      showInfo('info_denied');
    }
    ignore_onend = true;
  }
};

recognition.onend = function() {
  recognizing = false;
  if (ignore_onend) {
    return;
  }
  start_button.innerHTML = 'click to start record'
  if (!final_transcript) {
    showInfo('info_start');
    return;
  }
  showInfo('');
  if (window.getSelection) {
    window.getSelection().removeAllRanges();
    let range = document.createRange();
    range.selectNode(document.getElementById('text'));
    window.getSelection().addRange(range);
  }

};

recognition.onresult = function(event) {
  let interim_transcript = '';
  if (typeof(event.results) == 'undefined') {
    recognition.onend = null;
    recognition.stop();
    upgrade();
    return;
  }
  for (let i = event.resultIndex; i < event.results.length; ++i) {
    if (event.results[i].isFinal) {
      final_transcript += event.results[i][0].transcript;
    } else {
      interim_transcript += event.results[i][0].transcript;
    }
  }
  final_transcript = capitalize(final_transcript);
  text.value = linebreak(final_transcript);
  text.placeholder = linebreak(interim_transcript);
  if (final_transcript || interim_transcript) {
    showButtons('inline-block');
  }
};


let two_line = /\n\n/g;
let one_line = /\n/g;
function linebreak(s) {
  return s.replace(two_line, '<p></p>').replace(one_line, '<br>');
}

let first_char = /\S/;
function capitalize(s) {
  return s.replace(first_char, function(m) { return m.toUpperCase(); });
}

function copyButton() {
  if (recognizing) {
    recognizing = false;
    recognition.stop();
  }
  showInfo('');
}

function startButton(event) {
  if (recognizing) {
    recognition.stop();
    return;
  }
  final_transcript = '';
  recognition.lang = select_dialect.value;
  recognition.start();
  ignore_onend = false;
  text.value = '';
  text.placeholder = '';
  showInfo('info_allow');
  showButtons('none');
  start_timestamp = event.timeStamp;
}

function showInfo(s) {
  if (s) {
    for (let child = info.firstChild; child; child = child.nextSibling) {
      if (child.style) {
        child.style.display = child.id == s ? 'inline' : 'none';
      }
    }
    info.style.visibility = 'visible';
  } else {
    info.style.visibility = 'hidden';
  }
}

let current_style;
function showButtons(style) {
  if (style == current_style) {
    return;
  }
  current_style = style;
}