matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def print_matrix(matrix=matrix):
    for row in matrix:
        print(row)

def rotateMatrix(matrix):
    N = len(matrix[0])

    return [[matrix[N - 1 - y][x] for y in range(N)] for x in range(N)]

def main():
    print_matrix()
    print("Rotated matrix:")
    print_matrix(rotateMatrix(matrix))

if __name__ == "__main__":
    main()
