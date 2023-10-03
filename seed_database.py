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










