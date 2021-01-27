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
    dimensions_a = [int(num) for num in input().split(" ")]
    a = [[float(num) for num in input().split(" ")] for _ in range(dimensions_a[0])]
    multiplier = float(input())
    for n in range(dimensions_a[0]):
        for m in range(dimensions_a[1]):
            a[n][m] = str(a[n][m] * multiplier)
    return "The result is:\n" + "\n".join([" ".join(row) for row in a])


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


commands = {"1": adding,
            "2": multiplication_by_constant,
            "3": multiply_matrices,
            "0": lambda x: x - 1}

while True:
    choice = input("1. Add matrices\n"
                   "2. Multiply matrix by a constant\n"
                   "3. Multiply matrices\n"
                   "0. Exit\n"
                   "Your choice: \n")
    if choice == "0":
        break
    print(commands[choice]())
