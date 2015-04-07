import os
import tornado.ioloop
import tornado.web
import tornado.template
import tornado.websocket

clients = dict()

class IndexHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self):
		loader = tornado.template.Loader("templates/")
		self.write(loader.load("index.html").generate())
		self.finish()

class WebSocketHandler(tornado.websocket.WebSocketHandler):
	def open(self, *args):
		self.id = self.get_argument("Id")
		self.stream.set_nodelay(True)
		clients[self.id] = {"id":self.id, "object": self}

	def on_message(self, message):
		print "Client %s received a message: %s" % (self.id, message)

	def on_close(self):
		if self.id in clients:
			del clients[self.id]

app = tornado.web.Application([
	(r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static/'}),
	(r'/', IndexHandler),
	(r'/socket', WebSocketHandler),
])

port = os.getenv('VCAP_APP_PORT', '5000')

if __name__ == "__main__":
	app.listen(int(port))
	print("Server running on port: %s" % port)
	try:
		tornado.ioloop.IOLoop.instance().start()
	except KeyboardInterrupt:
		print("Shutting down webserver")
		tornado.ioloop.IOLoop.instance().stop()
