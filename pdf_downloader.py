#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

url="http://www.gatsby.ucl.ac.uk/teaching/courses/ml1-2016.html"

down_path='/PDF_downloads'

try:
    print("Checking Directory status")
    os.stat(down_path)
except:
    os.mkdir(down_path)
    print("Directory Created")

response=requests.get(url)
html_file=BeautifulSoup(response.text, "html.parser")
print(html_file.prettify())

for link in html_file.select("a[href$='.pdf']"):
    print("Links Present in the Website are:")
    print("\n")
    print(link)
    filename=os.path.join(down_path,link['href'].split('/')[-1])
    print("Downloading PDF\n")
    with open(filename,'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)
    
