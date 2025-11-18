#perfect number function

def is_perfect (num):
    divider = 1
    total = 0
    while divider < num:
        if num % divider == 0:
            total += divider 
        divider += 1
    return total == num
# end of is_perfect()
num = 1
while number <= 1000000:
    if is_perfect(num):
        print(f"{num} is perfect.")
    num += 1



