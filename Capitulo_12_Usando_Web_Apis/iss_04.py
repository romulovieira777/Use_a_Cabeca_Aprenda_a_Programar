import json
import requests
import turtle


screen = turtle.Screen()
screen.setup(1000, 500)
screen.bgpic('earth.gif')
screen.setworldcoordinates(-180, -90, 180, 90)

iss = turtle.Turtle()
turtle.register_shape('iss.gif')
iss.shape('iss.gif')

url = 'http://api.open-notify.org/iss-now.json'

reposnse = requests.get(url)

if reposnse.status_code == 200:
    response_dictionary = json.loads(reposnse.text)
    position = response_dictionary['iss_position']
    print('International Space Station at', position['latitude'], position['longitude'])
else:
    print('Houston, we have a problem:', reposnse.status_code)

turtle.mainloop()
