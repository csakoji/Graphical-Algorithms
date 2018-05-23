from math import inf

alist = [[0,5,1,2],
		[5,0,3,inf],
		[1,3,0,4],
		[2,inf,0,4]
		]

interation = 0
while interation < len(alist):
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	print("iteration is {}".format(interation))
	for row in range(0, len(alist)):
		if row == interation:
			continue
		for col in range(0, len(alist[row])):
			if col == interation or col == row:
				continue
			print("row is {}".format(row))
			print("col is {}".format(col))
			print("alist[row][col] is {}".format(alist[row][col]))
			print("alist[row][iteration] is {}".format(alist[row][interation]))
			print("alist[col][iteration] is {}".format(alist[col][interation]))
			if alist[row][col] > (alist[row][interation] + alist[col][interation]):
				alist[row][col] = (alist[row][interation] + alist[col][interation])
			print(alist)
	interation += 1

print(alist)