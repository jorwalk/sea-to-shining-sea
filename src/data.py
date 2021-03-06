import json
import pathlib
import itertools

from geopy import distance

class Data:
    def __init__(self):
        self.matrix = []
        # states = pathlib.Path.cwd().joinpath('src','states.json')
        # with open(states) as json_file:
        #     self.capitals = json.load(json_file)

        cities = pathlib.Path.cwd().joinpath('src', 'cities.json')
        with open(cities) as json_file:
            self.cities = json.load(json_file)

    def distance(self):
        for i in range(0, 1000):
            # the initial capital where the distance will be computed from
            # a_lat = self.capitals[i].get('lat')
            # a_lon = self.capitals[i].get('long')
            a_lat = self.cities[i].get('fields')['coordinates'][0]
            a_lon = self.cities[i].get('fields')['coordinates'][1]

            a = (a_lat, a_lon)

            dist = []
            # iterate over the rest of the capitals]
            # for capital in self.capitals:
            #     b_lat = capital.get('lat')
            #     b_lon = capital.get('long')
            for city in self.cities:
                b_lat = city.get('fields')['coordinates'][0]
                b_lon = city.get('fields')['coordinates'][1]

                b = (b_lat, b_lon)

                # calculate the distance between the two
                miles = round(distance.distance(a, b).miles)
                dist.append(miles)

            self.matrix.append(dist)

    def capital_name(self, idx):
        return self.cities[idx].get('fields')['city']
        # return self.capitals[idx].get('capital')

    def pairwise(self, iterable):
        a, b = itertools.tee(iterable)
        next(b, None)
        return zip(a, b)

    def flight_path(self, sequence):
        flight_path = []
        for x in list(self.pairwise(sequence)):
            # from_capital = self.capitals[x[0]]
            # to_capital = self.capitals[x[1]]
            #
            # from_path = [
            #     float(from_capital.get('lat')),
            #     float(from_capital.get('long'))]
            #
            # to_path = [
            #     float(to_capital.get('lat')),
            #     float(to_capital.get('long'))]

            from_capital = self.cities[x[0]]
            to_capital = self.cities[x[1]]

            from_path = [
                float(from_capital.get('fields')['coordinates'][0]),
                float(from_capital.get('fields')['coordinates'][1])]

            to_path = [
                float(to_capital.get('fields')['coordinates'][0]),
                float(to_capital.get('fields')['coordinates'][1])]

            flight_path.append([from_path, to_path])

        return flight_path
