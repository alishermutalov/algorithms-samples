def selection_sort(ulist:list) -> list:

    for i in range(len(ulist)):
        min_index = i
        for j in range(i+1,len(ulist)):
            if ulist[j]>ulist[min_index]:
                min_index=j
        
        ulist[i], ulist[min_index] = ulist[min_index], ulist[i]
                
    return ulist

print(selection_sort([1,2,3,4,5,7,8,0,5,4,5]))