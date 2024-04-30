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
def scrape_headings_from_html(soup):
    # Parse the HTML content
    
    # Find all heading tags (h1, h2, h3, h4, h5, h6)
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    # Initialize a dictionary to store headings
    headings_dict = {}
    
    # Loop through the heading tags
    for heading in headings:
        # Get the tag name (e.g., 'h1', 'h2', etc.)
        tag_name = heading.name
        
        # Get the text of the heading
        heading_text = heading.get_text().strip()
        
        # Get the numerical order of the heading
        order = len(headings_dict.get(tag_name, [])) + 1
        
        # Add the heading text to the dictionary
        if tag_name not in headings_dict:
            headings_dict[tag_name] = {}
        headings_dict[tag_name][order] = heading_text
    
    return headings_dict    
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
                soup=BeautifulSoup(response.text)
                fj={'status': 'success','final':str(response.url),'tst':str(tst),'testedurl':testedurl,'lasturl':str(list(map(lambda a:a.url,response.history))),'prefix':prefix, 'data': soup.get_text()}
                fj.update(scrape_headings_from_html(soup))
                
                return  jsonify(fj)

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
