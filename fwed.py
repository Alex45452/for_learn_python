def count(x):
    operation = x*10/3+100
    return operation
def count_list(my_list):
    for number in my_list:
        print(count(number))
count_list(3, 6, 9)
