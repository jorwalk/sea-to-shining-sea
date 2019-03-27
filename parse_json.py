import json

with open('states.json') as json_file:
    data = json.load(json_file)
    print(data[0])

    # for d in data:
    #     print('Name: ' + p['name'])
    #     print('Website: ' + p['website'])
    #     print('From: ' + p['from'])
    #     print('')