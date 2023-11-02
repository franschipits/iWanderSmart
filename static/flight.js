const form = document.querySelector('#flight_info');

form.addEventListener('submit', (evt) => {
    evt.preventDefault(); 

    const formAnswer = {
        type_flight: document.querySelector('#type_flight').value,
        date_time: document.querySelector('#date_time').value,
        price: document.querySelector('#price').value,
        itinerary_to_add_to: document.querySelector('#itinerary_to_add_to').value,
    };

    fetch('/add_flight', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        }
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        document.querySelector('#flight_results')
        .insertAdjacentHTML('beforeend', `<div>
        <p>Type of Flight: ${responseJSON.type_flight} </p>
        <p>Date/Time: ${responseJSON.date_time} </p>
        <p>Price: ${responseJSON.price} </p>
    <button class="delete_flight btn btn-outline-secondary" id="${responseJSON.flight_id}"> Delete </button>
    </div>`)
    })

});



const deleteFlightButtons = document.querySelectorAll('button.delete_flight');
for (const deleteFlightButton of deleteFlightButtons) {
deleteFlightButton.addEventListener('click', (evt) => {
    const formAnswer = {
        delete_flight: evt.target.id
 
    }
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
        window.location.href = "/profile"
    })
});
}