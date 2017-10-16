#Python master which runs a ruby script to generate the required url depending on search queries, then makes an API request and retrieves XML

import requests
import subprocess
import search_parser

#Replace with absolute ruby path
RUBY_SLAVE = "search_request_gen.rb"
#Replace with absolute path in Azure
#TODO
temp_XML_file_path = "/Users/vedantc98/Desktop/Code/HAL9000/Responses/temp_search_results.xml"

def get_request_url(searchQuery, searchIndex = "All"):

	cmd = "ruby " + RUBY_SLAVE + " " + searchQuery + " " + searchIndex
	inputstr = subprocess.check_output(cmd, shell=True)
	inputstr = inputstr[:len(inputstr) - 1]
	
	r = requests.get(inputstr)
	responseXML = r.text.encode('utf-8').strip()

	xmlFile = open(temp_XML_file_path, "w")
	xmlFile.write(responseXML)
	xmlFile.close()

	search_parser.searchXMLParse(temp_XML_file_path)

query = raw_input().strip()
get_request_url(query.replace(" ", "+"))