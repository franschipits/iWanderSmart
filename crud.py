"""CRUD operations."""

from model import db, User, User_Itinerary, Flights, Activities, Hotel, connect_to_db
def create_user(user_name, email, password, budget=0):
    """Create and return a new user."""

    user = User(
        user_name=user_name,
        email=email, 
        password=password,
        budget=budget,
    )

    return user
 
  
def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    
    return User.query.get(user_id)


def get_user_by_email(email):
    """"Return a user by email"""

    return User.query.filter(User.email == email).first()


def create_user_itinerary(creator, name_place):

    user_itinerary = User_Itinerary(
        creator=creator,
        name_place=name_place,
    )
 
    return user_itinerary


def get_user_itinerary(user):
    """Return all user itineraries."""

    return User_Itinerary.query.filter(User_Itinerary.user == user).first()


def get_user_itineraries():
    """Return all user itineraries."""

    return User_Itinerary.query.all()


def get_user_itinerary_by_id(user_itinerary_id):
    

    return User_Itinerary.query.get(user_itinerary_id)


# def create_saved_itinerary(user_id, user_itinerary_id):

#     saved_itinerary = Saved_Itinerary(
#         user_id=user_id,
#         user_itinerary_id=user_itinerary_id,
#     )

#     return saved_itinerary


def create_flights(user_itinerary_id, type_flight, date_time, price):

    flights = Flights(
        user_itinerary_id=user_itinerary_id,
        type_flight=type_flight,
        date_time=date_time,
        price=price,
    )

    return flights


# def create_itinerary_activities(user_itinerary_id, activities_id, price):

#     itinerary_activities = Itinerary_Activities(
#         user_itinerary_id=user_itinerary_id,
#         activities_id=activities_id,
#         price=price,
#     )

#     return itinerary_activities


def create_activities(name, address, contact_info, user_itinerary_id):

    activities = Activities(
        name=name,
        address=address,
        contact_info=contact_info,
        user_itinerary_id=user_itinerary_id,
    )

    return activities


def create_hotel(name, location, contact, user_itinerary_id, num_nights, price):

    hotel = Hotel(
        name=name,
        location=location,
        contact=contact,
        user_itinerary_id=user_itinerary_id,
        num_nights=num_nights,
        price=price,
    )

    return hotel
 





# def create_stays(hotel_id, user_itinerary_id, price, num_nights):

#     stays = Stays(
#         hotel_id=hotel_id,
#         user_itinerary_id=user_itinerary_id,
#         price=price,
#         num_nights=num_nights,
#     )

#     return stays
 

# def create_places(country, state, city, passport, visa):

#     places = Places(
#         country=country,
#         state=state,
#         city=city,
#         passport=passport,
#         visa=visa,
#     )

#     return places

def get_flights_by_itinerary_id(user_itinerary_id):

    return Flights.query.filter_by(user_itinerary_id=user_itinerary_id).all()

def get_hotels_by_itinerary_id(user_itinerary_id):

    return Hotel.query.filter_by(user_itinerary_id=user_itinerary_id).all()

def get_activities_by_itinerary_id(user_itinerary_id):

    return Activities.query.filter_by(user_itinerary_id=user_itinerary_id).all()

def get_flight_by_id(flight_id):

    return Flights.query.get(flight_id)

def get_hotel_by_id(hotel_id):

    return Hotel.query.get(hotel_id)

def get_activity_by_id(activities_id):

    return Activities.query.get(activities_id)
  

if __name__ == '__main__':
    from server import app
    connect_to_db(app)