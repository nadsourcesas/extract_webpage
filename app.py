from distutils.log import debug
from fileinput import filename
import pandas as pd
from flask import *
import os
from werkzeug.utils import secure_filename
from string import Template
import random
import requests
ips={}
#UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads') /home/testi123/mysite/static
UPLOAD_FOLDER = "/home/testi123/mysite/static"            #os.path.join('mysite','static')

# Define allowed files
ALLOWED_EXTENSIONS = {'xlsx'}

app = Flask(__name__)
#@app.route("/getsql/<string:name>")
#def get(name):
#    t,d=name.split("é")
# Configure upload file path flask
dirr = UPLOAD_FOLDER

app.secret_key = 'This is your secret key to utilize session in Flask'

html=Template("""
<!DOCTYPE html>

<html><style> .button {   display: inline-block;   padding: 15px 25px;   font-size: 24px;   cursor: pointer;   text-align: center;   text-decoration: none;   outline: none;   color: #fff;   background-color: #4CAF50;   border: none;   border-radius: 15px;   box-shadow: 0 9px #999; }  .button:hover {background-color: #3e8e41}  .button:active {   background-color: #3e8e41;   box-shadow: 0 5px #666;   transform: translateY(4px); } </style>
<style>
html {
  text-align: center;
}
</style>
    <button  class="button" data-inline="true" style="height:200px;width:400px" onclick="window.location.href='https://testi123.pythonanywhere.com/ajouter_xlsx/$id';">
     ajouter_xlsx
    </button>
        <button  class="button" data-inline="true" style="height:200px;width:400px" onclick="window.location.href='https://testi123.pythonanywhere.com/remplacer_xlsx/$id';">
      remplacer_xlsx
    </button>
        <button  class="button" data-inline="true" style="height:200px;width:400px" onclick="window.location.href='https://testi123.pythonanywhere.com/lire_element/$id';">
      lire_element
    </button>
        <button  class="button" data-inline="true" style="height:200px;width:400px" onclick="window.location.href='https://testi123.pythonanywhere.com/afficher_xlsx/$id';">
     afficher_xlsx
    </button>
        </button>
        <button  class="button" data-inline="true" style="height:200px;width:400px" onclick="window.location.href='https://testi123.pythonanywhere.com/static/data$id.xlsx';">
     telecharger xlsx
    </button>
        <button  class="button" data-inline="true" style="height:200px;width:400px" onclick="window.location.href='https://testi123.pythonanywhere.com/clear/$id';">
     nouveau
    </button>
<body onload="clip_text">

<button type="button" id="bahae123" onClick = "clip_text()" >Generate text</button>
<button type="button" id="bahae321" onClick = "copier()" >Copy</button>

<button hidden type="button" id="bahae123"  >$text</button>
<p id="demo"></p>

 <script defer>
function clip_text(){
   try{

	document.getElementById("demo").innerHTML ="$text"
	} catch(err){
	  document.getElementById("demo").innerHTML = err.message;

	}
}
function copier(){
   try{
    var input = document.createElement('input')
    input.id="__copyText__";
    input.value = "$text"; // OOPS! ; générer le texte
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    input.remove()
	document.getElementById("bahae321").innerHTML ="Copied"
	} catch(err){
	  document.getElementById("demo").innerHTML = err.message;

	}
}
 //setTimeout( function(){clip_text (); }, 1000);

</script>
</body>
</html>
""")
html2=Template("""
<!DOCTYPE html>
<html><style> .button {   display: inline-block;   padding: 15px 25px;   font-size: 24px;   cursor: pointer;   text-align: center;   text-decoration: none;   outline: none;   color: #fff;   background-color: #4CAF50;   border: none;   border-radius: 15px;   box-shadow: 0 9px #999; }  .button:hover {background-color: #3e8e41}  .button:active {   background-color: #3e8e41;   box-shadow: 0 5px #666;   transform: translateY(4px); } </style>
<style>
html {
  text-align: center;
}
</style>
<body onload="clip_text">

<button type="button" id="bahae123" onClick = "clip_text()" >Generate the text</button>
<button type="button" id="bahae321" onClick = "copier()" >Copy</button>

<button hidden type="button" id="bahae123"  >$text</button>
<p id="demo"></p>

 <script defer>
function clip_text(){
   try{

	document.getElementById("demo").innerHTML ="$text"
	} catch(err){
	  document.getElementById("demo").innerHTML = err.message;

	}
}
function copier(){
   try{
    var input = document.createElement('input')
    input.id="__copyText__";
    input.value = "$text"; // OOPS! ;
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    input.remove()
	document.getElementById("bahae321").innerHTML ="Copied"//"Copié!"
	} catch(err){
	  document.getElementById("demo").innerHTML = err.message;

	}
}
 //setTimeout( function(){clip_text (); }, 1000);

</script>
</body>
</html>
""")
html3=Template("""
<!DOCTYPE html>
<html><style> .button {   display: inline-block;   padding: 15px 25px;   font-size: 24px;   cursor: pointer;   text-align: center;   text-decoration: none;   outline: none;   color: #fff;   background-color: #4CAF50;   border: none;   border-radius: 15px;   box-shadow: 0 9px #999; }  .button:hover {background-color: #3e8e41}  .button:active {   background-color: #3e8e41;   box-shadow: 0 5px #666;   transform: translateY(4px); } </style>
<style>
html {
  text-align: center;
}
</style>
<body onload="clip_text">

<button type="button" id="bahae321" onClick = "copier()" >Copy</button>

<button hidden type="button" id="bahae123"  >$text</button>
<p id="demo">$text</p>

 <script defer>

function copier(){
   try{
    var input = document.createElement('input')
    input.id="__copyText__";
    input.value = "$text"; // OOPS! ;
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    input.remove()
	document.getElementById("bahae321").innerHTML ="Copied"//"Copié!"
	} catch(err){
	  document.getElementById("demo").innerHTML = err.message;

	}
}
 //setTimeout( function(){clip_text (); }, 1000);

</script>
</body>
</html>
""")
@app.route('/<string:name>')
def home(name):
 if  name=="check":
     return"""
     <!DOCTYPE html>
<html><style> .button {   display: inline-block;   padding: 15px 25px;   font-size: 24px;   cursor: pointer;   text-align: center;   text-decoration: none;   outline: none;   color: #fff;   background-color: #4CAF50;   border: none;   border-radius: 15px;   box-shadow: 0 9px #999; }  .button:hover {background-color: #3e8e41}  .button:active {   background-color: #3e8e41;   box-shadow: 0 5px #666;   transform: translateY(4px); } </style>
<head>
<style>
.button {
  display: inline-block;
  padding: 15px 25px;
  font-size: 24px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  color: #fff;
  background-color: #4CAF50;
  border: none;
  border-radius: 15px;
  box-shadow: 0 9px #999;
}

.button:hover {background-color: #3e8e41}

.button:active {
  background-color: #3e8e41;
  box-shadow: 0 5px #666;
  transform: translateY(4px);
}
</style>
</head>
<body>


<button class="button" style="height:200px;width:400px" onclick="window.location.href='https://testi123.pythonanywhere.com/check/check'" >Analyser</button>
    <button class="button" style="height:200px;width:400px" data-inline="true" onclick="window.location.href='https://testi123.pythonanywhere.com/ajouter_xlsx/"""+name+"""';">
     ajouter_xlsx
    </button>
        <button class="button" style="height:200px;width:400px" data-inline="true" onclick="window.location.href='https://testi123.pythonanywhere.com/remplacer_xlsx/"""+name+"""';">
      remplacer_xlsx
    </button>
        <button class="button" style="height:200px;width:400px" data-inline="true" onclick="window.location.href='https://testi123.pythonanywhere.com/lire_element/"""+name+"""';">
      lire_element
    </button>
        <button class="button" style="height:200px;width:400px" data-inline="true" onclick="window.location.href='https://testi123.pythonanywhere.com/afficher_xlsx/"""+name+"""';">
     afficher_xlsx
    </button>
    </button>
        <button  class="button" data-inline="true" style="height:200px;width:400px" onclick="window.location.href='https://testi123.pythonanywhere.com/static/data"""+name+""".xlsx';">
     telecharger xlsx
    </button>
        </button>
        <button  class="button" data-inline="true" style="height:200px;width:400px" onclick="window.location.href='https://testi123.pythonanywhere.com/clear/data"""+name+"""';">
     nouveau
    </button>
</body>
</html>

     """
 else:
    return"""<!DOCTYPE html>
<html><style> .button {   display: inline-block;   padding: 15px 25px;   font-size: 24px;   cursor: pointer;   text-align: center;   text-decoration: none;   outline: none;   color: #fff;   background-color: #4CAF50;   border: none;   border-radius: 15px;   box-shadow: 0 9px #999; }  .button:hover {background-color: #3e8e41}  .button:active {   background-color: #3e8e41;   box-shadow: 0 5px #666;   transform: translateY(4px); } </style>
    <button class="button" style="height:200px;width:400px" data-inline="true" onclick="window.location.href='https://testi123.pythonanywhere.com/ajouter_xlsx/"""+name+"""';">
     ajouter_xlsx
    </button>
        <button class="button" style="height:200px;width:400px" data-inline="true" onclick="window.location.href='https://testi123.pythonanywhere.com/remplacer_xlsx/"""+name+"""';">
      remplacer_xlsx
    </button>
        <button class="button" style="height:200px;width:400px" data-inline="true" onclick="window.location.href='https://testi123.pythonanywhere.com/lire_element/"""+name+"""';">
      lire_element
    </button>
        <button class="button" style="height:200px;width:400px" data-inline="true" onclick="window.location.href='https://testi123.pythonanywhere.com/afficher_xlsx/"""+name+"""';">
     afficher_xlsx
    </button>
    </button>
        <button  class="button" data-inline="true" style="height:200px;width:400px" onclick="window.location.href='https://testi123.pythonanywhere.com/static/data"""+name+""".xlsx';">
     telecharger xlsx
    </button>
        </button>
        <button  class="button" data-inline="true" style="height:200px;width:400px" onclick="window.location.href='https://testi123.pythonanywhere.com/clear/data"""+name+"""';">
     nouveau
    </button>
<body >

</body>
</html>
"""
@app.route('/ajouter_xlsx/<string:name>', methods=['GET', 'POST'])
def uploadFile1(name):
    if request.method == 'POST':



        dfold = pd.read_excel(request.files.get('file'), skiprows=1)
        dfold.to_excel("/home/testi123/mysite/static/data"+name+".xlsx", mode='a',index=False)

        #session['uploaded_data_file_path'] =os.path.join(dirr,data_filename)

        return render_template('index2.html',page='ajouter_xlsx',idd=name)
    return render_template("index.html",page="ajouter_xlsx",idd=name)

