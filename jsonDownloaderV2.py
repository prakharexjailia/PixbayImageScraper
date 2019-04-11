import json
from pprint import pprint
import urllib2
import sys    #Importing the System Library

from urllib2 import Request,urlopen
from urllib2 import URLError, HTTPError

key = "a45646ad64a6d4a64d64ad" # put your key here in quotes get it from https://pixabay.com/api/docs/ under parameter by creating account.
query = "Nature"               # your query
pageCount = 30                 # query pages OPTIONAL
ImagePerPage = 50              # no of image per page OPTIONAL
count = 1
while (count <= pageCount):
	imageuri = "https://pixabay.com/api/?key="+key+"&q="+query+"&image_type=photo&page="+str(count)+"&per_page="+str(ImagePerPage) 
	imageuri=imageuri.lower()
	print(imageuri)
	req = Request(imageuri, headers={"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
	response = urlopen(req,None,15)
	output_file = open("Jsons/data"+str(count)+".json",'wb')
	data = response.read()
	output_file.write(data)
	response.close()
	print("json "+str(count)+" downloaded.")
	count = count + 1
print("All json downloaded.")
