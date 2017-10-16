from flask import Flask
from flask import request
import app.send_req
import json
from flask import make_response
from responses import makeWebhookResponse

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
  return 'This is an app used for an e-commerce price-tracking chatbot. What are YOU doing here?'

@app.route("/", methods=['POST'])
def post_handler():
	req = request.get_json(silent=True, force=True)

	#Perform the search after getting the JSON from API.ai
	#searchQuery = "iphone 7"
	#searchIndex = "All"

	if req['status']['code'] != 200:
		print "Status code not 200"
		raise

	webhookResponse = makeWebhookResponse(req)

	webhookResponse = json.dumps(webhookResponse, indent=4)
	r = make_response(webhookResponse)
	r.headers['Content-Type']='application/json'

	return r

if __name__ == '__main__':
  app.run()

