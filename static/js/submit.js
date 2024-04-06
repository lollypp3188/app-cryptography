const urlParams = new URL(document.currentScript.src).searchParams;
const formId = urlParams.get('formId');
const fetchUrl = urlParams.get('fetchUrl');


// Register a listener for submit events.
const form = document.getElementById(formId)
form.addEventListener('submit', evt => {
    evt.preventDefault();

    fetch(`/${fetchUrl}`, {
        method: 'post',
        body: new FormData(evt.target)
    }).then(resp => resp.json())
        .then(text => {
            const elem = document.getElementById('result');
            if(elem && text?.result){
                elem.className = 'border border-accent p-2 my-4 w-full max-w-full flex rounded-btn'
                elem.innerHTML = text.result
            } else {
                elem.className = 'hidden'
            }
        });
    // Reset the form.
    // evt.target.reset();
});
