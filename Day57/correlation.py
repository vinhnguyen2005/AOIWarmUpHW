import numpy as np

# Bai 1
print("Bài 1:")
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])


def calculate_correlation(x, y):
    n = len(x)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    covariance = np.sum((x - mean_x) * (y - mean_y)) / (n - 1)
    std_x = np.std(x, ddof=1)
    std_y = np.std(y, ddof=1)
    correlation = covariance / (std_x * std_y)
    return correlation

print("Hệ số tương quan giữa x và y:", calculate_correlation(x, y))

# Bai 2
print("Bài 2:")
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 8, 6, 4, 2])
print("Hệ số tương quan giữa x và y:", calculate_correlation(x, y))

# Bài 3
print("Bài 3:")
x = np.linspace(0, 10, 100)
y = np.sin(x)
print("Hệ số tương quan giữa x và y:", calculate_correlation(x, y))

# Bài 4
print("Bài 4:")
features = np.array([1.1, 1.9, 3.2, 4.5, 5.1])
labels = np.array([1.0, 2.0, 3.0, 4.1, 5.3])
print("Hệ số tương quan giữa features và labels:", calculate_correlation(features, labels))

# Bài 5
print("Bài 5:")
height = np.array([150, 160, 170, 180, 190])
weight = np.array([50, 60, 70, 80, 90])
print("Hệ số tương quan giữa chiều cao và cân nặng:", calculate_correlation(height, weight))

# Bài 6
embeda = np.array([0.3, 0.5, 0.7, 0.8])
embedb = np.array([0.9, 1.4, 2.1, 2.4])
print("Hệ số tương quan giữa embeda và embedb:", calculate_correlation(embeda, embedb))

# Bài 7
print("Bài 7:")
x = np.random.rand(100)
y = np.random.rand(100)
print("Hệ số tương quan giữa x và y:", calculate_correlation(x, y))

# Bài 8
print("Bài 8:")
x = np.arange(100)
y_clean = x
y_noisy = x + np.random.normal(0, 10, 100)
print("Hệ số tương quan giữa x và y_clean:", calculate_correlation(x, y_clean))
print("Hệ số tương quan giữa x và y_noisy:", calculate_correlation(x, y_noisy))

# Bài 9
print("Bài 9:")
temperature = np.array([22, 24, 23, 25, 26])
sales = np.array([100, 110, 105, 115, 120])
print("Hệ số tương quan giữa nhiệt độ và doanh số:", calculate_correlation(temperature, sales))

# Bài 10
print("Bài 10:")
doc1 = "deep learning for natural language processing"
doc2 = "transformer models improve language understanding"
doc3 = "convolutional neural networks for image classification"
query = "language models for text understanding"

def preprocess_text(text):
    return text.lower().split()

def create_corpus(docs):
    corpus = set(sorted(" ".join(docs).split()))
    return corpus

def calculate_tf(corpus, docs):
    tf = np.zeros((len(docs), len(corpus)))
    
    for i, doc in enumerate(docs):
        total_words = len(doc)
        for j, word in enumerate(corpus):
            tf[i, j] = doc.count(word) / total_words if total_words > 0 else 0
    
    return tf

def calculate_idf(corpus, docs):
    idf = np.zeros(len(corpus))
    
    for j, word in enumerate(corpus):
        doc_count = sum(1 for doc in docs if word in doc)
        idf[j] = np.log(len(docs) / (doc_count + 1)) if doc_count > 0 else 0
    
    return idf

def calculate_tfidf(tf, idf):
    return tf * idf

def find_vector(query, docs):
    corpus = create_corpus(docs + [query])
    tf = calculate_tf(corpus, docs + [query])
    idf = calculate_idf(corpus, docs + [query])
    tfidf = calculate_tfidf(tf, idf)
    return tfidf[-1], tfidf[:-1]

query_vector, doc_vectors = find_vector(query, [doc1, doc2, doc3])
coefficients = []
for doc_vector in doc_vectors:
    coefficients.append(calculate_correlation(query_vector, doc_vector))

print("Hệ số tương quan giữa truy vấn và các tài liệu:")
for i, coeff in enumerate(coefficients):
    print(f"Tài liệu {i + 1}: {coeff}")

    
    

    