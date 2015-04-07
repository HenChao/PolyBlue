import os
import subprocess
import tornado.ioloop
import tornado.web
import tornado.template
import tornado.websocket

port = os.getenv('VCAP_APP_PORT', '5000')

class IndexHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self):
		loader = tornado.template.Loader("templates/")
		self.write(loader.load("index.html").generate(app_port=port))
		self.finish()

class WebSocketHandler(tornado.websocket.WebSocketHandler):
	proc = None
	stdoutput = None

	def open(self, *args):
		proc = subprocess.Popen('scripts/test.py',
					stdin=subprocess.PIPE,
					stdout=subprocess.PIPE,
					)
		stdoutput = proc.communicate()
		self.write_message(stdoutput[0])
		print ("Socket connection open")

	def on_message(self, message):
		print ("Received message: %s" % message)
		#self.write_message("The message received was - " + message)

	def on_close(self):
		pass

app = tornado.web.Application([
	(r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static/'}),
	(r'/', IndexHandler),
	(r'/socket', WebSocketHandler),
])

if __name__ == "__main__":
	app.listen(int(port))
	print("Server running on port: %s" % port)

	try:
		tornado.ioloop.IOLoop.instance().start()
	except KeyboardInterrupt:
		print("Shutting down webserver")
		tornado.ioloop.IOLoop.instance().stop()
