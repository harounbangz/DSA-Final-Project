"""
Graph Algorithms Implementation

Includes:

1. Dijkstra Shortest Path Algorithm
2. Prim Minimum Spanning Tree Algorithm

Data Structures and Algorithms Project
"""

import heapq



# Weighted Graph

graph = {


    "A": {
        "D":4
    },


    "B": {
        "C":2,
        "D":8
    },


    "C": {
        "B":2,
        "E":5,
        "J":10
    },


    "D": {
        "A":4,
        "B":8,
        "F":6,
        "G":3,
        "H":9,
        "K":6
    },


    "E": {
        "C":5,
        "H":4,
        "I":9,
        "J":2
    },


    "F": {
        "D":6,
        "G":1,
        "K":7
    },


    "G": {
        "D":3,
        "F":1,
        "K":4
    },


    "H": {
        "D":9,
        "E":4,
        "I":3,
        "K":6
    },


    "I": {
        "E":9,
        "H":3,
        "J":7
    },


    "J": {
        "C":10,
        "E":2,
        "I":7,
        "L":1
    },


    "K": {
        "D":6,
        "F":7,
        "G":4,
        "H":6
    },


    "L": {
        "J":1
    }

}



# -------------------------------
# DIJKSTRA ALGORITHM
# -------------------------------


def dijkstra(graph, start):


    distances = {

        vertex: float("inf")

        for vertex in graph

    }


    previous = {

        vertex: None

        for vertex in graph

    }


    distances[start] = 0


    queue = [

        (0,start)

    ]



    while queue:


        current_distance, current_vertex = heapq.heappop(queue)



        for neighbour, weight in graph[current_vertex].items():


            distance = (
                current_distance +
                weight
            )


            if distance < distances[neighbour]:


                distances[neighbour] = distance

                previous[neighbour] = current_vertex


                heapq.heappush(

                    queue,

                    (
                        distance,
                        neighbour
                    )

                )


    return distances, previous





# -------------------------------
# PRIM ALGORITHM
# -------------------------------


def prim(graph,start):


    visited = set()


    mst = []


    edges = [

        (0,start,None)

    ]


    total_cost = 0



    while edges:


        weight, node, parent = heapq.heappop(edges)



        if node in visited:

            continue



        visited.add(node)



        if parent:

            mst.append(

                (
                    parent,
                    node,
                    weight
                )

            )


            total_cost += weight



        for neighbour, cost in graph[node].items():


            if neighbour not in visited:


                heapq.heappush(

                    edges,

                    (
                        cost,
                        neighbour,
                        node
                    )

                )


    return mst, total_cost




# -------------------------------
# MAIN PROGRAM
# -------------------------------


print("===== Graph Algorithms =====")



print("\nDijkstra Shortest Paths from A")


distances, previous = dijkstra(

    graph,

    "A"

)



for node, distance in distances.items():

    print(
        "A to",
        node,
        "=",
        distance
    )



print("\nPrim Minimum Spanning Tree")


mst, cost = prim(

    graph,

    "A"

)



for edge in mst:

    print(edge)



print(
    "\nTotal MST Cost:",
    cost
)