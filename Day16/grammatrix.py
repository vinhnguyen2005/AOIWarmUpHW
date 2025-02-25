import numpy as np
def compute_gram_matrix(feature_map: np.ndarray) -> np.ndarray:
    C, H, W = feature_map.shape
    
    F = feature_map.reshape(C, H * W)
    print(F.shape)
    K = np.dot(F, F.T)
    G = K / (H*W)
    return G

def compute_similarity(gram1 : np.ndarray, gram2 : np.ndarray) -> float:
    return np.sum((gram1 * gram2)) / np.sqrt(np.sum(gram1 ** 2) * np.sum(gram2 ** 2))
    
    
feature_map1 = np . array ([
[[1 , 2] , [3 , 4]] ,
[[5 , 6] , [7 , 8]] ,
[[9 , 10] , [11 , 12]]
])

feature_map2 = np . array ([
[[2 , 4] , [6 , 8]] ,
[[1 , 3] , [5 , 7]] ,
[[0 , 2] , [4 , 6]]
])

gram_matrix1 = compute_gram_matrix (feature_map1)
gram_matrix2 = compute_gram_matrix (feature_map2)
similarity = compute_similarity (gram_matrix1 , gram_matrix2)
print(similarity)

    
