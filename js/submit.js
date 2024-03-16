(uri => {
    // Register a listener for submit events.
    const form = document.getElementById("cesarForm")
    form.addEventListener('submit', evt => {
    // Suppress the default behavior of the form.
    evt.preventDefault();
    // Submit the form data.
    console.log( new FormData(evt.target))
    fetch(uri, {
        method: 'post',
        body: new FormData(evt.target)
    }).then(resp => resp.json()) // <-- !!!
        .then(text => {
        console.log(text);
        // Handle response here.
        const elem = document.getElementById('result');
        elem && (elem.innerHTML = text.result);
        });
    // Reset the form.
    // evt.target.reset();
    });
})({{ url_for('cesar')| tojson }})
