const button = document.querySelector('#delete_user_itinerary');

button.addEventListener('click', (evt) => {
    
    const formAnswer = {
        delete_itinerary: evt.target.value
    };

    fetch('/delete_itinerary', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        },
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        alert('itinerary deleted')
        window.location.href = '/profile'
    })
})
