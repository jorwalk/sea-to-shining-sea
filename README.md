# From Sea To Shining Sea

Given a list of 50 capitals in the United States of America, 
and the distance of every capital from each other, what is the 
shortest possible route that visits each  and returns to the origin city?

The travelling saleman problem - from sea to shining sea.

## How did this project came about?
- What is my inspiration for this article?
- If tomorrow a flying drone was available to the general public, I would want to travel to all 50 capitals
- If you wanted to visit the capital of all 50 states, what would be the most optimal order.

## What is the travelling salesman problem?

## Where was the data sourced?

## What tools and code were used?
### OR Tools
### Self-Organizing Maps


https://public.opendatasoft.com/explore/dataset/1000-largest-us-cities-by-population-with-geographic-coordinates/table/?sort=-rank&location=7,33.9388,-117.65259&basemap=jawg.streets

The travelling salesman problem (TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?" It is an NP-hard problem in combinatorial optimization, important in operations research and theoretical computer science.

The travelling purchaser problem and the vehicle routing problem are both generalizations of TSP.

In the theory of computational complexity, the decision version of the TSP (where, given a length L, the task is to decide whether the graph has any tour shorter than L) belongs to the class of NP-complete problems. Thus, it is possible that the worst-case running time for any algorithm for the TSP increases superpolynomially (but no more than exponentially) with the number of cities.

The problem was first formulated in 1930 and is one of the most intensively studied problems in optimization. It is used as a benchmark for many optimization methods. Even though the problem is computationally difficult, a large number of heuristics and exact algorithms are known, so that some instances with tens of thousands of cities can be solved completely and even problems with millions of cities can be approximated within a small fraction of 1%.[1]

The TSP has several applications even in its purest formulation, such as planning, logistics, and the manufacture of microchips. Slightly modified, it appears as a sub-problem in many areas, such as DNA sequencing. In these applications, the concept city represents, for example, customers, soldering points, or DNA fragments, and the concept distance represents travelling times or cost, or a similarity measure between DNA fragments. The TSP also appears in astronomy, as astronomers observing many sources will want to minimize the time spent moving the telescope between the sources. In many applications, additional constraints such as limited resources or time windows may be imposed.

NP-hardness

NP-hardness (non-deterministic polynomial-time hardness), in computational complexity theory, is the defining property of a class of problems that are, informally, "at least as hard as the hardest problems in NP". A simple example of an NP-hard problem is the subset sum problem.

A more precise specification is: a problem H is NP-hard when every problem L in NP can be reduced in polynomial time to H; that is, assuming a solution for H takes 1 unit time, we can use H‎'s solution to solve L in polynomial time.[1][2] As a consequence, finding a polynomial algorithm to solve any NP-hard problem would give polynomial algorithms for all the problems in NP, which is unlikely as many of them are considered difficult.[3]

A common misconception is that the NP in "NP-hard" stands for "non-polynomial" when in fact it stands for "non-deterministic polynomial acceptable problems".[4] Although it is suspected that there are no polynomial-time algorithms for NP-hard problems, this has not been proven.[5] Moreover, the class P, in which all problems can be solved in polynomial time, is contained in the NP class.[6]


Combinatorial optimization

In Operations Research, applied mathematics and theoretical computer science, combinatorial optimization is a topic that consists of finding an optimal object from a finite set of objects.[1] In many such problems, exhaustive search is not tractable. It operates on the domain of those optimization problems, in which the set of feasible solutions is discrete or can be reduced to discrete, and in which the goal is to find the best solution. Some common problems involving combinatorial optimization are the travelling salesman problem ("TSP") and the minimum spanning tree problem ("MST").

Combinatorial optimization is a subset of mathematical optimization that is related to operations research, algorithm theory, and computational complexity theory. It has important applications in several fields, including artificial intelligence, machine learning, auction theory, and software engineering.

Some research literature[2] considers discrete optimization to consist of integer programming together with combinatorial optimization (which in turn is composed of optimization problems dealing with graph structures) although all of these topics have closely intertwined research literature. It often involves determining the way to efficiently allocate resources used to find solutions to mathematical problems.

```
 $ python3 -m pip install ortools
 $ python3 -m pip install geopy
```

```
$ python3 map.py
```
## Data
TBD: json file with lon lat of all 50 capitals
```
{
    "abbr": "MO",
    "name": "Missouri",
    "capital": "Jefferson City",
    "lat": "38.572954",
    "long": "-92.189283"
}
```

## Python Libraries
TBD: Talk about the libraries that I used in python, what was there purpose

## OpenLayers
TBD: Stamen terrain basemap

## Flask App

## Reference Links
- https://developers.google.com/optimization/routing/tsp#or-tools
- https://geopy.readthedocs.io/en/stable/
- https://openlayers.org/en/latest/examples/flight-animation.html
- https://towardsdatascience.com/using-unsupervised-learning-to-plan-a-paris-vacation-geo-location-clustering-d0337b4210de
-  https://jsfiddle.net/jonataswalker/079xha47/
- https://github.com/DiegoVicen/som-tsp