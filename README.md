# About me
Franciane is a Brazilian living in the US for 6 years.  In Brazil Fran went to College for Business Management.  She was a financial analyst where she uses to do bank reconciliations and manage providers accounts. Most recently Fran was a freelance photographer, where she had to manage her own small business and client relations. She now started a Software Engineering program at Hackbright Academy, where she is learning full stack programming to prepare for a career in Software Engineering. She loves learning new things and she looks forward to finding a job as a backend Software Engineer where she can put into practice her programming skills. With her background in finance and her passion for photography and traveling, Fran got inspired to create this application, combining her experiences and passions into a single platform. 
![Contact info image](/static/images/FrancianeSchipits.png)

# iWanderSmart
The iWanderSmart is an itinerary builder application made with `Python` and `Flask`. It is designed to improve travel planning, allowing users to create personalized travel itineraries while staying within a predefined budget.

# Tech Stack 
- Python
- HTML
- Jinja2
- Flask
- PostgreSQL
- SQLAlchemy
- JavaScript
- CSS
- Bootstrap

# Features
The app allows users to create an account, log in and log out of their account. 
![Homepage image](/static/images/gif-project-login.gif)

When a user logs in, they are taken to their profile page, where they can input their budget. I used `AJAX` to create a dynamic budget update feature, allowing users to update their budgets without requiring a full page refresh. Under My Itineraries, users can also visualize their Budget per day in each itinerary, being able to compare itineraries and decide which one can fit best within their budget at the moment.
![Profile page image](/static/images/gif-budget-update.gif)

Users can also create a new itinerary by simply naming them and clicking the “create” button. Then they can navigate to the itinerary details page, where they can input their flight and hotel information. They can also remove items from a specific itinerary or delete the itinerary as a whole.
![User itinerary details page image](/static/images/gif-create-itinerary.gif)

The Google Places `API` enables users to search for, and add, accommodation information and activities to their itinerary, being able to also view photos and the location on the map. And all the data entered is stored in my `Postgres` database using `SQLAlchemy`.
![Search page image](/static/images/gif-google-places-api.gif)

Upon entering this information, the application will automatically calculate the remaining budget by deducting the costs of flights and hotels, and then display the user's daily budget. 
![User itinerary details page image](/static/images/User-itinerary-details-page.png)

Additionally, at the bottom of the page, a curated list of restaurant recommendations will be provided, tailored to the user's remaining daily budget. The Google Places `API` provided a list of information about restaurants including price range and ratings, which was very useful for this feature.
![Restaurant Suggestion image](/static/images/gif-restaurant-suggestions.gif)

Another notable feature is the "All Users Itineraries", offering users the opportunity to browse, save and edit copies of itineraries created by fellow users directly in their own profiles.
![All User itineraries page image](/static/images/gif-all-users-itineraries.gif)

I styled my app using a combination of `Bootstrap` and `CSS` to create a visually appealing, well-organized layout.

This application was created so users can plan their dream getaway while maintaining control of their finances. Set your budget, and iWanderSmart will help you keep track of your expenses, ensuring you stay within your financial limits.

# Installing iWanderSmart
Clone this repo into your computers directory:
```python
https://github.com/franschipits/iWanderSmart.git
```

Create your virtual environment inside your iWanderSmart Directory:
```python
virtualenv env
```

Activate the environment:
```python
source env/bin/activate
```

Install the Requirements:
```python
pip install -r requirements.txt
```

Create your database(db):
```python
createdb travels
  python3 -i model.py
       >>db.create_all()
```

Sign up to use the [Google Places API](https://developers.google.com/maps/documentation/places/web-service/overview)

Run the application:
```python
python3 server.py
```

You can now access iWanderSmart at 'localhost:5000/' and start creating your itineraries!


 