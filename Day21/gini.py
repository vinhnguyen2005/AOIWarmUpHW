# Lương Đủ điều kiện vay vốn?
# 50 Yes
# 20 No
# 30 No
# 70 Yes
# 40 No
# 60 Yes

import numpy as np

def split_data(data, threshold=45):
    left, right = [], []
    for row in data:
        if row[0] < threshold: 
            left.append(row)
        else:
            right.append(row)
    return left, right

def gini(groups, classes):
    total_samples = sum(len(group) for group in groups)
    gini_score = 0.0

    for group in groups:
        size = len(group)
        if size == 0:
            continue  

        score = 0.0
        for c in classes:
            prob = sum(1 for row in group if row[1] == c) / size
            score += prob ** 2
        
        gini_score += (1 - score) * (size / total_samples)

    return gini_score

data_set = [[50, 'Yes'], [20, 'No'], [30, 'No'], [70, 'Yes'], [40, 'No'], [60, 'Yes']]
classes = ['Yes', 'No']
groups = split_data(data_set)
gini_score = gini(groups, classes)
print('Gini index: %.3f' % gini_score)

# Steps
# gini_index
# solit_data
# get_best_split
# build_tree
# printtree

#Bai 2

# Thời tiết	Nhiệt độ	Gió	Đi gặp NY?
# Sunny	High	Weak	No
# Sunny	Medium	Strong	Yes
# Rainy	Low	Weak	Yes
# Cloudy	High	Strong	No
# Rainy	Medium	Weak	Yes
# Sunny	Low	Strong	Yes
# Cloudy	Medium	Weak	No
class DecisionTree:
    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.root = None

    def split_data(self, data, threshold):
        left, right = [], []
        for row in data:
            if row[0] < threshold:
                left.append(row)
            else:
                right.append(row)
        return left, right
    
    def gini(self, groups, classes):
        total_samples = sum(len(group) for group in groups)
        gini_score = 0.0

        for group in groups:
            size = len(group)
            if size == 0:
                continue  

            score = 0.0
            for c in classes:
                prob = sum(1 for row in group if row[1] == c) / size
                score += prob ** 2
            
            gini_score += (1 - score) * (size / total_samples)

        return gini_score

    def get_best_split(self, data):
        best_gini = float('inf')
        best_threshold = None
        best_groups = None
        best_score = None
        classes = list(set(row[-1] for row in data))
        
        
        