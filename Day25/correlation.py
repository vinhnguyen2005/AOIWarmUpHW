import numpy as np
def pearson_correlation(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(len(x)))
    denominator = np.sqrt(sum((x[i] - x_mean) ** 2 for i in range(len(x))) * sum((y[i] - y_mean) ** 2 for i in range(len(y))))
    if denominator == 0:
        return 0
    return numerator / denominator

x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y = np.array([12, 25, 28, 35, 48, 55, 70, 78, 90, 102])

print(f"Pearson correlation: {pearson_correlation(x, y)}")

#Scatter plot
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.show()
#Conclude
correlation = pearson_correlation(x, y)
if correlation > 0:
    print("Chi tiếu quảng cáo tăng khi doanh số bán hàng tăng")
elif correlation < 0:
    print("Chi tiếu quảng cáo giảm khi doanh số bán hàng tăng")
else:
    print("Không có sự tương quan giữa chi tiếu quảng cáo và doanh số bán hàng")

#Bai 2
#Một quán cà phê muốn kiểm tra xem nhiệt độ ngoài trời có ảnh hưởng đến doanh số bán cà phê hay không
#X = [30, 28, 25, 30, 29, 27, 26, 24, 23, 22] (nhiệt độ, độ C).
#Y = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95] (số ly cà phê bán được).

x = np.array([30, 28, 25, 30, 29, 27, 26, 24, 23, 22])
y = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

print(f"Pearson correlation: {pearson_correlation(x, y)}")

plt.scatter(x, y)
plt.show()
correlation = pearson_correlation(x, y)
if correlation > 0:
    print("Doanh số bán cà phê tăng khi nhiệt độ tăng")
elif correlation < 0:
    print("Doanh số bán cà phê giảm khi nhiệt độ tăng")
else:
    print("Không có sự tương quan giữa doanh số bán cà phê và nhiệt độ")



    