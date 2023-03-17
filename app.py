import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# API endpoint for retrieving population data
@app.route('/api/population')
def get_population():
    region = request.args.get('region')
    response = requests.get(f"https://ghsl.jrc.ec.europa.eu/population-api/v1.0/population?country=auto&region={region}&resolution=250")
    data = response.json()['data'][0]['population']
    return jsonify({'region': region, 'population': data})

if __name__ == '__main__':
    app.run(debug=True)
