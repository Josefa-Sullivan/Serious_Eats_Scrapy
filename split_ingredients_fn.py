import re


def split_ingredients(giant_str):

	giant_str = str(giant_str)
    result_lis = []
                   
    while True:
        match = re.search('[^ ],[^ ]', giant_str)
        
        if match == None:
            result_lis.append(giant_str)
            break
            
        result_lis.append(giant_str[: match.span()[1]-2])
        giant_str = giant_str[match.span()[1]-1:]

    return result_lis