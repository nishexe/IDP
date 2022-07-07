def get_row(matrix):
    for x in range(len(matrix)):
        print(matrix[x])

def get_col(matrix):
        for y in range(len(matrix[0])):
            print([matrix[i][y] for i in range(len(matrix)) ])
def main():
    matrix = [[1,2,3],[4,5,6]]
    get_row(matrix)
    get_col(matrix)

if __name__ == "__main__":
    main()