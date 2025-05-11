def find_prompt_with_keyword(prompt, keyword):
    for i, line in enumerate(prompt.split("\n")):
        if keyword in line:
            return i
    return -1


prompts = [
    " Generate a report for patient X.",
    " Summarize the input text .",
    " Suggest a diagnosis based on symptoms .",
    " Translate this to French .",
]

print("Line with keyword 'patient':", find_prompt_with_keyword(prompts[0], "patient"))

def find_first_unlabeled ( images ):
    for i, image in enumerate(images):
        if image['label'] is None:
            return i
    return -1
    
images = [
    {'name': 'img1.png', 'label': 'benign'},
    {'name': 'img2.png', 'label': None},
    {'name': 'img3.png', 'label': 'malignant'}
]

print("First unlabeled image index:", find_first_unlabeled(images))

def sort_by_blurriness(images):
    for i in range(len(images)):
        swapped = False
        for j in range(0, len(images)-i-1):
            if images[j]['blurriness'] < images[j+1]['blurriness']:
                images[j], images[j+1] = images[j+1], images[j]
                swapped = True
        if not swapped:
            break
        
        
image_data = [
    {'name': 'img1', 'blurriness': 0.8},
    {'name': 'img2', 'blurriness': 0.3},
    {'name': 'img3', 'blurriness': 0.5}
]
sort_by_blurriness ( image_data )
print([image_data['name'] for image_data in image_data])


def sort_models_by_accuracy(models, accuracies):
    model_accuracy = list(zip(models, accuracies))
    for i in range(len(model_accuracy)):
        swapped = False
        for j in range(0, len(model_accuracy)-i-1):
            if model_accuracy[j][1] < model_accuracy[j+1][1]:
                model_accuracy[j], model_accuracy[j+1] = model_accuracy[j+1], model_accuracy[j]
                swapped = True
        if not swapped:
            break
    sorted_models = [model[0] for model in model_accuracy]
    return sorted_models

models = [" ModelA ", " ModelB ", " ModelC "]
accuracies = [0.89, 0.93, 0.91]
print(sort_models_by_accuracy(models, accuracies))

def bubble_sort_with_count(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                count += 1
                swapped = True
        if not swapped:
            break
    return count

losses = [0.4, 0.3, 0.5, 0.2]
print(bubble_sort_with_count(losses))  


def binary_search_threshold(f1_scores, threshold):
    left , right = 0 , len ( f1_scores ) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if f1_scores[mid][0] == threshold:
            return f1_scores[mid][1]
        elif f1_scores[mid][0] < threshold:
            left = mid + 1
        else:
            right = mid - 1


f1_scores = [(0.1 , 0.6) , (0.2 , 0.65) , (0.3 , 0.7) , (0.4 , 0.68) ]
print(binary_search_threshold(f1_scores, 0.3))

def exists_similar_image(similar_images, threshold):
    left = 0
    right = len(similar_images) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if similar_images[mid] == threshold:
            return True
        elif similar_images[mid] < threshold:
            left = mid + 1
        else:
            right = mid - 1
    return False

sims = [0.95 , 0.89 , 0.85 , 0.80 , 0.75]
print(exists_similar_image(sims, 0.85))    