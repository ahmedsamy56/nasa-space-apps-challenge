from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset from the URL
data_url = "https://raw.githubusercontent.com/LawlietBlack/FCC-Ziplines/master/Zipline-18/app/planets.csv"
df = pd.read_csv(data_url)

# Home route
@app.route('/')
def home():
    return render_template('explore.html')

# API route to get exoplanet data
@app.route('/api/exoplanets')
def get_exoplanets():
    # Simplify data for frontend usage (like names, mass, distance, radius, etc.)
    exoplanet_data = df[['Name', 'Mass', 'Distance', 'Radius']].dropna().to_dict(orient='records')
    return jsonify(exoplanet_data)

if __name__ == '__main__':
    app.run(debug=True)
