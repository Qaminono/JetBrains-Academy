from copy import deepcopy


def adding():
    print("Enter size of first matrix: ", end="")
    dimensions_a = [int(num) for num in input().split(" ")]
    print("Enter first matrix: ")
    a = [[float(num) for num in input().split(" ")] for _ in range(dimensions_a[0])]
    print("Enter size of second matrix: ", end="")
    dimensions_b = [int(num) for num in input().split(" ")]
    print("Enter second matrix: ")
    b = [[float(num) for num in input().split(" ")] for _ in range(dimensions_b[0])]
    if dimensions_a == dimensions_b:
        c = [[0 for _ in range(dimensions_a[1])] for _ in range(dimensions_a[0])]
        str_c = [["0" for _ in range(dimensions_a[1])] for _ in range(dimensions_a[0])]
        for n in range(dimensions_a[0]):
            for m in range(dimensions_a[1]):
                c[n][m] = a[n][m] + b[n][m]
                str_c[n][m] = str(c[n][m])
        return "The result is:\n" + "\n".join([" ".join(row) for row in str_c])
    else:
        return "The operation cannot be performed."


def multiplication_by_constant():
    dimensions = [int(num) for num in input().split(" ")]
    matrix = [[float(num) for num in input().split(" ")] for _ in range(dimensions[0])]
    constant = float(input())
    return "The result is:\n" + \
           "\n".join([" ".join(row) for row in _multiplication_by_constant(constant, matrix, dimensions)])


def _multiplication_by_constant(constant, matrix, dimensions):
    for n in range(dimensions[0]):
        for m in range(dimensions[1]):
            matrix[n][m] = str(matrix[n][m] * constant)
    return matrix


def multiply_matrices():
    print("Enter size of first matrix: ", end="")
    dimensions_a = [int(num) for num in input().split(" ")]
    print("Enter first matrix: ")
    a = [[float(num) for num in input().split(" ")] for _ in range(dimensions_a[0])]
    print("Enter size of second matrix: ", end="")
    dimensions_b = [int(num) for num in input().split(" ")]
    print("Enter second matrix: ")
    b = [[float(num) for num in input().split(" ")] for _ in range(dimensions_b[0])]

    if dimensions_a[1] != dimensions_b[0]:
        return "The operation cannot be performed."
    c = [[0 for _ in range(dimensions_b[1])] for _ in range(dimensions_a[0])]
    str_c = [["0" for _ in range(dimensions_b[1])] for _ in range(dimensions_a[0])]
    rows_a = [row_a for row_a in a]
    columns_b = [[row_b[i] for row_b in b] for i in range(dimensions_b[1])]
    for n, row_a in enumerate(rows_a):
        for m, column_b in enumerate(columns_b):
            c[n][m] = sum([row_a[i] * column_b[i] for i in range(len(row_a))])
            str_c[n][m] = str(c[n][m])
    return "The result is:\n" + "\n".join([" ".join(row) for row in str_c])


def transpose_matrix():
    def main_diagonal():
        return [[row[i] for row in matrix] for i in range(dimensions[1])]

    def side_diagonal():
        return [[row[i] for row in matrix][::-1] for i in range(dimensions[1])][::-1]

    def vertical_line():
        return [row[::-1] for row in matrix]

    def horizontal_line():
        return matrix[::-1]

    commands = {"1": main_diagonal,
                "2": side_diagonal,
                "3": vertical_line,
                "4": horizontal_line}
    choice = input("1. Main diagonal\n"
                   "2. Side diagonal\n"
                   "3. Vertical line\n"
                   "4. Horizontal line\n"
                   "Your choice: ")
    print("Enter size of first matrix: ", end="")
    dimensions = [int(num) for num in input().split(" ")]
    print("Enter matrix: ")
    matrix = [[num for num in input().split(" ")] for _ in range(dimensions[0])]
    transposed_matrix = commands[choice]()
    return "The result is:\n" + "\n".join([" ".join(row) for row in transposed_matrix])


def determinate():
    print("Enter matrix size: ", end="")
    dimensions_a = [int(num) for num in input().split(" ")]
    print("Enter matrix: ")
    a = [[float(num) for num in input().split(" ")] for _ in range(dimensions_a[0])]
    return "The result is:\n" + str(_determinate(a))


def _determinate(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        del_column = 0
        determinant = 0
        cofactor = 1
        for i, a in enumerate(matrix[0]):
            minor = deepcopy(matrix)
            for row in minor:
                row.pop(i)
            minor = minor[1:]
            determinant += a * _determinate(minor) * cofactor
            cofactor *= -1
        return determinant


commands = {"1": adding,
            "2": multiplication_by_constant,
            "3": multiply_matrices,
            "4": transpose_matrix,
            "5": determinate}

while True:
    choice = input("1. Add matrices\n"
                   "2. Multiply matrix by a constant\n"
                   "3. Multiply matrices\n"
                   "4. Transpose matrix\n"
                   "5. Calculate a determinant\n"
                   "0. Exit\n"
                   "Your choice: \n")
    if choice == "0":
        break
    print(commands[choice]())
