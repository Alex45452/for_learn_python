def count(x):
    operation = x*10/3+100
    return operation
def count_list(*numbers):
    for number in numbers:
        print(count(number))
count_list(3, 6, 9)
