import numpy as np


def get_median(data):
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        return data[n // 2]


def get_iqr(data):
    q1 = get_median(data[: len(data) // 2])
    q3 = get_median(data[len(data) // 2 :])
    iqr = q3 - q1
    return q1, q3, iqr


def get_outliers(min, max, data):
    outliers = []
    for value in data:
        if value < min or value > max:
            outliers.append(value)
    return outliers


# Bai 1
print("Bài 1:")
data = np.array([3, 7, 8, 5, 12, 14, 21, 13, 18])
sorted_data = np.sort(data)
q1, q3, iqr = get_iqr(sorted_data)
print(f"Q1 = {q1}, Q3 = {q3}, IQR = {iqr}")

# Bai 2
print("Bài 2:")
data = np.array([3, 5, 7, 8, 12, 13, 14, 18, 21, 100])
sorted_data = np.sort(data)
q1, q3, iqr = get_iqr(sorted_data)
print(f"Q1 = {q1}, Q3 = {q3}, IQR = {iqr}")
min = q1 - 1.5 * iqr
max = q3 + 1.5 * iqr
outliers = get_outliers(min, max, sorted_data)
outliers = [int(x) for x in outliers]
print(f"Outliers = {[x for x in outliers]}")

# Bai 3
print("Bài 3:")
import pandas as pd

df = pd.DataFrame({"score": [55, 61, 70, 65, 68, 90, 91, 94, 300, 58]})
arr = df["score"].to_numpy()
sorted_data = np.sort(arr)
q1, q3, iqr = get_iqr(sorted_data)
print(f"Q1 = {q1}, Q3 = {q3}, IQR = {iqr}")
min = q1 - 1.5 * iqr
max = q3 + 1.5 * iqr
outliers = get_outliers(min, max, sorted_data)
outliers = [int(x) for x in outliers]
print(f"Outliers = {[x for x in outliers]}")
new_df = df[~df["score"].isin(outliers)]
print(f"New DataFrame :\n{new_df}")


