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
            const wrapper = document.getElementById('result-wrapper')
            const elem = document.getElementById('result');
            if(elem && text?.result){
                wrapper.className = 'flex gap-3 my-4'
                elem.innerHTML = text.result
            } else {
                wrapper.className = 'hidden'
            }
        });
    // Reset the form.
    // evt.target.reset();
});
