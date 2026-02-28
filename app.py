from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
import pickle
import json
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load models and data
# IMPORTANT: Ensure your model files are in the same folder as app.py
rf_model = pickle.load(open(os.path.join(BASE_DIR, "rf_model.pkl"), "rb"))
lr_model = pickle.load(open(os.path.join(BASE_DIR, "linear_model.pkl"), "rb"))
df = pd.read_csv("city_day.csv")

features = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
all_cities = sorted(df["City"].unique().tolist())

# Coordinate Database for Mapping (Leaflet needs Lat/Lng)
CITY_COORDS = {
    "Delhi": [28.6139, 77.2090], "Mumbai": [19.0760, 72.8777],
    "Bengaluru": [12.9716, 77.5946], "Chennai": [13.0827, 80.2707],
    "Hyderabad": [17.3850, 78.4867], "Ahmedabad": [23.0225, 72.5714],
    "Kolkata": [22.5726, 88.3639], "Lucknow": [26.8467, 80.9462],
    "Bhopal": [23.2599, 77.4126], "Patna": [25.5941, 85.1376]
}

@app.route("/")
def page1():
    """Page 1: User Entry and Module Selection."""
    return render_template("page1.html", cities=all_cities)

@app.route("/process", methods=["POST"])
def process():
    """Route to handle Page 1 form and redirect to Page 2 or 3."""
    city = request.form.get("city")
    choice = request.form.get("view_choice") # 'dashboard' or 'map'
    theme = request.form.get("current_theme") # 'light' or 'dark'

    # Prepare flags for dashboard view
    if choice == "dashboard":
        show_lr = "on" if request.form.get("showLR") else "off"
        show_rf = "on" if request.form.get("showRF") else "off"
        show_radar = "on" if request.form.get("showRadar") else "off"
        return redirect(url_for('page2', city=city, lr=show_lr, rf=show_rf, radar=show_radar, theme=theme))
    
    elif choice == "map":
        # For map view, we pass all data by default
        return redirect(url_for('page3', city=city, theme=theme))
    
    else:
        # Default or error case
        return redirect(url_for('page1'))

@app.route("/dashboard")
def page2():
    """Page 2: The Data Analytics Dashboard."""
    city = request.args.get('city')
    # Use global theme flag if passed
    current_theme = request.args.get('theme', 'light')

    city_data = df[df["City"] == city].dropna(subset=features)
    avg_vals = [city_data[features].mean().values]
    
    pred_rf = round(rf_model.predict(avg_vals)[0], 2)
    pred_lr = round(lr_model.predict(avg_vals)[0], 2)
    
    category = "good" if pred_rf <= 100 else "moderate" if pred_rf <= 200 else "severe"
    # Recommendation text based on category
    rec = "Great day for outdoor activities!" if category == "good" else "Satisfactory, but sensitive groups should minimize time outdoors." if category == "moderate" else "Avoid all outdoor physical activity."

    return render_template("page2.html", 
                           city=city, pred_rf=pred_rf, pred_lr=pred_lr,
                           show_lr=request.args.get('lr')=="on",
                           show_rf=request.args.get('rf')=="on",
                           show_radar=request.args.get('radar')=="on",
                           pollutants=json.dumps(features),
                           pollutant_values=json.dumps(avg_vals[0].tolist()),
                           category=category, recommendation=rec, current_theme=current_theme)

@app.route("/map-view")
def page3():
    """Page 3: Geospatial Map Intelligence."""
    city = request.args.get('city')
    # Use global theme flag if passed
    current_theme = request.args.get('theme', 'light')

    city_data = df[df["City"] == city].dropna(subset=features)
    avg_vals = [city_data[features].mean().values]
    
    pred_rf = round(rf_model.predict(avg_vals)[0], 2)
    pred_lr = round(lr_model.predict(avg_vals)[0], 2)
    
    return render_template("page3.html", 
                           city=city, rf=pred_rf, lr=pred_lr,
                           coords=CITY_COORDS.get(city, [20.5937, 78.9629]), current_theme=current_theme) # Default to center of India

if __name__ == "__main__":
    app.run(debug=True)