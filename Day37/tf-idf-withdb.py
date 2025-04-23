import numpy as np
import mysql.connector
import math
import seaborn as sns
import matplotlib.pyplot as plt

sample_docs = [
    (
        "Bài luận 1",
        "Trí tuệ nhân tạo đang phát triển nhanh chóng và tác động lớn đến cuộc sống.",
    ),
    (
        "Bài luận 2",
        "Trí tuệ nhân tạo đang phát triển mạnh mẽ và ảnh hưởng nhiều đến đời sống con người.",
    ),
    (
        "Bài luận 3",
        "Trí tuệ nhân tạo rất mạnh mẽ và ảnh hưởng nhiều đến đời sống con người.",
    ),
    (
        "Bài luận 4",
        "Deep Learning đã mang lại những bước tiến vượt bậc trong lĩnh vực xử lý ngôn ngữ tự nhiên.",
    ),
    (
        "Bài luận 5",
        "Robotics và tự động hóa đang thay đổi cách chúng ta làm việc trong các nhà máy.",
    ),
    (
        "Bài luận 6",
        "Internet of Things kết nối hàng tỷ thiết bị thông minh trên toàn cầu.",
    ),
    (
        "Bài luận 7",
        "Blockchain không chỉ dùng cho tiền điện tử mà còn nhiều ứng dụng khác.",
    ),
    (
        "Bài luận 8",
        "Cloud Computing giúp doanh nghiệp tiết kiệm chi phí và tăng hiệu quả.",
    ),
    ("Bài luận 9", "Bảo mật thông tin là thách thức lớn trong kỷ nguyên số."),
    ("Bài luận 10", "5G sẽ tạo ra cuộc cách mạng trong truyền thông di động."),
]


def preprocess_Text(text):
    if isinstance(text, list):
        text = " ".join(text)
    text = text.lower()
    text = "".join([char for char in text if char.isalnum() or char.isspace()])
    words = text.split()
    return words



def create_Corpus(docs):
    corpus = set()
    for doc in docs:
        words = preprocess_Text(doc)
        corpus.update(words)
    return sorted(corpus)


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


def find_cosine_similarity(vec1, vec2):
    numerator = np.dot(vec1, vec2)
    demominator = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return numerator / demominator if demominator != 0 else 0


def show_similarity_matrix(tfidf_matrix):
    similarity_matrix = np.zeros((tfidf_matrix.shape[0], tfidf_matrix.shape[0]))

    for i in range(tfidf_matrix.shape[0]):
        for j in range(tfidf_matrix.shape[0]):
            similarity_matrix[i, j] = find_cosine_similarity(
                tfidf_matrix[i], tfidf_matrix[j]
            )

    return similarity_matrix


def connect_mysql():
    return mysql.connector.connect(
        host="localhost", user="root", password="Vinh2005", database="plagiarism_checker"
    )

def insert_document(title, content):
    conn = connect_mysql()
    cursor = conn.cursor()
    sql = "INSERT INTO documents (title, content) VALUES (%s, %s)"
    cursor.execute(sql, (title, content))
    conn.commit()
    cursor.close()
    conn.close()
    return cursor.lastrowid

def insert_similarities(doc1_id, doc2_id, similarity):
    conn = connect_mysql()
    cursor = conn.cursor()
    sql = "INSERT INTO similarity_scores (doc1_id, doc2_id, similarity_score) VALUES (%s, %s, %s)"
    cursor.execute(sql, (doc1_id, doc2_id, similarity))
    conn.commit()
    cursor.close()
    conn.close()
    

def display_with_heatmap(similarity_matrix):
    sns.heatmap(similarity_matrix, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Cosine Similarity Heatmap")
    plt.xlabel("Documents")
    plt.ylabel("Documents")
    plt.show()
    
def display_similarity_matrix(similarity_matrix):
    print("Cosine Similarity Matrix:")
    for i in range(similarity_matrix.shape[0]):
        for j in range(similarity_matrix.shape[1]):
            print(f"{similarity_matrix[i][j]:.2f}", end="\t")
        print()
    display_with_heatmap(similarity_matrix)

def main():
    # Preprocess documents
    docs = [doc[1] for doc in sample_docs]
    preprocessed_docs = [preprocess_Text(doc) for doc in docs]

    # Create corpus
    corpus = create_Corpus(preprocessed_docs)

    # Calculate TF-IDF
    tf = calculate_tf(corpus, preprocessed_docs)
    idf = calculate_idf(corpus, preprocessed_docs)
    tfidf = calculate_tfidf(tf, idf)

    # Calculate cosine similarity
    similarity_matrix = show_similarity_matrix(tfidf)
    display_similarity_matrix(similarity_matrix)


    doc_ids = []
    for doc in sample_docs:
        doc_id = insert_document(doc[0], doc[1])
        doc_ids.append(doc_id)
        print(f"Inserted document: {doc[0]} with ID {doc_id}")

    # Insert similarities into MySQL using document IDs
    for i in range(len(sample_docs)):
        for j in range(i + 1, len(sample_docs)):
            insert_similarities(
                doc_ids[i], doc_ids[j], similarity_matrix[i][j]
            )
            print(
                f"Inserted similarity between document {doc_ids[i]} and {doc_ids[j]}"
            )
if __name__ == "__main__":
    main()