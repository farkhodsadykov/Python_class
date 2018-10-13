import requests
import json

newlist = ['Chicago', 'Denver', 'San Jose']


for address in newlist:
    data = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=Washington,DC&destinations=' + address  +',NY&key=token')
    data = data.json()
    print('From :', data['origin_addresses'][0]+ ' to :' +data['destination_addresses'][0]+ ' Miles :' + data['rows'][0]['elements'][0]['distance']['text'])
