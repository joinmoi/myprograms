#homework question

num = [0, 1, 0, 3, 12]

# zero_list = [] 
# integer_list = []

# for i in a_list: 
#     if i == 0: 
#         zero_list.append(i)
#     else: 
#         integer_list.append(i)

# num = integer_list + zero_list
# print(num)

#my solution
# def move(a_list): 
#     for i in a_list: 
#         if i == 0: 
#             a_list.append(i)
#     return a_list
# print(move(num))

# mr park's solution 1
def moveZeros(num): 
    temp = [0] * len(nums)
    i = 0 
    for num in nums: 
        if num != 0: 
            temp[i] = num 
            i += 1
    nums = temp

# mr park's solution 2
def moveZeros(nums): 
    zero_ i = 0
    for i in range(len(nums)): 
        if num[i] != 0: 
            nums[i], nums[zero_i] = nums[zero_i], nums[i]
            zero_i += 1
    reutrn nums #unnecessary

# importance of this lesson 
# 1. sometimes you want a list filled with placeholders (learned from the second solution) 
# 2. sometimes you can have 2 pointers
# 3. remember complexity 