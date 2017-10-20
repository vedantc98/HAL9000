import requests
import json

def shorten(longUrl):
	api_url = "https://www.googleapis.com/urlshortener/v1/url"
	api_key = "AIzaSyAxzTyMGys0LT6gs5vBewpx7orR2nxPX9M"
	headers = {"Content-Type" : "application/json"}
	
	raw = {"longUrl" : longUrl}
	payload = json.dumps(raw)

	url = api_url + "?key=" + api_key

	res = requests.post(url, data = payload, headers = headers)
	res_dict = json.loads(res.text)

	return res_dict['id']