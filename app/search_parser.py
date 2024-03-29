import xml.etree.ElementTree as ET

def searchXMLParse(xmlFile, numberOfResults):
	tree = ET.fromstring(xmlFile)
	root = tree

	# Items begin from index 4
	items = root[1][4:]
	searchResults = []
	attributes = {}

	# Index 0 is the ASIN number
	ind = 1
	for item in items:
		attributes = {}
		#Item index in search
		attributes['index'] = ind
		ind += 1
		#Item ASIN 
		asin = item[0].text
		attributes['ASIN'] = asin
		#Item URL
		url = item[2].text
		attributes['DetailPageURL'] = url

		#ItemAttributes
		itemAttributes = None
		for i in xrange(len(item)):
			if item[i].tag.find("ItemAttributes") != -1:
				itemAttributes = item[i]
		
		for i in range(len(itemAttributes)):
			if itemAttributes[i].tag.find("ListPrice") != -1:
				attributes['ListPrice'] = itemAttributes[i][2].text
				attributes['price'] = int(itemAttributes[i][0].text)/100
			if itemAttributes[i].tag.find("Color") != -1:
				attributes['Color'] = itemAttributes[i].text
			if itemAttributes[i].tag.find("Brand") != -1:
				attributes['Brand'] = itemAttributes[i].text
			if itemAttributes[i].tag.find("Title") != -1:
				attributes['Title'] = itemAttributes[i].text

		searchResults.append(attributes)

	return searchResults[:numberOfResults]