@app.route('/remplacer_xlsx/<string:name>', methods=['GET', 'POST'])
def uploadFile2(name):
    if request.method == 'POST':
      # upload file flask
        f = request.files.get('file')

        # Extracting uploaded file name
        data_filename = secure_filename(f.filename)

        f.save("/home/testi123/mysite/static/data"+name+".xlsx")

        #session['uploaded_data_file_path'] =os.path.join(dirr,data_filename)

        return render_template('index2.html',page="remplacer_xlsx",idd=name)
    return render_template("index.html",page="remplacer_xlsx",idd=name)

@app.route('/lire_element/<string:name>', methods=['GET', 'POST'])
def reader(name):
    data_file_path ="/home/testi123/mysite/static/data"+name+".xlsx"# session.get('uploaded_data_file_path', None)
    # read xlsx
    data = pd.read_excel(data_file_path)
    ii=0
    while data.at[ii,'statut']==1:
        ii=ii+1
        if ii==data.shape[0]:
         return"""<!DOCTYPE html>
<html><style> .button {   display: inline-block;   padding: 15px 25px;   font-size: 24px;   cursor: pointer;   text-align: center;   text-decoration: none;   outline: none;   color: #fff;   background-color: #4CAF50;   border: none;   border-radius: 15px;   box-shadow: 0 9px #999; }  .button:hover {background-color: #3e8e41}  .button:active {   background-color: #3e8e41;   box-shadow: 0 5px #666;   transform: translateY(4px); } </style>

<h1></h1>

    <button data-inline="true" onclick="window.location.href='https://testi123.pythonanywhere.com/ajouter_xlsx/"""+name+"""';">
     ajouter_xlsx
    </button>
        <button data-inline="true" onclick="window.location.href='https://testi123.pythonanywhere.com/remplacer_xlsx/"""+name+"""';">
      remplacer_xlsx
    </button>
        <button data-inline="true" onclick="window.location.href='https://testi123.pythonanywhere.com/lire_element/"""+name+"""';">
      lire_element
    </button>
        <button data-inline="true" onclick="window.location.href='https://testi123.pythonanywhere.com/afficher_xlsx/"""+name+"""';">
     afficher_xlsx
    </button>
    </button>
        <button  class="button" data-inline="true" style="height:200px;width:400px" onclick="window.location.href='https://testi123.pythonanywhere.com/static/data"""+name+""".xlsx';">
     telecharger xlsx
    </button>
        </button>
        <button  class="button" data-inline="true" style="height:200px;width:400px" onclick="window.location.href='https://testi123.pythonanywhere.com/clear/"""+name+"""';">
     nouveau
    </button>
<body >

</body>
</html>
"""
    data.at[ii,'statut']=1
    data.to_excel("/home/testi123/mysite/static/data"+name+".xlsx",index=False)
    return html.safe_substitute(text=data.at[ii,'text'])

