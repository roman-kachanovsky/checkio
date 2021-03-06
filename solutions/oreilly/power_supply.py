""" --- Power Supply --- Simple

You are given power networks and power-plant's information
(plant-number and supply-range). You should find out blackout
cities. Power-plant can supply himself and connected cities
with power. but the range is limited.

Input:          Two arguments. The first one is network,
                that represented as a list of connections.
                Each connection is a list of two nodes that are
                connected. City or Power Plant can be a node.
                Each City or Power Plant is a unique string.
                The second argument is a dict where keys are
                Power Plants and values are Power Plant's range.
Output:         Is a list of strings. Each string is a name of blacked cities.
Precondition:   required

"""


def my_solution(network, power_plants):
    def find_shortest_path(g, s, e, p):
        p = p + [s]

        if s == e:
            return p

        if s not in g.keys():
            return None

        shortest = None

        for n in g[s]:
            if n not in p:
                new_path = find_shortest_path(g, n, e, p)
                if new_path and (not shortest or len(new_path) < len(shortest)):
                    shortest = new_path
        return shortest

    all_points = {n for subnet in network for n in subnet}
    cities = all_points - set(power_plants.keys())
    covered_cities = []

    supply_graph = {k: [m[0] if k != m[0] else m[1] for m in network if k in m] for k in all_points}

    for plant, supply_range in power_plants.items():
        for city in cities:
            path = find_shortest_path(supply_graph, city, plant, [])

            if path and len(path) - 1 <= supply_range:
                covered_cities.append(city)

    return cities - set(covered_cities)


def sim0000_solution(networks, power_plants):
    from collections import deque

    net = [set(link) for link in networks]
    result = set.union(*net)
    for supply in power_plants:
        q = deque([(supply, power_plants[supply])])
        powered = set()
        while q:
            s, d = q.popleft()
            if s in powered or d < 0: continue
            powered |= {s}
            q.extend(((link - {s}).pop(), d - 1) for link in net if s in link)
        result -= powered
    return sorted(result)


def gyahun_dash_solution(network, plants):
    connections = tuple(map(set, network))
    cities = set.union(*connections)

    for plant, power in plants.items():
        supplied = {plant}
        for distance in range(power):
            supplied.update(*filter(supplied.intersection, connections))
        cities -= supplied
    return list(cities)
