from math import inf

alist = [[0,5,inf,10],
		[inf,0,3,inf],
		[inf,inf,0,1],
		[inf,inf,inf,0]
		]

interation = 0
while interation < len(alist):
	# print("iteration is {}".format(interation))
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
			if alist[row][col] > (alist[row][interation] + alist[col][interation]):
				alist[row][col] = (alist[row][interation] + alist[col][interation])
	interation += 1

print(alist)
