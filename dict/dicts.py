def clear_dict(dict):
    # delete everything in dict and return it
    return(dict.clear())
def get_dict_items(dict):
    # return keys and values of dict
    return(dict.items())
def get_dict_keys(dict):
    # return keys of dict
    return(dict.keys())
def get_dict_value_by_key(dict, key):
    # return values of dict that is stored in key
    return(dict.get(key))
def delete_dict_element_by_key(dict, key):
    # delete and element from dict lpllpllsuch that its key is the argument key
    if key not in dict.keys():
        return(dict)
    else:
        dict.pop(key)
        return(dict)
d = {"a": [1, 2, 3], "b": 2, "c": 3}
key_to_remove = "c"

print(delete_dict_element_by_key(d, key_to_remove))