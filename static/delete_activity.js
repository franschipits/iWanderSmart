const button = document.querySelector('#delete_activities');

button.addEventListener('click', (evt) => {
    
    const formAnswer = {
        delete_activities: evt.target.value
    };

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
        window.location.href = '/profile'
    })
})