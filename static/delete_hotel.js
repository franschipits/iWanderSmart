const button = document.querySelector('#delete_hotel');

button.addEventListener('click', (evt) => {
    
    const formAnswer = {
        delete_hotel: evt.target.value
    };

    fetch('/delete_hotel', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        },
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        alert('Hotel deleted')
        window.location.href = '/profile'
    })
})
