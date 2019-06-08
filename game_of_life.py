def print_matrix(matrix):
    for row in matrix:
        print(row)

def next_generation(matrix):
    new_generation = [[0 for col in matrix] for row in matrix]
    length = len(new_generation)
    for i in range(length):
        for j in range(length):
            new_generation[i][j] = live_or_die(matrix, i, j)
    return new_generation

def live_or_die(matrix, i, j):
    living_neighbors = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            row = x if x < len(matrix) else len(matrix) - x
            col = y if y < len(matrix) else len(matrix) - y
            if x == i and y == j:
                continue
            if(matrix[row][col] == 1):
                living_neighbors += 1
    if(matrix[i][j] == 1):
        if(living_neighbors >= 2 and living_neighbors <= 3):
            return 1
    else:
        if living_neighbors == 3:
            return 1
    return 0

matrix = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


initial_matrix = matrix

for i in range(85):
    print("Generation " + str(i) + " ================")
    print_matrix(initial_matrix)
    new_matrix = next_generation(initial_matrix)
    initial_matrix = new_matrix
