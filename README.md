# VayuSense
To predict Air Quality Index (AQI) using environmental pollutant data and  analyze pollution trends across Indian cities
<h2>Geospatial Air Quality Intelligence</h2>
VayuSense is an interactive web portal designed to monitor and predict urban air quality across major Indian cities. By combining machine learning with dynamic mapping, the platform allows users to switch between a deep-dive Analytics Dashboard and a high-level Geospatial Map View.

<hr><h2>📌 Project Overview</h2>
The application serves as a dual-view interface for environmental data:
<ul>
  <li>Analytics View: Provides a comparative study of Actual vs. Predicted AQI using Random Forest models, supplemented by radar charts for pollutant breakdowns.</li>
  <li>Map View: An interactive Leaflet.js integration that plots city-specific air quality data on a geographic layer, providing instant spatial context.</li>
</ul>

<hr><h2>🎯 Problem Statement</h2>
Raw environmental data is often difficult for the general public to interpret. While datasets like city_day.csv contain vast amounts of information, they lack the visual "storytelling" needed to understand how pollution travels or how a model's prediction compares to historical reality. VayuSense bridges this gap through intuitive UI and spatial visualization.

<hr><h2>📊 Dataset Description</h2>
The project is built upon the city_day.csv dataset, focusing on several key features:</br>
<ul>
  <li><b>Cities Covered:</b> Delhi, Mumbai, Bengaluru, Chennai, Hyderabad, and more.</br></li>
  <li><b>Pollutants Analyzed</b>: PM_{2.5}, PM_{10}, NO_2, SO_2, CO, and O_3.</br></li>
  <li><b>Target</b>: The official Air Quality Index (AQI) recorded for each city.</li>
</ul>

<hr><h2>🧠 Machine Learning Workflow</h2>
<ul>
  <li><b>Feature Engineering:</b> Extracting the latest recorded pollutant levels for each unique city in the database.</br></li>
  <li><b>Model Selection:</b> Utilizing Random Forest Regression for its ability to handle non-linear relationships in atmospheric data.</br></li>
  <li><b>Accuracy:</b> The model maintains a high R^2 Score (approx. 0.989), ensuring that predictions closely align with historical sensors.</li>
</ul>

<hr><h2>🛠️ Technologies Used</h2>
<ul>
  <li>Framework: Flask (Python)</li>
  <li>Data Science: Pandas, Scikit-Learn, Pickle</li>
  <li>Mapping: Leaflet.js (OpenStreetMap Tiles)</li>
  <li>Visualization: Chart.js (Bar and Radar charts)</li>
  <li>Frontend: HTML5/CSS3 with a focus on Glassmorphism and Responsive Design.</li>
</ul>

<hr><h2>🚀 Future Enhancements</h2>
<ul>
  <li>Live API Integration: Replacing static CSV data with live feeds from the OpenWeatherMap Air Pollution API.</li>
  <li>Predictive Heatmaps: Generating color-coded heatmaps across the entire country based on predicted wind patterns.</li>
  <li>Historical Timeline: A slider to view how a city's air quality has improved or declined over the last 5 years.</li>
</ul>
<hr><h2>✨ Key Features</h2>
 VayuSense features a high-end, responsive UI that adapts to user preference. Using CSS Variables and JavaScript, the dashboard transitions between:
<ul>
  <li>Light Mode: A clean, "Aero" aesthetic with soft shadows and high readability.</li>
  <li>Dark Mode: A "Midnight" theme designed to reduce eye strain, using deep slate tones and neon accents for data points.</li>
 
</ul>



