from math import inf

agraph = {0: [0, 4, 0, 0, 0, 0, 0, 8, 0],
  		 1: [4, 0, 8, 0, 0, 0, 0, 11, 0],
  		 2: [0, 8, 0, 7, 0, 4, 0, 0, 2],
  		 3: [0, 0, 7, 0, 9, 14, 0, 0, 0],
  		 4: [0, 0, 0, 9, 0, 10, 0, 0, 0],
  		 5: [0, 0, 4, 14, 10, 0, 2, 0, 0],
  		 6: [0, 0, 0, 0, 0, 2, 0, 1, 6],
  		 7: [8, 11, 0, 0, 0, 0, 1, 0, 7],
  		 8: [0, 0, 2, 0, 0, 0, 6, 7, 0]
 		}

# Consider starting vertex as 0
acost = [0, inf, inf, inf, inf, inf, inf, inf, inf]
aunvisited = [1, 2, 3, 4, 5, 6, 7, 8]
avisited = [0]

def cost_modify(vertex, cost, graph):
	for i in range(0, len(cost)):
		if graph[vertex][i] and cost[i] > (graph[vertex][i] + cost[vertex]):
			cost[i] = (graph[vertex][i] + cost[vertex])
	return cost

def find_next_vertex(visited, unvisited, cost):
	amin = 10000
	for i in unvisited:
		if cost[i] < amin:
			amin = cost[i]
	vertex = cost.index(amin)
	visited.append(unvisited.remove(vertex))
	print("unvisited is {}".format(unvisited))
	return vertex

start_vertex = 0

while(len(aunvisited)):
	acost = cost_modify(start_vertex, cost=acost, graph=agraph)
	print("acost is {}".format(acost))
	start_vertex = find_next_vertex(visited=avisited, unvisited=aunvisited, cost=acost)
	print("start vertex is {}".format(start_vertex))

print(acost)