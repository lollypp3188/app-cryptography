
// Register a listener for submit events.
const form = document.getElementById("cesarForm")
form.addEventListener('submit', evt => {
    evt.preventDefault();

    fetch('/cesar', {
        method: 'post',
        body: new FormData(evt.target)
    }).then(resp => resp.json())
        .then(text => {
            const elem = document.getElementById('result');
            elem && (elem.innerHTML = text.result);
        });
    // Reset the form.
    // evt.target.reset();
});
