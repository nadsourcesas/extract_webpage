from flask import Flask
import pandas as pd
import requests
import wget
import os
import subprocess 

app = Flask(__name__)
os.chdir("static")
@app.route('/')
def hello_world():
    return subprocess.getoutput("ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts")


@app.route('/task/<string:name>')
def task(name):
 return subprocess.getoutput(name)
@app.route('/start')
def taskgetready():
 wget.download("https://testi123.pythonanywhere.com/static/9854758/key")   
 wget.download("https://testi123.pythonanywhere.com/static/9854758/key.pub") 
 text=""   
 text=text+"<br>"+subprocess.getoutput("chmod 600 key")
 text=text+"<br>"+subprocess.getoutput("chmod 600 key.pub")
 text=text+"<br>"+subprocess.getoutput("ssh-agent ssh-add key")
 text=text+"<br>"+subprocess.getoutput("git clone https://github.com/misterbahaehmimdi/flask-hello-world")   

 text=text+"<br>"+subprocess.getoutput("git config --global user.signingkey key.pub")

 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git remote add bahaeelhmimdi git@github.com:misterbahaehmimdi/flask-hello-world.git")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git remote set-url bahaeelhmimdi git@github.com:misterbahaehmimdi/flask-hello-world.git")


 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git config --global user.email 'bahae-123@hotmail.com'")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git config --global user.name 'misterbahaehmimdi'")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git add .")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git status")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git commit -m 'bahae'")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git push origin master")
 return text 
@app.route('/sync')
def sync():
 text=""
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git remote add bahaeelhmimdi git@github.com:misterbahaehmimdi/flask-hello-world.git")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git remote set-url bahaeelhmimdi git@github.com:misterbahaehmimdi/flask-hello-world.git")
    
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git config --global user.email 'bahae-123@hotmail.com'")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git config --global user.name 'bahaeelhmimdi'")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git add .")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git status")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git commit -m 'bahae'")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git push bahaeelhmimdi master")
 return text 

erros=[]
@app.route('/clone/')
def clone():
    subprocess.getoutput("git clone https://github.com/misterbahaehmimdi/flask-hello-world")
    return "done"
@app.route('/eros/')
def err():
    return str(erros)
@app.route('/check/check')
def check():
    lis=[]
    wget.download("https://testi123.pythonanywhere.com/static/datacheck.xlsx")
    data = pd.read_excel("datacheck.xlsx")
    al=list(data.iterrows())
    lal=len(al)
    for index2,d1 in al[int(lal/2):int(lal*(3/4))]:
     try:
      nm=d1['name']
      print("-+-+-+",nm,"-+-+-+-+",d1['name']) 

      if not type(nm)==type(""):
         nm=str(nm)
      wget.download("https://testi123.pythonanywhere.com/static/data"+nm+".xlsx")       
      data2 = pd.read_excel("data"+nm+".xlsx")
      
       
      rr=requests.get(d1['url']).text
     
      for index2,d2 in data2.iterrows():
       try: 
        if not type(d2['text'])==type(""):
            continue
        if d2['text'].replace("\n","#012") in rr.replace("\\n","#012").replace("\#012","#012"):
         d2['statut']=1
        else:
         d2['statut']=0
        
       except Exception as eror:
        lis.append({"name":nm,"url":d1['url'],"text":d2['text'],"error":str(eror)})
        print("----",lis)
      data2.to_excel("data"+nm+".xlsx",index=False) 
      if True:   
       
       url = 'https://testi123.pythonanywhere.com/remplacer_xlsx/'+nm
       files = {'file': open('data'+nm+'.xlsx', 'rb')}

       r = requests.post(url, files=files)
       del data2 
     except Exception as first:
                lis.append({"url":d1['url'],"name":d1['name']   })
                print("++++",lis)
     erros.append(lis)
    return "done"
