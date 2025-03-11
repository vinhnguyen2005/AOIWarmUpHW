import numpy as np
import pandas as pd

# Dữ liệu bệnh nhân
data = pd.DataFrame({
    "Sốt": ["Cao", "Cao", "Cao", "Thấp", "Cao", "Thấp", "Thấp", "Cao", "Thấp", "Cao"],
    "Ho": ["Có", "Không", "Có", "Có", "Có", "Không", "Có", "Không", "Không", "Có"],
    "Đau họng": ["Có", "Có", "Không", "Có", "Có", "Có", "Không", "Có", "Không", "Có"],
    "Mệt mỏi": ["Có", "Không", "Có", "Có", "Không", "Không", "Có", "Có", "Không", "Có"],
    "Flu": ["Có", "Có", "Có", "Không", "Có", "Không", "Không", "Có", "Không", "Có"]
})

# Bệnh nhân mới
new_patient = {"Sốt": "Cao", "Ho": "Có", "Đau họng": "Có", "Mệt mỏi": "Không"}

P_Flu = data["Flu"].value_counts()["Có"]
P_noFlu = 1 - P_Flu

def conditional_prob ( feature , value , flu_status ):
    sum_flu = data["Flu"].value_counts()[flu_status]
    sum_value_flu = data[(data["Flu"] == flu_status) & (data[feature] == value)].shape[0]
    return sum_value_flu + 1/ sum_flu + data[feature].nunique()


P_X_Flu = 1
P_X_noFlu = 1

for feature, value in new_patient.items():
    P_X_Flu *= conditional_prob(feature, value, "Có")
    P_X_noFlu *= conditional_prob(feature, value, "Không")

numerator_flu = P_X_Flu * P_Flu
numerator_noFlu = P_X_noFlu * P_noFlu
denominator = numerator_flu + numerator_noFlu
P_Flu_X = numerator_flu / denominator
P_noFlu_X = numerator_noFlu / denominator

print("\nKết quả Naive Bayes:")
print(f"P(Flu = Có | X) = {P_Flu_X:.4f}")
print(f"P(Flu = Không | X) = {P_noFlu_X:.4f}")

print("\nKết luận:", "Bệnh nhân có khả năng bị cúm." if P_Flu_X > P_noFlu_X else "Bệnh nhân KHÔNG có khả năng bị cúm.")

    

