import random

def random_number_with_condition(total):
    random.seed(0)
    count = 0
    while True:
        count += 1
        random_number_a = random.randint(1, 20)
        random_number_b = random.randint(1, 20)
        if random_number_a + random_number_b == total:
            break

    return count
        
print('Test case with total = 35:', random_number_with_condition(35))


