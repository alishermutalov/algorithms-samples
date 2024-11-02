def gcd(n:int,m:int)->int: #greatest common divisor
    if m == 0:
        return n
    else:
        return gcd(m, n % m)
    
print(gcd(45,27))
    
    