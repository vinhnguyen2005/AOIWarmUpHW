import numpy as np
import math

documents = [
    "Tôi thích học AI",
    "AI là trí tuệ nhân tạo",
    "AGI là siêu trí tuệ nhân tạo"
]

def preprocess(text):
    return text.split()

def create_vocab(docs):
    processed_docs = [preprocess(doc) for doc in docs]
    vocab = set(word for doc in processed_docs for word in doc)
    return vocab
    
def compute_tf(doc, vocab):
    tf = {}
    doc_words = preprocess(doc)
    for word in vocab:
        tf[word] = doc_words.count(word) / len(doc_words)
    return tf

def compute_idf(docs):
    vocab = create_vocab(docs)
    idf = {}
    num_docs = len(docs)
    
    for word in vocab:
        doc_count = sum(1 for doc in docs if word in preprocess(doc)) 
        idf[word] = math.log(num_docs / (1 + doc_count)) 
    
    return idf

def compute_tf_idf(docs):
    vocab = create_vocab(docs)
    idf = compute_idf(docs)
    
    tf_idf = []
    for doc in docs:
        tf = compute_tf(doc, vocab)
        tf_idf.append({word: tf[word] * idf[word] for word in vocab})  
        
    return tf_idf
tf_idf_values = compute_tf_idf(documents)

print(create_vocab(documents))
# Hiển thị kết quả
for i, doc_tfidf in enumerate(tf_idf_values):
    print(f"Tài liệu {i + 1}:")
    for word, score in doc_tfidf.items():
        print(f"{word}: {score:.4f}")
    print()