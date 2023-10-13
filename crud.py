"""CRUD operations."""

from model import db, User, User_Itinerary, Flights, Itinerary_Activities, Activities, Hotel, Stays, Places, connect_to_db
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


def create_user_itinerary(creator, places_id):

    user_itinerary = User_Itinerary(
        creator=creator,
        places_id=places_id,
    )
 
    return user_itinerary


def get_user_itinerary():
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


def create_itinerary_activities(user_itinerary_id, activities_id, price):

    itinerary_activities = Itinerary_Activities(
        user_itinerary_id=user_itinerary_id,
        activities_id=activities_id,
        price=price,
    )

    return itinerary_activities


def create_activities(name, address, contact_info):

    activities = Activities(
        name=name,
        address=address,
        contact_info=contact_info,
    )

    return activities


def create_hotel(name, location, contact):

    hotel = Hotel(
        name=name,
        location=location,
        contact=contact,
    )

    return hotel
 

def create_stays(hotel_id, user_itinerary_id, price, num_nights):

    stays = Stays(
        hotel_id=hotel_id,
        user_itinerary_id=user_itinerary_id,
        price=price,
        num_nights=num_nights,
    )

    return stays


def create_places(country, state, city, passport, visa):

    places = Places(
        country=country,
        state=state,
        city=city,
        passport=passport,
        visa=visa,
    )

    return places



if __name__ == '__main__':
    from server import app
    connect_to_db(app)