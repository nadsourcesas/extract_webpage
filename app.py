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
    prefixes = ['https://', 'http://', 'https://www.', 'http://www.']
    for prefix in prefixes:
        if prefix in url:
            prefixes.remove(prefix)
            prefixes=[prefix]+prefixes
    for prefix in prefixes:
        
        try:
            if prefix in url :
                response = requests.get( url) 
            else:    
               response = requests.get(prefix + url) 
           
            if response.status_code == 200:
                return  jsonify({'status': 'success',lasturl:str(response.history[-1].url),'prefix':prefix, 'data': BeautifulSoup(response.text).get_text()})

        except Exception as e:#requests.RequestException
            print(f"Error occurred while trying {prefix + url}: {e}")
    
    return jsonify({'status': 'failed',lasturl:'', 'data': '','prefix':''})
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
@app.route(r'/task/(?P<name>.+)', strict_slashes=False)
def task(name):
 return get_html_text(name)
