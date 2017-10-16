#Python master which runs a ruby script to generate the required url depending on search queries, then makes an API request and retrieves XML

import requests
import subprocess
import search_parser
import os

#Replace with absolute ruby path
cwd = os.getcwd()
RUBY_SLAVE = cwd + "/search_request_gen.rb"

def get_search_results(searchQuery, numberOfResults, userID, searchIndex = "All"):

	temp_XML_file_path = cwd + "../" + "Responses/temp_search_results_%s.xml" %(userID)
	cmd = "ruby " + RUBY_SLAVE + " " + searchQuery + " " + searchIndex
	inputstr = subprocess.check_output(cmd, shell=True)
	inputstr = inputstr[:len(inputstr) - 1]
	
	r = requests.get(inputstr)
	responseXML = r.text.encode('utf-8').strip()

	xmlFile = open(temp_XML_file_path, "w")
	xmlFile.write(responseXML)
	xmlFile.close()

	return search_parser.searchXMLParse(temp_XML_file_path, numberOfResults, userID)

#query = raw_input().strip()
#get_request_url(query.replace(" ", "+"))