const deleteActivityButtons = document.querySelectorAll('button.delete_activities');
for (const deleteActivityButton of deleteActivityButtons) {
deleteActivityButton.addEventListener('click', (evt) => {
    const formAnswer = {
        delete_activity: evt.target.id,
        itinerary_id: evt.target.name
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
        alert('Activity deleted')
        window.location.href = `/user_itinerary/${responseJSON.itinerary_id}`
    })
});
}

 