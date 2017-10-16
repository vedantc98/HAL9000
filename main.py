from flask import Flask
import app.send_req

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
  return 'This is an app used for an e-commerce price-tracking chatbot. What are YOU doing here?'

@app.route("/", methods=['POST'])
def post_handler():
	req=request.get_json(silent=True, force=True)

	#Perform the search after getting the JSON from API.ai
	searchQuery = "iphone 7"
	searchIndex = "All"

	app.send_req.get_request_url(searchQuery, searchIndex)

if __name__ == '__main__':
  app.run()

