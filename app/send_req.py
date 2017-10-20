#Python master which runs a ruby script to generate the required url depending on search queries, then makes an API request and retrieves XML

import requests
import subprocess
import search_parser
import os
import string

cwd = os.getcwd()
RUBY_SLAVE = cwd + "/app/search_request_gen.rb"

def get_search_results(searchQuery, numberOfResults, searchIndex = "All"):

	temp_XML_file_path = cwd + "../" + "Responses/temp_search_results_%s.xml" %("0")
	cmd = "ruby " + RUBY_SLAVE + " " + string.replace(searchQuery, " ", "+") + " " + searchIndex
	inputstr = subprocess.check_output(cmd, shell=True)
	inputstr = inputstr[:len(inputstr) - 1]
	
	r = requests.get(inputstr)
	responseXML = r.text.encode('utf-8').strip()

	

	return search_parser.searchXMLParse(responseXML, numberOfResults)
