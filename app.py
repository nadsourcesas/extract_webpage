from flask import Flask, jsonify,request
import pandas as pd
import requests
import wget
import os
import subprocess 
from bs4 import BeautifulSoup
import roman
app = Flask(__name__)
os.chdir("static")
@app.route('/index')
def hello_world():
    return "hello in bahae api"
def extract_titles(soup):
    """Extrait tous les titres h1, h2, h3, h4 de la soupe donnée."""
    titles = []
    for level in range(1, 5):
        for tag in soup.find_all(f'h{level}'):
            titles.append((level, tag.text))
    return titles

def create_table_of_contents(soup):
    # Initialize the table of contents list
    table_of_contents = []
    tag_names = ["h1", "h2", "h3", "h4", "h5"]
    indices = [0] * len(tag_names)

    # Loop through each tag name
    for index, tag_name in enumerate(tag_names):
        # Find all occurrences of the tag in the soup
        tags = soup.find_all(tag_name)

        # Loop through each found tag
        for tag in tags:
            # Get the content of the tag
            content = tag.get_text().strip()

            # Find the position of the tag content in the entire HTML content
            position = soup.get_text().find(content)

            # Set the index for the current level of hierarchy
            indices[index] += 1

            # Create the index string for the current tag
            if index == 1:
                index_str = chr(96 + indices[1])
            elif index >= 3:
                index_str = roman.toRoman(indices[index])
            else:
                index_str = str(indices[index])

            # Create a dictionary to store the tag information
            tag_info = {
                "tag_name": tag_name,
                "index": index_str,
                "position": position,
                "content": content
            }

            # Append the tag information to the table of contents list
            table_of_contents.append(tag_info)

            # Reset indices for lower levels of hierarchy
            for j in range(index + 1, len(indices)):
                indices[j] = 0

    return sorted(table_of_contents, key=lambda x: x['position'])
def tbl(soup):
 rt= {}  
# Create the table of contents
 table_of_contents = create_table_of_contents(soup)

# Print the table of contents
 niv = int(table_of_contents[0].get('tag_name')[1:])
 debut = "0"
 ii = 0

 for i in table_of_contents:
    nniv = int(i.get('tag_name')[1:])

    if nniv > niv:
        ii += 1
        debut = debut + ".1"
    elif nniv == niv:
        debut = ".".join(debut.split(".")[:-1] + [str(int(debut.split(".")[-1]) + 1)])
    else:
        ii -= 1
        debut = ".".join(debut.split(".")[:-2] + [str(int(debut.split(".")[-2]) + 1)])

    niv = nniv
    def ch(a):
      if len(a)==1:
        return a[0]
      elif len(a)==2:
        return [a[0],chr(96 + int(a[1]))]
      else :
        
        return [a[0],chr(96 + int(a[1])),roman.toRoman(int(a[2]))]+a[3::]
    chh=ch(debut.split("."))
    rt['.'.join(chh)]=i.get('content')
 return rt 
def extract_table_of_contents(soup):
    """
    Extracts the table of contents from a BeautifulSoup object.
    
    Args:
    - soup: BeautifulSoup object representing the parsed HTML
    
    Returns:
    - table_of_contents (dict): A dictionary representing the table of contents
                                with hierarchical structure based on heading tags
    """
    table_of_contents = {}
    current_level = table_of_contents
    
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    for heading in headings:
        tag_name = heading.name
        title = heading.get_text().strip()
        level = int(tag_name[1])  # Extract the level from the tag name (e.g., 'h1' -> level 1)
        
        # Create a new entry in the table of contents
        current_level[level] = {'title': title, 'subheadings': {}}
        
        # Update the current level based on the hierarchy
        if level == 1:
            current_level = table_of_contents
        else:
            parent_level = level - 1
            # Ensure the parent level exists before accessing it
            if parent_level in current_level:
                current_level = current_level[parent_level]['subheadings']
    
    return table_of_contents 
def extract_title(soup):
    """
    Extracts the title from a BeautifulSoup object.
    
    Args:
    - soup: BeautifulSoup object representing the parsed HTML
    
    Returns:
    - title (str): The text of the title tag, or None if not found
    """
    title_tag = soup.title
    if title_tag:
        return title_tag.get_text().strip()
    else:
        return None    
def extract_meta_tags(soup):
    """
    Extracts meta tags from a BeautifulSoup object.
    
    Args:
    - soup: BeautifulSoup object representing the parsed HTML
    
    Returns:
    - meta_tags (dict): A dictionary containing meta tag names as keys and their content as values,
                        with numerical keys for multiple occurrences of the same tag
    """
    meta_tags = {}
    meta_elements = soup.find_all('meta')
    for i, meta in enumerate(meta_elements, start=1):
        name = meta.get('name', f'meta_{i}')
        content = meta.get('content', '')
        meta_tags[name] = content.strip()
    return meta_tags    
def scrape_headings_from_html(soup):
    # Parse the HTML content
    
    # Find all heading tags (h1, h2, h3, h4, h5, h6)
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6','p','a'])
    
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
      #  if tag_name not in headings_dict:
       #     headings_dict[tag_name] = {}
       # headings_dict[tag_name][order] = heading_text
        headings_dict[tag_name+"_i_"+str(order)] = heading_text
    
    return headings_dict    
def get_html_text(url):
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
                
                response = requests.get(testedurl, allow_redirects=True)
           
            if response.status_code == 200:
                soup=BeautifulSoup(response.text)
                fj={'status': 'success','titles':tbl(soup),'topic':extract_title(soup),'metas':extract_meta_tags(soup),'final':str(response.url),'prefix':prefix, 'data': soup.get_text()}#,'testedurl':testedurl,'lasturl':str(list(map(lambda a:a.url,response.history))),
                
                #fj.update(scrape_headings_from_html(soup))
                
                return  jsonify(fj)

        except Exception as e:#requests.RequestException
            print(f"Error occurred while trying {prefix + url}: {e}")
            ers.append(e)
    return jsonify({'status': 'failed','ers':str(ers),'lasturl':'', 'data': '','prefix':'','testedurl':testedurl})
   except Exception as problem:
           return jsonify({'status': 'failed',"error":str(problem),'lasturl':'', 'data': '','prefix':'','testedurl':testedurl})

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
 try:   
  return get_html_text(request.url.replace(r"https://extract-webpage.onrender.com/",""))
 except Exception as me:
  return str(me)   
