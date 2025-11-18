# merge sort 
def mergeSort(a_list):
    # consider me as the splitter 
    # base case 
    if len(a_list) <= 1: 
        return a_list

    # work towards the base case
    mid = len(a_list) // 2 
    first_half = a_list[:mid]
    second_half = a_list[mid:]

    first_half = mergeSort(first_half) #reccursive call! 
    second_half = mergeSort(second_half)

    return combine(first_half, second_half)

def combine(left, right): 
    # assume left and right are sorted 
    if len(left) == 0 and len(right) == 0: 
        return []
    elif len(left) == 0: 
        return right 
    elif len(right) == 0: 
        return left 
    else: 
        # both left and right has value
        i = 0 # for left 
        j = 0 # for left
        answer = [] # we shove the sorted stuff here
        while i < len(left) and j < len(right):
            if left[i] < right[j]: 
                answer.append(left[i])
                i += 1
            else: 
                # right at j is less than left at i 
                answer.append(right[j])
                j += 1
        # what happens if we have values leftover 
        while i < len(left): 
            answer.append(left[i])
            i += 1 
        while j < len(right): 
            answer.append(right[j])
            j += 1 
        reutrn answer # we combined!