const notes_form = document.querySelector('#notes_update');
const notes_h2 = document.querySelector('#user_notes');

notes_form.addEventListener('submit', (evt) => {
    evt.preventDefault();

    const formAnswer = {
        new_notes: document.querySelector('#notes').value,
        note_update: document.querySelector('#note_update_itin_id').value
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
        notes_h2.innerHTML = responseJSON.notes;
    })
})
