#Python master which runs a ruby script to generate the required url depending on search queries, then makes an API request and retrieves XML

import requests
import subprocess
import xml.etree.ElementTree as ET

RUBY_SLAVE = "search_request_gen.rb"

def get_request_url(searchQuery, searchIndex = "All"):

	cmd = "ruby " + RUBY_SLAVE + " " + searchQuery
	inputstr = subprocess.check_output(cmd, shell=True)
	inputstr = inputstr[:len(inputstr) - 1]
	
	r = requests.get(inputstr)
	responseXML = r.text

	print responseXML

	#tree = ET.parse(r.text)

	#root = tree.getroot()


query = raw_input().strip()
get_request_url(query.replace(" ", "+"))