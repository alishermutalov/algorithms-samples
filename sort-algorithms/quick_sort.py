# example 1
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