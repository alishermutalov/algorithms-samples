#example 1
def count(n):
    print(n)
    if n<=1:
        return
    else:
        count(n-1)
    
count(10) # It will count from 10 to 1

#example 2
def factorial(x):
    if x<=1:
       return 1
    else:
        return x*factorial(x-1)
    
print(factorial(5))