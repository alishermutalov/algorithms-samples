from typing import List

def findContentChildren(g:List[int], s:List[int])->int:
    g.sort()
    s.sort()
    counter = 0
    i, j = 0, 0 
    
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            counter += 1
            i += 1  
        j += 1

    return counter

print(findContentChildren([1,2,3],[1,1]))

