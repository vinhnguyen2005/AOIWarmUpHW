# Compute median
def median(lst_data):
    median = 0
    length = len(lst_data)
    if length % 2 == 0:
        median =  (lst_data[int(length/2)] + lst_data[int(length/2) + 1]) / 2
    else:
        median = lst_data[int(length/2) + 1]
    return median
    

lst_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
new_odd_list = [x for x in lst_data if x % 2 == 1]
new_odd_list.sort(reverse=True)
print('Cau 1:', lst_data)
print('Cau 2: Median: ',median(lst_data))
print('Cau 3: ', new_odd_list)

# Compute mean 
def conclude_mean_median(mean, median):
    if mean > median:
        return f"Mean > Median: {mean} > {median}"
    elif mean < median:
        return f"Mean < Median: {mean} < {median}"
    else:
        return f"Mean = Median: {mean} = {median}"


def mean(lst_data):
    return sum(lst_data) / len(lst_data)

odd_data = [x for x in lst_data if x % 2 == 1]
even_data = [x for x in lst_data if x % 2 == 0]
odd_mean = mean(odd_data)
even_mean = mean(even_data)
print('Cau 2: Mean Le: ', odd_mean, '- Mean Chan: ', even_mean)
print('Cau 3: ', conclude_mean_median(mean(lst_data), median(lst_data)) )



