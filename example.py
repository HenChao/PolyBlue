from polyBlueClient import PolyBlueClient

p = PolyBlueClient('tornado-polyblue')
p.sendOutput("This is an example program.")

try:
	while True:
		result = p.getInput("What is your name?")
		p.sendOutput("Hello %s" % result)
finally:
	p.close()