@app.route('/afficher_xlsx/<string:name>')
def showData(name):
    # Uploaded File Path
    data_file_path ="/home/testi123/mysite/static/data"+name+".xlsx"# session.get('uploaded_data_file_path', None)
    # read xlsx
    uploaded_df = pd.read_excel(data_file_path)
    # Converting to html Table
    uploaded_df_html = uploaded_df.to_html()
    return render_template('show_xlsx_data.html',
                           data_var=uploaded_df_html,idd=name)

@app.route('/check/check')
def check():

    data = pd.read_excel("/home/testi123/mysite/static/datacheck.xlsx")
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
     data2 = pd.read_excel("/home/testi123/mysite/static/data"+nm+".xlsx")
     rr=requests.get(data.at[jj,'url']).text
     while not ii==data2.shape[0]:
        ii=ii+1
        if ii==data2.shape[0]:
            break
        if data2.at[ii,'text'].replace("\n","#012") in rr.replace("\\n","#012").replace("\#012","#012"):
         data2.at[ii,'statut']=1
        else:
         data2.at[ii,'statut']=0

     data2.to_excel("/home/testi123/mysite/static/data"+nm+".xlsx",index=False)
    return "done"
@app.route('/bahae/bahae')
def client1():
    return requests.get("https://www.google.com/maps/place/Diateor,+44+Rue+de+la+Garenne,+35510+Cesson-S%C3%A9vign%C3%A9/@48.1209907,-1.6186527,17z/data=!4m6!3m5!1s0x480edecfab28c57b:0xd6a7c182273467f4!8m2!3d48.1209907!4d-1.6186527!16s%2Fg%2F11dyn9sjsw?hl=fr-FR&gl=fr").text
