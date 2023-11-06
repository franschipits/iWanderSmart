Hi, I’m Fran! And with my background in finance and my passion for photography and traveling, I got inspired to create this application, combining my experiences and passions into a single platform.
![Contact info image](/static/images/Franciane Schipits.png)
The iWanderSmart is an itinerary builder application made with Python and Flask. It is designed to improve travel planning, allowing users to create personalized travel itineraries while staying within a predefined budget.

The app allows users to create an account, log in and log out of their account. When a user logs in, they are taken to their profile page, where they can input their budget. I used AJAX to create a dynamic budget update feature, allowing users to update their budgets without requiring a full page refresh.
![Homepage image](/static/images/iWanderSmart - Homepage.png)

Users can also create a new itinerary by simply naming them and clicking the “create” button. Then they can navigate to the itinerary details page, where they can input their flight  and hotel information. The Google Places API enables users to search for, and add, accommodation information and activities to their itinerary, being able to also view photos and the location on the map. And all the data entered is stored in my Postgres database using SQLAlchemy.

Upon entering this information, the application will automatically calculate the remaining budget by deducting the costs of flights and hotels, and then display the user's daily budget. 

Additionally, at the bottom of the page, a curated list of restaurant recommendations will be provided, tailored to the user's remaining daily budget.

Another notable feature is the "All Users Itineraries", offering users the opportunity to browse, save and edit copies of itineraries created by fellow users directly in their own profiles.

I styled my app using a combination of Bootstrap and CSS to create a visually appealing, well-organized layout.

This application was created so users can plan their dream getaway while maintaining control of their finances. Set your budget, and iWanderSmart will help you keep track of your expenses, ensuring you stay within your financial limits.
 