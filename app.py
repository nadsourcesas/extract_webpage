from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return requests.get('https://cima4u1.autos/').text
