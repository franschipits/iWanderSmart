const delete_buttons = document.querySelectorAll('button.delete_hotel');
for (const delete_button of delete_buttons) {
delete_button.addEventListener('click', (evt) => {
    const formAnswer = {
        delete_hotel: evt.target.id

    }
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
});
}
