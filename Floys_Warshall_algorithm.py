from math import inf

# Input graph for algorithm
alist = [[0,5,inf,10],
	[inf,0,3,inf],
	[inf,inf,0,1],
	[inf,inf,inf,0]
	]

# Iteration number
interation = 0

# Loop till iterations equal to number of vertices is done
while interation < len(alist):
	# print("iteration is {}".format(interation))
	# Iterate over each row and column of input graph except row==col and (row or col) == iteration  
	for row in range(0, len(alist)):
		if row == interation:
			continue
		for col in range(0, len(alist[row])):
			if col == interation or col == row:
				continue
			# print("row is {}".format(row))
			# print("col is {}".format(col))
			# print("alist[row][col] is {}".format(alist[row][col]))
			# print("alist[row][iteration] is {}".format(alist[row][interation]))
			# print("alist[col][iteration] is {}".format(alist[col][interation]))
			
			# Check if the value of edge between any two vertices of graph is greater than 
			# distance between those two vertices via "iteration" vertex
			if alist[row][col] > (alist[row][interation] + alist[col][interation]):
				# If true them modify the distance value between those two vertices
				alist[row][col] = (alist[row][interation] + alist[col][interation])
	# Increament the iteration vertex to next vertex
	interation += 1

print(alist)
