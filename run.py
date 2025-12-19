# Search methods

import search
import time

def print_results(result):
    print("Generados: ", result[3])
    print("Visitados: ", result[2])
    print("Costo total: ", result[1])
    print("Ruta: ", result[0].path())
    return

ab = search.GPSProblem('A', 'B'
                       , search.romania)

start=time.time()
result=search.branch_and_bound_with_overestimation_graph_search(ab)
end=time.time()

print_results(result)
print(f"Tiempo transcurrido: {(end-start)*1e6:.2f} µs")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
