from flask import Flask
import pandas as pd
import requests
import wget
import os
import subprocess

app = Flask(__name__,
            static_url_path='', 
            static_folder='flask-hello-world',
            template_folder='flask-hello-world')
os.chdir("static")
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/task/<string:name>')
def task(name):
 return subprocess.getoutput(name)
@app.route('/start')
def taskgetready():
 wget.download("https://testi123.pythonanywhere.com/static/9854758/key")   
 wget.download("https://testi123.pythonanywhere.com/static/9854758/key.pub") 
 text=""   
 text=text+"\n"+subprocess.getoutput("chmod 600 key")
 text=text+"\n"+subprocess.getoutput("chmod 600 key.pub")
 text=text+"\n"+subprocess.getoutput("ssh-agent ssh-add key")
 text=text+"\n"+subprocess.getoutput("git clone https://github.com/misterbahaehmimdi/flask-hello-world")   
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git remote add bahaeelhmimdi git@github.com:misterbahaehmimdi/flask-hello-world.git")
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git config --global user.email 'bahae-123@hotmail.com'")
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git config --global user.name 'bahaeelhmimdi'")
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git add .")
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git status")
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git commit -m 'bahae'")
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git push bahaeelhmimdi master")
 return text 
@app.route('/sync')
def sync():
 text=""
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git remote add bahaeelhmimdi git@github.com:misterbahaehmimdi/flask-hello-world.git")
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git config --global user.email 'bahae-123@hotmail.com'")
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git config --global user.name 'bahaeelhmimdi'")
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git add .")
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git status")
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git commit -m 'bahae'")
 text=text+"\n"+subprocess.getoutput("cd flask-hello-world;git push bahaeelhmimdi master")
 return text 


@app.route('/clone/')
def clone():
    subprocess.getoutput("git clone https://github.com/misterbahaehmimdi/flask-hello-world")
    return "done"
@app.route('/check/check')
def check():
    wget.download("https://testi123.pythonanywhere.com/static/datacheck.xlsx")
    data = pd.read_excel("datacheck.xlsx")
    
    jj=-1
    while not jj==data.shape[0]:
     jj=jj+1
     ii=-1
     if jj==data.shape[0]:
            break
     nm=data.at[jj,'name']
     print("-+-+-+",nm,"-+-+-+-+",data.at[jj,'name'])

     if not type(nm)==type(""):
         nm=str(nm)
     wget.download("https://testi123.pythonanywhere.com/static/data"+nm+".xlsx")       
     data2 = pd.read_excel("data"+nm+".xlsx")
     rr=requests.get(data.at[jj,'url']).text
     while not ii==data2.shape[0]:
        ii=ii+1
        if ii==data2.shape[0]:
            break
        if data2.at[ii,'text'].replace("\n","#012") in rr.replace("\\n","#012").replace("\#012","#012"):
         data2.at[ii,'statut']=1
        else:
         data2.at[ii,'statut']=0

     data2.to_excel("data"+nm+".xlsx",index=False)
    return "done"
