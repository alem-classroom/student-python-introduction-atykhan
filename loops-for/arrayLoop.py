#arr = [1, 2, 3]
#num = 5
def insert_squares(arr, num):
    # add square of numbers from 1 to num to the list named arr and return list
	for i in range (num):
		k = (i+1)*(i+1)
		arr.append(k)
	return(arr)

#a = [1, 2, 3]
#n = 5
#print(insert_squares(a,n))