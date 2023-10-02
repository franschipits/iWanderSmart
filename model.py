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

    saved_itineraries = db.relationship("Saved_Itinerary", back_populates="user")
    

    def __repr__(self):
        """Show info about the user"""

        return f"<User user_id={self.user_id} email={self.email}>"


class Movie(db.Model):
    """"A movie"""
    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    ratings = db.relationship("Rating", back_populates="movie")

    def __repr__(self):
        """"Show info about the movie"""

        return f"<Movie movie_id={self.movie_id} title={self.title}>"
    
    
class Rating(db.Model):
    """"A movie rating"""
    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    movie = db.relationship("Movie", back_populates="ratings")
    user = db.relationship("User", back_populates="ratings")

    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} score={self.score}>"