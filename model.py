"""Models for budget travel app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

 
class User(db.Model):
    """A user"""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    budget = db.Column(db.Float)

    # saved_itineraries = db.relationship("Saved_Itinerary", back_populates="user")
    user_itineraries = db.relationship("User_Itinerary", back_populates="user")
    
    def __repr__(self):
        """Show info about the user"""

        return f"<User user_id={self.user_id} name={self.user_name}>"

 

class User_Itinerary(db.Model):
    """"A User Itinerary"""
    __tablename__ = "user_itinerary"

    user_itinerary_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    creator = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    name_place = db.Column(db.String)
    notes = db.Column(db.Text, default="Take notes here!")

 
    
    # places_id = db.Column(db.Integer, db.ForeignKey("places.places_id"))


    # saved_itineraries = db.relationship("Saved_Itinerary", back_populates="user_itinerary")
    activities = db.relationship("Activities", back_populates="user_itinerary")
    hotels = db.relationship("Hotel", back_populates="user_itinerary")
    flights = db.relationship("Flights", back_populates="user_itinerary")
    # places = db.relationship("Places", back_populates="user_itinerary")
    user = db.relationship("User", back_populates="user_itineraries")


    def __repr__(self):
        """"Show info about the user itinerary"""

        return f"<User_Itinerary user_itinerary_id={self.user_itinerary_id} creator={self.creator}>"
    

    
# class Saved_Itinerary(db.Model):
#     """"The itineraries saved by the user"""
#     __tablename__ = "saved_itineraries"

#     saved_itineraries_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
#     user_itinerary_id = db.Column(db.Integer, db.ForeignKey("user_itinerary.user_itinerary_id"))

#     user = db.relationship("User", back_populates="saved_itineraries")
#     user_itinerary = db.relationship("User_Itinerary", back_populates="saved_itineraries")

#     def __repr__(self):
#         return f"<Saved_Itinerary saved_itineraries_id={self.saved_itineraries_id} user_itinerary={self.user_itinerary}>"
    
 

class Flights(db.Model):
    """Information about the flights"""
    __tablename__ = "flights"

    flight_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_itinerary_id = db.Column(db.Integer, db.ForeignKey("user_itinerary.user_itinerary_id"))
    type_flight = db.Column(db.String)
    date_time = db.Column(db.DateTime)
    price = db.Column(db.Float)

    user_itinerary = db.relationship("User_Itinerary", back_populates="flights")

    def __repr__(self):
        return f"<Flights flight_id={self.flight_id} type_flight={self.type_flight}>"
    
    
 
class Activities(db.Model):
    """Information about specific activities"""
    __tablename__ = "activities"

    activities_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    contact_info = db.Column(db.String)
    price = db.Column(db.Float)
    user_itinerary_id = db.Column(db.Integer, db.ForeignKey("user_itinerary.user_itinerary_id"))

    user_itinerary = db.relationship("User_Itinerary", back_populates="activities")

    def __repr__(self):
        return f"<Activities activities_id={self.activities_id} name={self.name}>"



class Hotel(db.Model):
    """Information about specific hotel"""
    __tablename__ = "hotel"

    hotel_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    contact = db.Column(db.String)

    user_itinerary_id = db.Column(db.Integer, db.ForeignKey("user_itinerary.user_itinerary_id"))
    price = db.Column(db.Float)
    num_nights = db.Column(db.Integer)

    user_itinerary = db.relationship("User_Itinerary", back_populates="hotels")

    def __repr__(self):
        return f"<Hotel hotel_id={self.hotel_id} name={self.name}>"
    
    


# class Places(db.Model):
#     """Information about places to go"""
#     __tablename__ = "places"

#     places_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     country = db.Column(db.String)
#     state = db.Column(db.String)
#     city = db.Column(db.String)
#     passport = db.Column(db.Boolean)
#     visa = db.Column(db.Boolean)

#     user_itinerary = db.relationship("User_Itinerary", back_populates="places")

#     def __repr__(self):
#         return f"<Places places_id={self.places_id} country={self.country}>"


def connect_to_db(flask_app, db_uri="postgresql:///travels", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == '__main__':
    import server
    connect_to_db(server.app) 