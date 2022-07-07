def make_matrix(row,col):
    matrix = []
    for x in range(row):
        temp = []
        for y in range(col):
            temp.append(x+y)
        matrix.append(temp)
    return matrix
print(make_matrix(2,2))