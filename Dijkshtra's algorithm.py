from math import inf

# Graph input for algorithm
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
# acost = cost of vertex
# vertex equal to corresponding index of this array
acost = [0, inf, inf, inf, inf, inf, inf, inf, inf]
# array of uvisited vertex
aunvisited = [1, 2, 3, 4, 5, 6, 7, 8]
# array of visited vertex
avisited = [0]

def cost_modify(vertex, cost, graph):
	'''function to modify the cost of all vertices connected to "vertex" vertex'''
	for i in range(0, len(cost)):
		# Check if edge is present from vertex "vertex" to i'th vertex
		# if edge present then check if current cost of i'th vertex is greater than weight 
		# of edge and cost of vertex "vertex"
		if graph[vertex][i] and cost[i] > (graph[vertex][i] + cost[vertex]):
			# If both conditions are true then modify cost of i'th vertex
			cost[i] = (graph[vertex][i] + cost[vertex])
	# return cost array
	return cost

def find_next_vertex(visited, unvisited, cost):
	'''function to find the next unvisited vertex from graph with minimum cost'''
	#starting minimum value assumption
	amin = 10000
	# iterate over all vertices in unvisited array
	for i in unvisited:
		# modify the minimum value accordingly
		if cost[i] < amin:
			amin = cost[i]
	# Find the index of minimum value found in cost array which will be next vertex to start with
	vertex = cost.index(amin)
	# Remove that vertex from unvisited array
	unvisited.remove(vertex)
	# Append the same vertex to visited array
	visited.append(vertex)
# 	print("unvisited is {}".format(unvisited))
	return vertex

# Consider starting vertex as 0
start_vertex = 0

# Loop until their is unvisited vertex present
while(len(aunvisited)):
	acost = cost_modify(start_vertex, cost=acost, graph=agraph)
# 	print("acost is {}".format(acost))
	start_vertex = find_next_vertex(visited=avisited, unvisited=aunvisited, cost=acost)
# 	print("start vertex is {}".format(start_vertex))

print(acost)
