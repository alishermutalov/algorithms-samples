def count(n):
    print(n)
    if n<=1:
        return
    else:
        count(n-1)
    
count(10) # It will count from 10 to 1