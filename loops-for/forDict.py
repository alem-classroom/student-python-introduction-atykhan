#dict = {'first': 'a', 'second': 'b'}
def reverse_dict(dict):
	inv_map = {v: k for k, v in dict.items()}
	return(inv_map)
#print(reverse_dict(dict))
