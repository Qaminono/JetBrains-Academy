dimensions_a = [int(num) for num in input().split(" ")]
a = [[int(num) for num in input().split(" ")] for _ in range(dimensions_a[0])]
dimensions_b = [int(num) for num in input().split(" ")]
b = [[int(num) for num in input().split(" ")] for _ in range(dimensions_b[0])]
if dimensions_a == dimensions_b:
    c = [[0 for _ in range(dimensions_a[1])] for _ in range(dimensions_a[0])]
    str_c = [["0" for _ in range(dimensions_a[1])] for _ in range(dimensions_a[0])]
    for n in range(dimensions_a[0]):
        for m in range(dimensions_a[1]):
            c[n][m] = a[n][m] + b[n][m]
            str_c[n][m] = str(c[n][m])
    print("\n".join([" ".join(row) for row in str_c]))
else:
    print("ERROR")
