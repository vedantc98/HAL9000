import send_req

DEFAULT_ITEMS = 3
SOURCE = "https://amazon.in"

def makeWebhookResponse(req):
	result = req['result']
	action = None
	contexts = None
	parameters = None
#	userID = None
	if 'action' in result:
		action = result['action']
	if 'contexts' in req:
		contexts = result['contexts']
	if 'parameters' in result:
		parameters = result['parameters']

#	userID = req['originalRequest']['data']['user']['user_id']

	if action == "web.search":
		response = searchResponse(parameters)
		return response

	else:
		return defaultResponse()

def searchResponse(parameters):
	searchQuery = parameters['q']
	searchIndex = "All"
	if 'index' in parameters:
		searchIndex = parameters['index']
	
	numberOfItems = DEFAULT_ITEMS
	if 'itemLimit' in parameters:
		numberOfItems = parameters['itemLimit']

	results = send_req.get_search_results(searchQuery, numberOfItems, searchIndex)
	speech = constructSpeechResponse(results)
	displayText = speech
#	contextOut = [{"name" : "searchResponseDisplayed", "lifespan" : "1", parameters : {}}] 
	data = {}

	return {
			"speech" : speech,
			"displayText" : displayText,
			#"contextOut" : contextOut,
			"source" : SOURCE
	}	


def constructSpeechResponse(results):
	speech = "Here's a list of %d responses for the item you requested:\n"
	i = 1

	for item in results:
		speech += str(i) + ". "
		speech += item['Title'] + "\n"
		speech += "Current price : " + item['ListPrice'] + "\n"
		speech += "Item url : " + item['DetailPageURL'] + "\n"
		speech += "\n"

	speech += "To track any one of these items, respond with 'Track [item_number]'"
	return speech

def defaultResponse():
	speech = "Could not find an appropriate response. File a bug?"
	return {
			"speech" : speech,
			"displayText" : speech,
			"source" : "Us"
	}

