from flask import Flask
import pandas as pd
import requests
import wget
import os
import subprocess 
from bs4 import BeautifulSoup

app = Flask(__name__)
os.chdir("static")
@app.route('/')
def hello_world():
    return "hello in bahae api"
def get_html_text(url):
    prefixes = ['http://', 'https://', 'http://www.', 'https://www.']
    
    for prefix in prefixes:
        try:
            response = requests.get(prefix + url,timeout=10)
            if response.status_code == 200:
                return BeautifulSoup(response.text).get_text()
        except Exception as e:#requests.RequestException
            print(f"Error occurred while trying {prefix + url}: {e}")
    
    return "nothing worked"
def get_html(url):
    prefixes = ['http://', 'https://', 'http://www.', 'https://www.']
    
    for prefix in prefixes:
        try:
            response = requests.get(prefix + url,timeout=10)
            if response.status_code == 200:
                return response.text
        except Exception as e:#requests.RequestException
            print(f"Error occurred while trying {prefix + url}: {e}")
    
    return "nothing worked"
@app.route('/taskhtml/<string:name>')
def taskhtml(name):
 return get_html_text(name)
