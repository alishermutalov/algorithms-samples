myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]

def returnIndex(num_list: list, value:int):
    for i in range(len(num_list)):
        if num_list[i]==value:
            return i
    
    return None
        
res = returnIndex(myList,99)
print(res)