import numpy as np

#Xac suat co ban
def calculate_probability ( event_occurrences , total_trials ) :
    return event_occurrences / total_trials

event_coccurrences = 5
total_trials = 20
propability = calculate_probability(event_coccurrences, total_trials)
print(f"Xac suat cua su kien xay ra {event_coccurrences} lan trong {total_trials} lan thu nghiem la: {propability}")

#Xac suat dieu kien
def conditional_probability ( event_occurrences , total_occurrences ) :
    return event_occurrences / total_occurrences
P_A_and_B = 0.2
P_A = 0.5
P_B_given_A = conditional_probability(P_A_and_B, P_A)
print(f"Xac suat cua B xay ra khi A xay ra la: {P_B_given_A}")

#Covariance
def calculate_covariance ( x , y ) :
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    return np.sum((x - x_mean) * (y - y_mean)) / (len(x) - 1)

X = [2 , 4 , 6 , 8 , 10]
Y = [1 , 3 , 5 , 7 , 9]
covariance = calculate_covariance(X, Y)
print(f"Covariance cua X va Y la: {covariance}")

def calculate_correlation ( x , y ) :
    x_std = np.std(x)
    y_std = np.std(y)
    return calculate_covariance(x, y) / (x_std * y_std) if (x_std * y_std) != 0 else 0

print(f"Correlation cua X va Y la: {calculate_correlation(X, Y)}")

