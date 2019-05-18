# Search methods

import search


ab = search.GPSProblem('A', 'B', search.romania)


print(" _______ANCHURA______")
print(search.breadth_first_graph_search(ab).path())
print()
print("________PROFUNDIDAD___")
print(search.depth_first_graph_search(ab).path())
print()
print("________RAMIFICACIÓN Y ACOTACIÓN______")
print(search.branchAndBound(ab).path())
print()
print("______RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACIÓN____")
print(search.branchAndBoundSubestimation(ab).path())

""" Result:
 [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
 [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450 """


print("\nTraza del camino AC")

ac = search.GPSProblem('A', 'C'
                       , search.romania)

print(search.breadth_first_graph_search(ac).path())     ## anchura
print(search.depth_first_graph_search(ac).path())       ## profundidad
print(search.branchAndBound(ac).path())
print(search.branchAndBoundSubestimation(ac).path())    # Coste+h


print("\nTraza del camino GZ")

gz = search.GPSProblem('G', 'Z'
                       , search.romania)

print(search.breadth_first_graph_search(gz).path())     ## anchura
print(search.depth_first_graph_search(gz).path())       ## profundidad
print(search.branchAndBound(gz).path())
print(search.branchAndBoundSubestimation(gz).path())    ## Coste+h
