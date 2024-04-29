from flask import Flask, jsonify,request
import pandas as pd
import requests
import wget
import os
import subprocess 
from bs4 import BeautifulSoup

app = Flask(__name__)
os.chdir("static")
@app.route('/index')
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
                return  jsonify({'status': 'success','lasturl':str(response.history[-1].url),'prefix':prefix, 'data': BeautifulSoup(response.text).get_text()})

        except Exception as e:#requests.RequestException
            print(f"Error occurred while trying {prefix + url}: {e}")
    
    return jsonify({'status': 'failed','lasturl':'', 'data': '','prefix':''})
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


@app.errorhandler(404)
def tasktest(name):
 return get_html_text(request.url.replace(r"https://test2-bblm.onrender.com/",""))
