from flask import Flask, request, jsonify
from flask_cors import CORS
from data import countries
from phoneNumbers import phonennnumbers

app = Flask(__name__)
CORS(app)

@app.route('/api/countries', methods=['GET'])
def get_countries():
    search_query = request.args.get('search', '').lower()
    filtered_countries = [country for country in countries if search_query in country.lower()]
    return jsonify(filtered_countries)

@app.route('/api/phoneNumbers', methods=['GET'])
def get_phone_numbers():
    name = request.args.get('name', '')
    return jsonify(phonennnumbers.get(name, {'phones': [], 'emails': []}))

if __name__ == '__main__':
    app.run(port=5500, debug=True)
