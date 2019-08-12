def count(x):
    operation = x*10/3+100
    return operation
def count_list(my_list):    
    result = []    
    for number in my_list:
        result.append(count(number))
    return result    
print(count_list([3, 6, 9]))
