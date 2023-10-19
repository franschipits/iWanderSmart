const form = document.querySelector('#notes_update');
const h2 = document.querySelector('#user_notes');

form.addEventListener('submit', (evt) => {
    evt.preventDefault();

    const formAnswer = {
        new_notes: document.querySelector('#notes').value
    };

    fetch('/notes_update', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        },
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        h2.innerHTML = responseJSON['notes'];
    })
})
