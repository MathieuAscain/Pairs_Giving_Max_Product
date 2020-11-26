# http://www.techiedelight.com/find-maximum-product-two-integers-array/

myList = [-10, -3, 5, 6, -2]

def search_the_max_index(productList):
	m = max(productList)
	myList = [i for i, j in enumerate(productList) if j == m]
	return myList

def research_pairs(givenList, maximum=0):
	index_position = []
	product = []
	for i in range(len(givenList)-1):
		for j in range(i + 1, len(givenList)):
			product_number = givenList[i] * givenList[j]
			if(product_number >= maximum):
				product.append(product_number)
				temp = []
				temp.append(i)
				temp.append(j)
				index_position.append(temp)
	maxProductIndex = search_the_max_index(product)
	print("Pairs of elements multiply together giving the maximum of the list : ")
	for elem in maxProductIndex:
		print("pair {0} : number {1} at position {2} muliply with number {3} at position {4}".format(elem + 1, givenList[index_position[elem][0]], index_position[elem][0], givenList[index_position[elem][1]], index_position[elem][1]))
	print('')

research_pairs(myList)
