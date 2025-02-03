def find_divisible_number(a):
    if a <= 0:
        return -1
    
    start_num = 101
    while True:
        if start_num % a == 0:
            return start_num
        start_num += 1

if find_divisible_number(5) == -1 or find_divisible_number(17) == -1:
    print("Invalid input")
else:
    print('Test Case with number 5:', find_divisible_number(5)) 
    print('Test Case with number 17:', find_divisible_number(17))