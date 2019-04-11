import json
import random
from pprint import pprint
import urllib2
import sys    #Importing the System Library

from urllib2 import Request,urlopen
from urllib2 import URLError, HTTPError
k=0

numberOfJsonFiles = 11  #count number of jsons file in jsons folder downloaded before and put it here

count = 1
while (count <= numberOfJsonFiles):
	with open('Jsons/data'+str(count)+'.json') as data_file:    
	    data = json.load(data_file)
	    for hello in data["hits"]:
	    	lal=hello 
	    	imageuri=lal["largeImageURL"]    # this tag image will be downloaded read json file. OPTIONAL
	    	imageuri = imageuri.replace(' ', '')[:-8].upper()
	    	temp="1280.jpg"       #completeing filename with extension read json files. OPTIONAL
	    	imageuri=imageuri+temp
	    	imageuri=imageuri.lower()
	    	print(imageuri)
	    	req = Request(imageuri, headers={"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
	    	response = urlopen(req,None,15)
	    	k=k+1
	    	output_file = open("Images/"+str(count)+str(k)+str(random.randrange(100000000000000000000))+".jpg",'wb')
	    	data = response.read()
	    	output_file.write(data)
	    	response.close()
	    data_file.close()
	    k=0
	count = count + 1

print("Image downloaded")
