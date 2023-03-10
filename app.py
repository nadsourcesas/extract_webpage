from flask import Flask
import requets
app = Flask(__name__)

@app.route('/')
def hello_world():
    return requests.get('https://cima4u1.autos/').text
