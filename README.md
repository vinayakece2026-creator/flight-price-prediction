Flight Fare Prediction — Work Completed and Workflow
1. Data preprocessing: Loaded the flight dataset and cleaned the data by handling date, departure time, arrival time, duration, and total stops.
2. Feature engineering: Extracted journey day, month, weekday, departure hour, arrival hour, duration in minutes, and number of stops. Applied one-hot encoding to categorical features such as Airline, Source, Destination, and Additional Info.
3. Model training: Trained machine learning regression models to estimate flight ticket prices and selected the tuned Bagging Regressor as the final model.
4. Model saving: Saved the trained model as flight_price_model.pkl and the feature column names as flight_price_columns.pkl.
5. Flask application: Developed app.py to load the trained model, receive flight details from the user, prepare the input features, and generate a predicted ticket price.
6. Web interface: Created templates/index.html for the flight input form and static/style.css to style the application.
7. Model integration: Connected the HTML form to Flask so that users can enter flight details and view the estimated ticket price.
8. Local testing: Ran the Flask application locally and tested the prediction form to confirm that the model receives the expected 36 input features.
9. GitHub upload: Uploaded the project files to GitHub for version control and deployment.
10. Cloud deployment: Deployed the Flask application on Render and obtained a public live demo URL.
11. Prediction validation: Identified that the predicted fare can differ from current MakeMyTrip prices because the model estimates prices from historical data rather than retrieving live booking fares.
12. Resume preparation: Prepared the project to showcase Python, Pandas, Scikit-learn, machine learning regression, Flask, GitHub, and Render deployment.
Project links
- Live Demo: [https://flight-price-prediction-eh1a.onrender.com](https://flight-price-prediction-eh1a.onrender.com)
- GitHub: https://github.com/vinayakece2026-creator/flight-price-prediction
