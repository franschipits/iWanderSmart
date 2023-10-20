const form = document.querySelector('#budget_update');
const h2 = document.querySelector('#user_budget');

form.addEventListener('submit', (evt) => {
    evt.preventDefault();

    const formAnswer = {
        new_budget: document.querySelector('#budget').value
    };

    fetch('/budget_update', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        },
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        h2.innerHTML = responseJSON['budget'];
    })
})
 