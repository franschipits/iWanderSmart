const deleteActivityButtons = document.querySelectorAll('button.delete_activities');
for (const deleteActivityButton of deleteActivityButtons) {
deleteActivityButton.addEventListener('click', (evt) => {
    const formAnswer = {
        delete_activities: evt.target.id

    }
    fetch('/delete_activity', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        },
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        alert('Ativity deleted')
        window.location.href = '/profile'
    })
});
}
