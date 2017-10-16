import send_req

DEFAULT_ITEMS = 3
SOURCE = "https://amazon.in"

def makeWebhookResponse(req):
	result = req['result']
	action = req['action']
	contexts = req['contexts']
	parameters = req['parameters']
	userID = req['user_id']

	if action == "web.search":
		response = searchResponse(parameters)
		return response

def searchResponse(parameters):
	searchQuery = parameters['q']
	searchIndex = "All"
	if 'index' in parameters:
		searchIndex = parameters['index']
	
	numberOfItems = DEFAULT_ITEMS
	if 'itemLimit' in parameters:
		numberOfItems = parameters['itemLimit']

	results = send_req.get_search_results(searchQuery, numberOfItems, userID, searchIndex)
	speech = constructSpeechResponse(results)
	displayText = speech
	contextOut = [{"name" : "searchResponseDisplayed", "lifespan" : "1", parameters : {}}] 
	data = {}

	return {
			"speech" : speech,
			"displayText" : displayText,
			#"contextOut" : contextOut,
			"source" : source
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
