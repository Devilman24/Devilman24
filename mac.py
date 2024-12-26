from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def get_mac_vendor(mac_address):
    url = f"https://api.macvendors.com/{mac_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Constructeur inconnu"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    mac_address = request.form['mac_address']
    vendor = get_mac_vendor(mac_address)
    return render_template('result.html', mac_address=mac_address, vendor=vendor)

if __name__ == '__main__':
    app.run(debug=True)
