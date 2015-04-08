from polyBlueClient import PolyBlueClient

p = PolyBlueClient()
p.sendOutput("This is an example program.")
result = p.getInput("What is your name?")

p.sendOutput("Hello %s" % result)
p.close()
