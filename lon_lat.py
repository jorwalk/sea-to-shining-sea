import json
import itertools

with open('states.json') as json_file:
    capitals = json.load(json_file)


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


sequence = [24, 15, 26, 14, 12, 13, 16, 41, 9, 0, 8, 39, 32, 45, 19, 7, 29, 6, 38, 20, 28, 18, 44, 31, 37, 47, 34, 21,
            48, 22, 40, 33, 25, 11, 43, 27, 4, 36, 46, 1, 10, 2, 30, 5, 49, 35, 42, 17, 23, 3, 24]

flight_path = []
for x in list(pairwise(sequence)):
    from_capital = capitals[x[0]]
    to_capital = capitals[x[1]]

    from_path = [
        float(from_capital.get('lat')),
        float(from_capital.get('long'))]

    to_path = [
        float(to_capital.get('lat')),
        float(to_capital.get('long'))]

    flight_path.append([from_path,to_path])


print(flight_path)