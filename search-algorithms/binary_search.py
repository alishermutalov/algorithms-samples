#Binary search ---> (desc.) || qadamlar soni : log2(N)
myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]

def binary_search_func(list,n):
    left, right = 0, len(list)
    step_counter = 1
    list_steps = []
    while left <= right:
        step_counter+=1
        mid = (left+right)//2
        list_steps.append(mid)
        if list[mid] == n:
            return mid, step_counter, list_steps
        elif list[mid]<n:
            left = mid+1
        else:
            right = mid-1
    return None

print(binary_search_func(myList,6))
        