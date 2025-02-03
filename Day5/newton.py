def find_squared_root(a):
    if a < 0:
        return -1
    EPSILON = 0.001
    xn = a
    while True:
        x_next = xn - ((xn**2 - a) / (2*xn))
        if abs(x_next - xn) < EPSILON:
            return x_next
        xn = x_next

if find_squared_root(2) == -1 or find_squared_root(3) == -1:
    print("Error: Negative number")
else:
    print('Test Case with 2:', find_squared_root(2)) 
    print('Test Case with 3:', find_squared_root(3))
