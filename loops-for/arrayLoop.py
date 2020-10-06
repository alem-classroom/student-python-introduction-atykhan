#arr = [1, 2, 3]
#num = 5
def insert_squares(arr, num):
    # add square of numbers from 1 to num to the list named arr and return list
	for i in num:
		arr[i+len(arr)] = i*i
		
	return(arr)

