const forms = document.querySelectorAll('.save_itinerary');
for(const form of forms) {
    form.addEventListener('submit', (evt) => {
    evt.preventDefault(); 

    const formAnswer = {
        name_place: form.querySelector('#save_name_place').value,
        save_hotels: form.querySelector('#save_hotels').value,
        save_activities: form.querySelector('#save_activities').value,
        itinerary_to_save: form.querySelector('#itinerary_to_save').value,
    };
 
    fetch('/save_itinerary', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        }
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        document.querySelector('#save_itinerary')
        .insertAdjacentHTML('beforeend', 
        `<li>${responseJSON.save_name_place} </li>
        <li>${responseJSON.save_hotels} </li>
        <li>${responseJSON.save_activities} </li>`)
    })

});
}

 