@app.route('/client/<string:name>')
def client(name):
    rr=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    found=False
    do=False

    for el in ips.keys():
      v= el.split("-")
    #  print("-----------------------v[0]",v[0],"==","rr",rr ,"v[-1]",v[-1],"name",name)
      if v[0]==rr and v[-1]==name:
          found=el

          break
    if found:
       return html3.safe_substitute(text=ips[found])
    else:
        do=True

    data_file_path ="/home/testi123/mysite/static/data"+name+".xlsx"# session.get('uploaded_data_file_path', None)
    # read xlsx
    data = pd.read_excel(data_file_path)
    ii=0
    while data.at[ii,'statut']==1:
        ii=ii+1
        if ii==data.shape[0]:
         return"""<!DOCTYPE html>
<html><style> .button {   display: inline-block;   padding: 15px 25px;   font-size: 24px;   cursor: pointer;   text-align: center;   text-decoration: none;   outline: none;   color: #fff;   background-color: #4CAF50;   border: none;   border-radius: 15px;   box-shadow: 0 9px #999; }  .button:hover {background-color: #3e8e41}  .button:active {   background-color: #3e8e41;   box-shadow: 0 5px #666;   transform: translateY(4px); } </style>

<h1></h1>


<body >

</body>
</html>
"""
    data.at[ii,'statut']=1
    if do:
         ips[rr+"-"+name]=data.at[ii,'text']
    data.to_excel("/home/testi123/mysite/static/data"+name+".xlsx",index=False)
    return html2.safe_substitute(text=data.at[ii,'text'])
@app.route('/ip/<string:name>')
def ip(name):
 return str(ips)+'#'+request.environ.get('HTTP_X_REAL_IP', request.remote_addr)



