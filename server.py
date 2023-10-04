from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
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

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again")
    
    else:
        user = crud.create_user(email, password)
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

    return redirect("/")


@app.route("/user_itinerary")
def all_user_itineraries():
    """"View all user itineraries"""

    user_itinerary = crud.get_user_itinerary()

    return render_template("all_user_itinerary.html", user_itinerary=user_itinerary)






if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)