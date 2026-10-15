
from flask import Flask, render_template, request
import joblib
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Load the trained ML model
model = joblib.load("flight_price_model.pkl")

# Load the feature columns
feature_columns = joblib.load("flight_price_columns.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get details from the HTML form
    airline = request.form["airline"]
    source = request.form["source"]
    destination = request.form["destination"]

    journey_date = datetime.strptime(
        request.form["journey_date"], "%Y-%m-%d"
    )

    departure_time = request.form["departure_time"]
    arrival_time = request.form["arrival_time"]

    dep_hour, dep_minute = map(int, departure_time.split(":"))
    arr_hour, arr_minute = map(int, arrival_time.split(":"))

    stops = request.form["stops"]

    stops_map = {
        "non-stop": 0,
        "1 stop": 1,
        "2 stops": 2,
        "3 stops": 3,
        "4 stops": 4
    }

    duration = int(request.form["duration"])
    additional_info = request.form["additional_info"]

    # Prepare numerical features
    numeric_features = {
        "Journey_Day": journey_date.day,
        "Journey_month": journey_date.month,
        "Journey_weekday": journey_date.weekday(),
        "Dep_Hour": dep_hour,
        "Dep_minute": dep_minute,
        "Arrival_Hour": arr_hour,
        "Arrival_minute": arr_minute,
        "Total_Stops_Num": stops_map[stops],
        "Duration_Minutes": duration
    }

    # Create one row with the exact training columns
    input_data = pd.DataFrame(
        0, index=[0], columns=feature_columns
    )

    for column, value in numeric_features.items():
        if column in input_data.columns:
            input_data.loc[0, column] = value

    # Normalize destination as in training
    if destination == "New Delhi":
        destination = "Delhi"

    # Set categorical dummy columns
    categories = {
        "Airline": airline,
        "Source": source,
        "Destination": destination,
        "Additional_Info": additional_info
    }

    for column, value in categories.items():
        dummy_column = f"{column}_{value}"

        if dummy_column in input_data.columns:
            input_data.loc[0, dummy_column] = 1

    # Check the input structure
    print("Input shape:", input_data.shape)
    print("Expected features:", len(feature_columns))
    print(
        "Input columns match:",
        list(input_data.columns) == feature_columns
    )
    print(input_data)

    # Predict flight price
    prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction_text=f"Estimated flight price: ₹{prediction:,.2f}"
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
