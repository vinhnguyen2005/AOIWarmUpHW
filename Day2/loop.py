import math 
# Tính lãi suất tiền gửi ngân hàng
def compute_interest(money, period):
    daily_rate = 1 / period

    for _ in range(period):
        money *= (1 + daily_rate)

    return round(money, 3)

print("Test case:", compute_interest(1, 12)) 

#  Thuật toán sàng số nguyên tố Eratosthenes
def is_prime_eratosthenes(n):
    if n <= 1:
        return False
    prime = [True] * (n+1)
    prime[0] = False
    prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i] == True:
            for j in range(i*i, n+1, i):
                prime[j] = False

    return prime[n]

n1 = 50
n2 = 7
print("Test case with n = 50:", is_prime_eratosthenes(n1))
print("Test case with n = 7:", is_prime_eratosthenes(n2))