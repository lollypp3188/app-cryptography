// Register a listener for submit events.
document.getElementById('vigenereForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let key = document.getElementById('key').value;
    let text = document.getElementById('text').value;
    let action = document.getElementById('action').value;
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/vigenere', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.error) {
                document.getElementById('errorMessage').textContent = response.error;
                document.getElementById('result').textContent = '';
            } else {
                document.getElementById('errorMessage').textContent = '';
                document.getElementById('result').innerHTML = '<h2>Result:</h2><p>' + response.result + '</p>';
            }
        }
    };
    xhr.send('key=' + encodeURIComponent(key) + '&text=' + encodeURIComponent(text) + '&action=' + encodeURIComponent(action));
});