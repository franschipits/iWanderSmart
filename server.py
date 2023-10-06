from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db, User, User_Itinerary, Saved_Itinerary
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route("/users")
def all_users():
    """"View all users"""

    users = crud.get_users()

    return render_template("all_users.html", users=users)


@app.route("/users", methods=["POST"])
def register_user():
    """"Create a new user"""

    user_name = request.form.get('user_name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again")
    
    else:
        user = crud.create_user(user_name, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")


@app.route("/users/<user_id>")
def show_user(user_id):
    """"Show details on a particular user"""""

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)


@app.route("/login", methods=["POST"])
def user_login():

    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email(email)

    if not user:
        flash("Login incorrect")

    elif password != user.password:
        flash("Password incorrect")

    else:
        session['current_user'] = user.email
        flash("Logged in!")
        return redirect("/profile")
    
    return redirect("/")


@app.route("/profile")
def show_profile():

    user = crud.get_user_by_email(session["current_user"])
    itineraries = Saved_Itinerary.query.filter_by(user_id=user.user_id).all()
    user_itineraries = User_Itinerary.query.filter_by(creator=user.user_id).all()

    return render_template("profile.html", user=user, itineraries=itineraries, user_itineraries=user_itineraries)


@app.route("/user_itinerary")
def all_user_itineraries():
    """"View all user itineraries"""

    user_itinerary = crud.get_user_itinerary()

    return render_template("all_user_itinerary.html", user_itinerary=user_itinerary)


@app.route("/user_itinerary/<user_itinerary_id>")
def show_user_itinerary(user_itinerary_id):
    """"Show details on a particular itinerary"""

    user_itinerary = crud.get_user_itinerary_by_id(user_itinerary_id)

    return render_template("user_itinerary_details.html", user_itinerary=user_itinerary)


#VIEW ITINERARIES THAT USER CREATED AFTER USER LOG IN:
# @app.route("/user_itinerary")
# def all_user_itineraries():
#     """"View all user itineraries"""

#     # If the user isn't logged in, flash a message saying "please log in" and redirect to homepage
#     # If the user is logged in, their email is in session['current_user']
#     # To get all THAT USER's itineraries:
#     #       Look up the user ID for that email
#     #           0) The user's email address will be session['current_user']
#     #           1) get their email, the use user = crud.get_user_by_email(...)
#     #           2) their ID is user.user_id
#     #       Find all the user_itineraries that have that ID for their creator
#     #           0) User_Itinerary.query.filter_by(creator=user.user_id)
#     # Give all those itineraries to the render_template to show in HTML
#     login = session['current_user'] = user.email

#     if not login:
#         flash("Please log in")

#     else:
#         user = crud.get_user_by_email(user.email)
#         user = crud.get_user_by_id(user.user_id)
#         User_Itinerary.query.filter_by(creator=user.user_id)
    

#     return render_template("all_user_itinerary.html", user_itinerary=user_itinerary)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)