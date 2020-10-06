def insert_squares(arr, num):
    # add square of numbers from 1 to num to the list named arr and return list
    i = 1
    while i <= 5: 
    	k = i*i
    	arr.append(k)
    	i = i + 1
    return(arr)
#a = [1, 2, 3]
#n = 5
#print(insert_squares(a,n))