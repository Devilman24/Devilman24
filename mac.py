from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_mac_vendor(mac_address):
    url = f"https://api.macvendors.com/{mac_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Constructeur inconnu"

@app.route('/api/lookup', methods=['POST'])
def lookup():
    data = request.get_json()
    mac_address = data.get('mac_address')
    vendor = get_mac_vendor(mac_address)
    return jsonify({'mac_address': mac_address, 'vendor': vendor})

if __name__ == '__main__':
    app.run(debug=True)
