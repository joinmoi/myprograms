
#2b - binary search 
def bin_search (a_list, target): 
    low = 0 
    high = len(a_list)
    while low < high: 
        mid = (low + high) //2
        if a_list[mid] == target:
            return mid
        elif a_list[mid] > target: 
            high = mid
        else: 
            low = mid + 1
    return -1