@app.route('/smiley')
def smiley():
 return """
 😀😁😂😃😄😅😆😉😊😋😎😍😘😗😙😚🙂🤗🤔😐😑😶🙄😏😣😥😮🤐😯😪😫😴😌😛😜😝😒😓😔😕🙃🤑😲☹🙁😖😞😟😤😢😭😦😧😨😩😬😰😱😳😵😡😠😷🤒🤕😇🤓😈👿👹👺💀☠👻👽👾🤖💩😺😸😹😻😼😽🙀😿😾🙈🙉🙊👶👧👦👩👨👵👴👲👳‍♀️👳‍♂️👮‍♀️👮‍♂️👷‍♀️👷‍♂️💂‍♀️💂‍♂️🕵️‍♀️🕵️‍♂️👩‍⚕️👨‍⚕️👩‍🌾👨‍🌾👩‍🍳👨‍🍳👩‍🎓👨‍🎓👩‍🎤👨‍🎤👩‍🏫👨‍🏫👩‍🏭👨‍🏭👩‍💻👨‍💻👩‍💼👨‍💼👩‍🔧👨‍🔧👩‍🔬👨‍🔬👩‍🎨👨‍🎨👩‍🚒👨‍🚒👩‍✈️👨‍✈️👩‍🚀👨‍🚀👩‍⚖️👨‍⚖️👰👸🎅‍♀️‍♂️‍♀️‍♂️‍♀️‍♂️‍♀️‍♂️‍♀️‍♂️‍♀️‍♂️‍♀️‍♂️👼🙇‍♀️🙇‍♂️💁‍♀️💁‍♂️🙅‍♀️🙅‍♂️🙆‍♀️🙆‍♂️🙋‍♀️🙋‍♂️‍♀️‍♂️‍♀️‍♂️🙎‍♀️🙎‍♂️🙍‍♀️🙍‍♂️💇‍♀️💇‍♂️💆‍♀️💆‍♂️‍♀️‍♂️💅💃👯‍♀️👯‍♂️🕴🚶‍♀️🚶‍♂️👫👭👬💑👩‍❤️‍👩👨‍❤️‍👨💏👩‍❤️‍💋‍👩👨‍❤️‍💋‍👨👪👨‍👩‍👧👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧👩‍👩‍👦👩‍👩‍👧👩‍👩‍👧‍👦👩‍👩‍👦‍👦👩‍👩‍👧‍👧👨‍👨‍👦👨‍👨‍👧👨‍👨‍👧‍👦👨‍👨‍👦‍👦👨‍👨‍👧‍👧👩‍👦👩‍👧👩‍👧‍👦👩‍👦‍👦👩‍👧‍👧👨‍👦👨‍👧👨‍👧‍👦👨‍👦‍👦👨‍👧‍👧🗣👤👥💪👈👉☝👆🖕👇✌🖖🤘🖐✋👌👍👎✊👊👋✍👏👐🙌🙏💅👂👃👣👀👁👁️‍🗨️👅👄💋💘💝💖💗💓💞💕💌❣💔❤💛💚💙💜💟💤💢💣💥💦💨💫💬🗨🗯💭🕳👓🕶👔👕👖👗👘👙👚👛👜👝🛍🎒👞👟👠👡👢👑👒🎩🎓⛑📿💄💍💎
⚽️ 🏀 🏈 ⚾️ 🎾 🏐 🏉 🎱 🏓 🏸 🏒 🏑 🏏 ⛳️ 🏹 🎣 🎽 ⛸ 🎿 ⛷ 🏂 🏋️‍♀️ 🏋🏻‍♀️ 🏋🏼‍♀️ 🏋🏽‍♀️ 🏋🏾‍♀️ 🏋🏿‍♀️ 🏋️‍♂️ 🏋🏻‍♂️ 🏋🏼‍♂️ 🏋🏽‍♂️ 🏋🏾‍♂️ 🏋🏿‍♂️ ‍♀️ ‍♂️ ‍♀️ 🏻‍♀️ 🏼‍♀️ 🏽‍♀️ 🏾‍♀️ 🏿‍♀️ ‍♂️ 🏻‍♂️ 🏼‍♂️ 🏽‍♂️ 🏾‍♂️ 🏿‍♂️ ⛹️‍♀️ ⛹🏻‍♀️ ⛹🏼‍♀️ ⛹🏽‍♀️ ⛹🏾‍♀️ ⛹🏿‍♀️ ⛹️‍♂️ ⛹🏻‍♂️ ⛹🏼‍♂️ ⛹🏽‍♂️ ⛹🏾‍♂️ ⛹🏿‍♂️ ‍♀️ 🏻‍♀️ 🏼‍♀️ 🏾‍♀️ 🏾‍♀️ 🏿‍♀️ ‍♂️ 🏻‍♂️ 🏼‍♂️ 🏽‍♂️ 🏾‍♂️ 🏿‍♂️ 🏌️‍♀️ 🏌🏻‍♀️ 🏌🏼‍♀️ 🏌🏽‍♀️ 🏌🏾‍♀️ 🏌🏿‍♀️ 🏌️‍♂️ 🏌🏻‍♂️ 🏌🏼‍♂️ 🏌🏽‍♂️ 🏌🏾‍♂️ 🏌🏿‍♂️ 🏇 🏇🏻 🏇🏼 🏇🏽 🏇🏾 🏇🏿 ‍♀️ 🏻‍♀️ 🏼‍♀️ 🏽‍♀️ 🏾‍♀️ 🏿‍♀️ ‍♂️ 🏻‍♂️ 🏼‍♂️ 🏽‍♂️ 🏾‍♂️ 🏿‍♂️ 🏄‍♀️ 🏄🏻‍♀️ 🏄🏼‍♀️ 🏄🏽‍♀️ 🏄🏾‍♀️ 🏄🏿‍♀️ 🏄‍♂️ 🏄🏻‍♂️ 🏄🏼‍♂️ 🏄🏽‍♂️ 🏄🏾‍♂️ 🏄🏿‍♂️ 🏊‍♀️ 🏊🏻‍♀️ 🏊🏼‍♀️ 🏊🏽‍♀️ 🏊🏾‍♀️ 🏊🏿‍♀️ 🏊‍♂️ 🏊🏻‍♂️ 🏊🏼‍♂️ 🏊🏽‍♂️ 🏊🏾‍♂️ 🏊🏿‍♂️ ‍♀️ 🏻‍♀️ 🏼‍♀️ 🏽‍♀️ 🏾‍♀️ 🏿‍♀️ ‍♂️ 🏻‍♂️ 🏼‍♂️ 🏽‍♂️ 🏾‍♂️ 🏿‍♂️ 🚣‍♀️ 🚣🏻‍♀️ 🚣🏼‍♀️ 🚣🏽‍♀️ 🚣🏾‍♀️ 🚣🏿‍♀️ 🚣‍♂️ 🚣🏻‍♂️ 🚣🏼‍♂️ 🚣🏽‍♂️ 🚣🏾‍♂️ 🚣🏿‍♂️ ‍♀️ 🏻‍♀️ 🏼‍♀️ 🏽‍♀️ 🏾‍♀️ 🏿‍♀️ ‍♂️ 🏻‍♂️ 🏼‍♂️ 🏽‍♂️ 🏾‍♂️ 🏿‍♂️ 🚵‍♀️ 🚵🏻‍♀️ 🚵🏼‍♀️ 🚵🏽‍♀️ 🚵🏾‍♀️ 🚵🏿‍♀️ 🚵‍♂️ 🚵🏻‍♂️ 🚵🏼‍♂️ 🚵🏽‍♂️ 🚵🏾‍♂️ 🚵🏿‍♂️ 🚴‍♀️ 🚴🏻‍♀️ 🚴🏼‍♀️ 🚴🏽‍♀️ 🚴🏾‍♀️ 🚴🏿‍♀️ 🚴‍♂️ 🚴🏻‍♂️ 🚴🏼‍♂️ 🚴🏽‍♂️ 🚴🏾‍♂️ 🚴🏿‍♂️ 🏆 🏅 🎖 🏵 🎗 🎫 🎟 🎪 ‍♀️ 🏻‍♀️ 🏼‍♀️ 🏽‍♀️ 🏾‍♀️ 🏿‍♀️ ‍♂️ 🏻‍♂️ 🏼‍♂️ 🏽‍♂️ 🏾‍♂️ 🏿‍♂️ 🎭 🎨 🎬 🎤 🎧 🎼 🎹 🎷 🎺 🎸 🎻 🎲 🎯 🎳 🎮 🎰🐶🐱🐭🐹🐰🐻🐼🐨🐯🦁🐮🐷🐽🐸🐵🙈🙉🙊🐒🐔🐧🐦🐤🐣🐥🐺🐗🐴🦄🐝🐛🐌🐚🐞🐜🕷🕸🦂🐢🐍🐙🦀🐡🐠🐟🐬🐳🐋🐊🐅🐆🐘🐪🐫🐃🐂🐄🐎🐖🐏🐑🐐🐕🐩🐈🐓🦃🕊🐇🐁🐀🐿🐾🐉🐲🌵🎄🌲🌳🌴🌱🌿☘️🍀🎍🎋🍃🍂🍁🍄🌾💐🌷🌹🌺🌸🌼🌻🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒🍑🍍🍅🍆🌶🌽🍠🍞🧀🍳🍗🍖🌭🍔🍟🍕🌮🌯🍝🍜🍲🍛🍣🍱🍤🍙🍚🍘🍥🍢🍡🍧🍨🍦🍰🎂🍮🍭🍬🍫🍿🍩🍪🌰🍯🍼☕️🍵🍶🍺🍻🍷🍸🍹🍾🍴🍽🌍🌎🌏🌐🗺🗾🏔⛰🌋🗻🏕🏖🏜🏝🏞🏟🏛🏗🏘🏚🏠🏡🏢🏣🏤🏥🏦🏨🏩🏪🏫🏬🏭🏯🏰💒🗼🗽⛪🕌🕍⛩🕋⛲⛺🌁🌃🏙🌄🌅🌆🌇🌉♨🌌🎠🎡🎢💈🎪🚂🚃🚄🚅🚆🚇🚈🚉🚊🚝🚞🚋🚌🚍🚎🚐🚑🚒🚓🚔🚕🚖🚗🚘🚙🚚🚛🚜🚲🚏🛣🛤🛢⛽🚨🚥🚦🚧⚓⛵🚤🛳⛴🛥🚢✈🛩🛫🛬💺🚁🚟🚠🚡🛰🚀🌑🌒🌓🌔🌕🌖🌗🌘🌙🌚🌛🌜🌡☀🌝🌞⭐🌟🌠☁⛅⛈🌤🌥🌦🌧🌨🌩🌪🌫🌬🌀🌈🌂☂☔⛱⚡❄☃⛄☄🔥💧🌊⌚️📱📲💻⌨️🖥🖨🖱🖲🕹🗜💽💾💿📀📼📷📸📹🎥📽🎞📞☎️📟📠📺📻🎙🎚🎛⏱⏲⏰🕰⌛️⏳📡🔋🔌💡🔦🕯🗑🛢💸💵💴💶💷💰💳💎⚖️🔧🔨⚒🛠⛏🔩⚙️⛓🔫💣🔪🗡⚔️🛡🚬⚰️⚱️🏺🔮📿💈⚗️🔭🔬🕳💊💉🌡🚽🚰🚿🛁🛀🛀🏻🛀🏼🛀🏽🛀🏾🛀🏿🛎🔑🗝🚪🛋🛏🛌🖼🛍🎁🎈🎏🎀🎊🎉🎎🏮🎐✉️📩📨📧💌📥📤📦🏷📪📫📬📭📮📯📜📃📄📑📊📈📉🗒🗓📆📅📇🗃🗳🗄📋📁📂🗂🗞📰📓📔📒📕📗📘📙📚📖🔖🔗📎🖇📐📏📌📍✂️🖊🖋✒️🖌🖍📝✏️🔍🔎🔏🔐🔒🔓☮️✝️☪️🕉☸️✡️🔯🕎☯️☦️🛐⛎♈️♉️♊️♋️♌️♍️♎️♏️♐️♑️♒️♓️🆔⚛️🉑☢️☣️📴📳🈶🈚️🈸🈺🈷️✴️🆚💮🉐㊙️㊗️🈴🈵🈹🈲🅰️🅱️🆎🆑🅾️🆘❌⭕️⛔️📛🚫💯💢♨️🚷🚯🚳🚱🔞📵🚭❗️❕❓❔‼️⁉️🔅🔆〽️⚠️🚸🔱⚜️🔰♻️✅🈯️💹❇️✳️❎🌐💠Ⓜ️🌀💤🏧🚾♿️🅿️🈳🈂️🛂🛃🛄🛅🚹🚺🚼🚻🚮🎦📶🈁🔣ℹ️🔤🔡🔠🆖🆗🆙🆒🆕🆓0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟🔢#️⃣*️⃣⏏️▶️⏸⏯⏹⏺⏭⏮⏩⏪⏫⏬◀️🔼🔽➡️⬅️⬆️⬇️↗️↘️↙️↖️↕️↔️↪️↩️⤴️⤵️🔀🔁🔂🔄🔃🎵🎶➕➖➗✖️💲💱™️©️®️〰️➰➿🔚🔙🔛🔝🔜✔️☑️🔘⚪️⚫️🔴🔵🔺🔻🔸🔹🔶🔷🔳🔲▪️▫️◾️◽️◼️◻️⬛️⬜️🔈🔇🔉🔊🔔🔕📣📢👁‍🗨💬💭🗯♠️♣️♥️♦️🃏🎴🀄️🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛🕜🕝🕞🕟🕠🕡🕢🕣🕤🕥🕦🕧🏳️ 🏴 🏁 🚩 🏳️‍🌈 🇦🇫 🇦🇽 🇦🇱 🇩🇿 🇦🇸 🇦🇩 🇦🇴 🇦🇮 🇦🇶 🇦🇬 🇦🇷 🇦🇲 🇦🇼 🇦🇺 🇦🇹 🇦🇿 🇧🇸 🇧🇭 🇧🇩 🇧🇧 🇧🇾 🇧🇪 🇧🇿 🇧🇯 🇧🇲 🇧🇹 🇧🇴 🇧🇦 🇧🇼 🇧🇷 🇮🇴 🇻🇬 🇧🇳 🇧🇬 🇧🇫 🇧🇮 🇰🇭 🇨🇲 🇨🇦 🇮🇨 🇨🇻 🇧🇶 🇰🇾 🇨🇫 🇹🇩 🇨🇱 🇨🇳 🇨🇽 🇨🇨 🇨🇴 🇰🇲 🇨🇬 🇨🇩 🇨🇰 🇨🇷 🇨🇮 🇭🇷 🇨🇺 🇨🇼 🇨🇾 🇨🇿 🇩🇰 🇩🇯 🇩🇲 🇩🇴 🇪🇨 🇪🇬 🇸🇻 🇬🇶 🇪🇷 🇪🇪 🇪🇹 🇪🇺 🇫🇰 🇫🇴 🇫🇯 🇫🇮 🇫🇷 🇬🇫 🇵🇫 🇹🇫 🇬🇦 🇬🇲 🇬🇪 🇩🇪 🇬🇭 🇬🇮 🇬🇷 🇬🇱 🇬🇩 🇬🇵 🇬🇺 🇬🇹 🇬🇬 🇬🇳 🇬🇼 🇬🇾 🇭🇹 🇭🇳 🇭🇰 🇭🇺 🇮🇸 🇮🇳 🇮🇩 🇮🇷 🇮🇶 🇮🇪 🇮🇲 🇮🇱 🇮🇹 🇯🇲 🇯🇵 🎌 🇯🇪 🇯🇴 🇰🇿 🇰🇪 🇰🇮 🇽🇰 🇰🇼 🇰🇬 🇱🇦 🇱🇻 🇱🇧 🇱🇸 🇱🇷 🇱🇾 🇱🇮 🇱🇹 🇱🇺 🇲🇴 🇲🇰 🇲🇬 🇲🇼 🇲🇾 🇲🇻 🇲🇱 🇲🇹 🇲🇭 🇲🇶 🇲🇷 🇲🇺 🇾🇹 🇲🇽 🇫🇲 🇲🇩 🇲🇨 🇲🇳 🇲🇪 🇲🇸 🇲🇦 🇲🇿 🇲🇲 🇳🇦 🇳🇷 🇳🇵 🇳🇱 🇳🇨 🇳🇿 🇳🇮 🇳🇪 🇳🇬 🇳🇺 🇳🇫 🇰🇵 🇲🇵 🇳🇴 🇴🇲 🇵🇰 🇵🇼 🇵🇸 🇵🇦 🇵🇬 🇵🇾 🇵🇪 🇵🇭 🇵🇳 🇵🇱 🇵🇹 🇵🇷 🇶🇦 🇷🇪 🇷🇴 🇷🇺 🇷🇼 🇼🇸 🇸🇲 🇸🇦 🇸🇳 🇷🇸 🇸🇨 🇸🇱 🇸🇬 🇸🇽 🇸🇰 🇸🇮 🇬🇸 🇸🇧 🇸🇴 🇿🇦 🇰🇷 🇸🇸 🇪🇸 🇱🇰 🇧🇱 🇸🇭 🇰🇳 🇱🇨 🇵🇲 🇻🇨 🇸🇩 🇸🇷 🇸🇿 🇸🇪 🇨🇭 🇸🇾 🇹🇼 🇹🇯 🇹🇿 🇹🇭 🇹🇱 🇹🇬 🇹🇰 🇹🇴 🇹🇹 🇹🇳 🇹🇷 🇹🇲 🇹🇨 🇹🇻 🇻🇮 🇺🇬 🇺🇦 🇦🇪 🇬🇧 🏴 🏴 🏴 🇺🇸 🇺🇾 🇺🇿 🇻🇺 🇻🇦 🇻🇪 🇻🇳 🇼🇫 🇪🇭 🇾🇪 🇿🇲 🇿🇼
 """
@app.route('/clear/<string:name>')
def cleardata(name):
 return "tous les clients pourront de nouveau generer un nouveau text"
