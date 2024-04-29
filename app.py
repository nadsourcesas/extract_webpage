from flask import Flask, jsonify
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
   try: 
    prefixes = ['http://', 'https://', 'http://www.', 'https://www.']
    
    for prefix in prefixes:
        try:
            response = requests.get(prefix + url[1:-1])
            if response.status_code == 200:
                return  jsonify({'status': 'success','prefix':prefix, 'data': BeautifulSoup(response.text).get_text()})

        except Exception as e:#requests.RequestException
            print(f"Error occurred while trying {prefix + url}: {e}")
    
    return jsonify({'status': 'failed', 'data': '','prefix':''})
   except Exception as problem:
       return str(problem)
def get_html(url):
    prefixes = ['http://', 'https://', 'http://www.', 'https://www.']
    
    for prefix in prefixes:
        try:
            response = requests.get(prefix + url)
            if response.status_code == 200:
                return response.text
        except Exception as e:#requests.RequestException
            print(f"Error occurred while trying {prefix + url}: {e}")
    
    return "nothing worked"
@app.route('/taskhtml/<string:name>')
def taskhtml(name):
 return get_html(name)
@app.route('/task/<string:name>')
def task(name):
 return get_html_text(name)
