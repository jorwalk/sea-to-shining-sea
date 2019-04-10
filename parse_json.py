import json

with open('states.json') as json_file:
    data = json.load(json_file)
    print(data)
    # for p in data['people']:
    #     print('Name: ' + p['name'])
    #     print('Website: ' + p['website'])
    #     print('From: ' + p['from'])
    #     print('')