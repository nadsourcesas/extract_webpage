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
   tst= []
   ers= []
   try: 
    prefixes = [ 'https://','http://','https://www.',  'http://www.']
    if "//" in url :   
        prefixes=['']
    for prefix in prefixes:
        
        try:
            if "//" in url :
                testedurl= url
                
            else: 
                testedurl = prefix + url
                
            tst.append(testedurl)  
            print("-----------------",tst)
            response = requests.get(testedurl, allow_redirects=True)
           
            if response.status_code == 200:
                return  jsonify({'status': 'success','final':str(response.url),'tst':str(tst),'testedurl':testedurl,'lasturl':str(list(map(lambda a:a.url,response.history))),'prefix':prefix, 'data': BeautifulSoup(response.text).get_text()})

        except Exception as e:#requests.RequestException
            print(f"Error occurred while trying {prefix + url}: {e}")
            ers.append(e)
    return jsonify({'status': 'failed','ers':str(ers),'tst':str(tst),'lasturl':'', 'data': '','prefix':'','testedurl':testedurl})
   except Exception as problem:
           return jsonify({'status': 'failed','tst':str(tst),"error":str(problem),'lasturl':'', 'data': '','prefix':'','testedurl':testedurl})

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
