import json
from geopy import distance

# Open the json file that contains the data about the state capitals
with open('states.json') as json_file:
    capitals = json.load(json_file)

    matrix = []

    for i in range(0, 50):
        # the initial capital where the distance will be computed from
        a_lat = capitals[i].get('lat')
        a_lon = capitals[i].get('long')

        a = (a_lat, a_lon)

        dist = []
        # iterate over the rest of the capitals]
        for capital in capitals:
            b_lat = capital.get('lat')
            b_lon = capital.get('long')

            b = (b_lat, b_lon)

            # calculate the distance between the two
            miles = round(distance.distance(a, b).miles)
            dist.append(miles)

        matrix.append(dist)

print(matrix)