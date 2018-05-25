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

# Always Consider starting vertex as 0
# Cost of starting vertex will always be zero
acost = [0, inf, inf, inf, inf, inf, inf, inf, inf]
# array of unvisited vertces
aunvisited = [1, 2, 3, 4, 5, 6, 7, 8]
# array of visited vertices
avisited = [0]


# modify cost array with respective to edge between current starting vertex and
# cost of unvisited vertices in unvisited array
def cost_modify(vertex, cost, graph, unvisited):
	# Iterate over all the elements in cost array
	for i in range(0, len(cost)):
		# If element at i'th index in still unvisited depending upon following condition
		# if their is edge exist between current starting vertex and i'th vertex
		# if true, then compare the weight of that edge with respect ot that of cost of i'th vertex
		if graph[vertex][i] and i in unvisited and cost[i] > graph[vertex][i]:
			cost[i] = graph[vertex][i]
	return cost

# Find next starting vertex
def find_next_vertex(visited, unvisited, cost):
	# minimum value assumption
	amin = 10000
	# Iterate over all elements in unvisited array and
	# find element with minimun weight in cost array
	# which is present in unvisited array
	for i in unvisited:
		if cost[i] < amin:
			amin = cost[i]

	# This is to find vertex with minium weight in cost array present in 
	# unvisited array in case of multiple occurances of minimum weight value 
	# elements in cost array
	vertex = [i for i in range(0, len(cost)) if cost[i] == amin]
	for i in vertex:
		if i in visited:
			continue
	vertex = i
	print("vertex in function is {}".format(vertex))
	# remove that element from unvisited array
	unvisited.remove(vertex)
	# Add the same element in visited array
	visited.append(vertex)
	print("unvisited is {}".format(unvisited))
	return vertex

# Always consider 1st vertex as starting vertex 
start_vertex = 0

# Iterate over until all the elements are visited exactly once
while(aunvisited):
	acost = cost_modify(start_vertex, cost=acost, graph=agraph, unvisited=aunvisited)
	print("acost is {}".format(acost))
	start_vertex = find_next_vertex(visited=avisited, unvisited=aunvisited, cost=acost)
	print("start vertex is {}".format(start_vertex))

print(avisited)