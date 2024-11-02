# example 1
import random


def gcd(n:int,m:int)->int: #greatest common divisor
    if m == 0:
        return n
    else:
        return gcd(m, n % m)
    
print(gcd(45,27))

#example 2
def sum_list(list:list)->int | float:
    if len(list)==0:
        return 0
    else:
        return list.pop(-1) + sum_list(list)
    
print(sum_list([5,8,12,22]))

#example 3
def len_arr(array:list)->int:
    if not array:
        return 0
    array.pop()
    return len_arr(array)+1

print(len_arr([]))

# example 4
def max_value(array:list)->int | float:
    if len(array)==1:
        return array.pop()
    a = array.pop()
    b = max_value(array)
    return a if a>b else b

print(max_value([1,2,3,5,112]))
    
#example 5
def qsort(array:list)->list:
    if len(array)<2:
        return array
    else:
        pivot = array.pop(random.randrange(len(array)))
        minimum = [i for i in array if i<=pivot]
        maximum = [i for i in array if i>=pivot]
        return qsort(minimum)+[pivot]+qsort(maximum)
    
print(qsort([1,5,112,34,52,66]))