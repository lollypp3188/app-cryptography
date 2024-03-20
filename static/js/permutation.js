// Register a listener for submit events.
const form = document.getElementById("permutationForm")
form.addEventListener('submit', evt => {
    evt.preventDefault();

    fetch('/permutation', {
        method: 'post',
        body: new FormData(evt.target)
    }).then(resp => resp.json())
        .then(text => {
            const elem = document.getElementById('result');
            elem && (elem.innerHTML = text.result);
            if(elem && text?.result){
                elem.className = 'border border-accent p-2 my-4 w-full max-w-full flex rounded-btn'
            } else {
                elem.className = 'hidden'
            }
        });
});