import os
from flask import Flask,render_template,request

app = Flask(__name__)

port = os.getenv('VCAP_APP_PORT', '5000')

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/sayHello", methods=['POST', 'GET'])
def sayHello():
	if request.method == 'GET':
		return "Hello " + request.args.get('Name', '')
	else:
		return "Hello " + request.form['Name']

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
