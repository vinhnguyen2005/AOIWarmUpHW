import numpy as np

#Cau 1
lst_data = np.arange(2, 13, 2)
print("Cau 1:", ", ".join(map(str, lst_data.tolist())))

#Cau 2
new_lst_data = [x for x in lst_data if x % 3 != 0]
print("Cau 2:", ", ".join(map(str, new_lst_data)))

#Cau 3
for i in range(1, 4):
    new_lst_data.append(i)

temp_list = [8, 7, 6]
for i in temp_list:
    new_lst_data.insert(3, i)
print("Cau 3:", ", ".join(map(str, new_lst_data)))

#Cau 4
for i in range(0, len(new_lst_data)):
    if new_lst_data[i] % 2 == 0 or new_lst_data[i] % 5 == 0:
        new_lst_data[i] = 0
print("Cau 4:", ", ".join(map(str, new_lst_data)))
