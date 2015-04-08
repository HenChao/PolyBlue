from polyBlueClient import PolyBlueClient
# Be sure to import the Python module from the polyBlueClient.py file in your code

# Call the PolyBlueClient class and pass it the name of your BlueMix application
# In this example, the BlueMix application is running under 'tornado-polyblue',
# and can be accessed from http://tornado-polyblue.mybluemix.net
p = PolyBlueClient('tornado-polyblue')

# To send messages to the web console, call the sendOutput function and pass
# it the string you wish to display on the website
p.sendOutput("This is an example program.")

# To wait and receive input from the web console, call the getInput function
# and pass it a prompt to display on the website. In this example, the input
# from the website is stored as locally in the variable result
result = p.getInput("What is your name?")

p.sendOutput("Hello %s" % result)

# IMPORTANT! Be sure to close the connection at the end of your script
p.close()
