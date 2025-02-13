import math
def create_position_matrix (seq_length , embed_size ) :
    positional_matrix = [[0 for _ in range(embed_size)] for _ in range(seq_length)]
    for pos in range(seq_length):
        for embed_dim in range(embed_size):
            if embed_dim % 2 == 0:
                positional_matrix[pos][embed_dim] = math.sin(pos / math.pow(10000, (2*embed_dim/embed_size)))
            if embed_dim % 2 == 1:
                positional_matrix[pos][embed_dim] = math.cos(pos / math.pow(10000, (2*embed_dim/embed_size))) 
    return positional_matrix  


seq_length = 10
embed_size = 16
position_matrix = create_position_matrix ( seq_length , embed_size )
print ( position_matrix )
