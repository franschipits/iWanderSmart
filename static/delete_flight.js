const button = document.querySelector('#delete_flight');

button.addEventListener('click', (evt) => {
    
    const formAnswer = {
        delete_flight: evt.target.value
    };

    fetch('/delete_flight', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        },
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        alert('Flight deleted')
        window.location.href = '/profile'
    })
}) 