
import numpy as np

#Cau 1
start = 1
end = 10
lst_data = np.arange(start, end + 1, 1)
print("Cau 1:", ", ".join(map(str, lst_data.tolist())))

#Cau 2
count = 0
new_lst_data = []
for var in lst_data:
    new_lst_data.append(int(var))
    count += 1
    if(count >= 5):
        break
print("Cau 2:", ", ".join(map(str, new_lst_data)))

#Cau 3
odd_array = []
for i in lst_data:
    if i % 2 != 0:
        odd_array.append(i)
print("Cau 3:", ", ".join(map(str, odd_array)))

#Cau 4
sum = 0
for x in lst_data:
    sum += x
print("Cau 4:", sum)
