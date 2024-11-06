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

def countPairs(nums: List[int], target: int) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]<target:
                count+=1
    return count

print(countPairs([-6,2,5,-2,-7,-1,3],-2))