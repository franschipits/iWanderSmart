"""Script to seed database."""

import os
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb travels")
os.system('createdb travels')

model.connect_to_db(server.app)
model.db.create_all()

#User:
users = []
names = ["Stone", "Fredric", "Cornelius", "Kaitlyn", "Destinee", "Stacia", "Addie", "Roman", "Eliott", "Davin", "Maisy"]
for n in range(10):
    email = f'{names[n]}@test.com'
    password = 'password'
    user_name = f'{names[n]}'

    user = crud.create_user(user_name, email, password)
    users.append(user)


model.db.session.add_all(users)
model.db.session.commit()

#Places:
places = [{'country':"Brazil",
           'state':"Sao Paulo",
           'city':"Boituva",
           'passport':True,
           'visa':False}, 
           
           {'country':"United States",
            'state':"Illinois",
            'city':"Chicago",
            'passport':False,
            'visa':False}, 
            
            {'country':"United States",
             'state':"Texas",
             'city':"Austin",
             'passport':False,
             'visa':False}]

list_places = []

for place in places:
    new_place = crud.create_places(place['country'], place['state'], place['city'], place['passport'], place['visa'])
    list_places.append(new_place)

model.db.session.add_all(list_places)
model.db.session.commit()


#User_Itinerary:
user_itinerary = []

for user in users:
    current_place = choice(list_places)
    new_itinerary = crud.create_user_itinerary(user.user_id, current_place.places_id)
    user_itinerary.append(new_itinerary)


model.db.session.add_all(user_itinerary)
model.db.session.commit()


#Flights:
flights = [{'type_flight':"departure",
           'date_time':"10/25/2023 7:00pm",
           'price': 500.00}, 
           
           {'type_flight':"departure",
           'date_time':"05/18/2024 10:00pm",
           'price': 250.00}, 
            
            {'type_flight':"departure",
           'date_time':"12/07/2023 6:00am",
           'price': 185.00}, 
           ]

list_flights = []

for flight in flights:
    new_flight = crud.create_flights(user_itinerary[0].user_itinerary_id, flight['type_flight'], flight['date_time'], flight['price'])
    list_flights.append(new_flight)

model.db.session.add_all(list_flights)
model.db.session.commit()


#Saved_Itinerary:
#User #1 saves Itinerary #2
#User #4 saves Itinerary #1

saved_itineraries = []

new_save = crud.create_saved_itinerary(users[1].user_id, user_itinerary[2].user_itinerary_id)
saved_itineraries.append(new_save)

new_save2 = crud.create_saved_itinerary(users[4].user_id, user_itinerary[1].user_itinerary_id)
saved_itineraries.append(new_save2)

model.db.session.add_all(saved_itineraries)
model.db.session.commit()

# TODO: Add activities, itinerary_activities, hotels and stays later.


