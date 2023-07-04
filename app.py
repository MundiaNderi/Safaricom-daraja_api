from flask import Flask
from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

# mpesa details
load_dotenv()
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']

# Home route and method


@app.route('/')
def home():
    return 'Hello World'


# access token


@app.route('/access_token')
def token():
    data = ac_token()
    return data


def ac_token():
    mpesa_auth_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    data = (requests.get(mpesa_auth_url, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))).json()
    return data['access_token']


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3400, debug=True)
