dimensions_a = [int(num) for num in input().split(" ")]
a = [[int(num) for num in input().split(" ")] for _ in range(dimensions_a[0])]
multiplier = int(input())
for n in range(dimensions_a[0]):
    for m in range(dimensions_a[1]):
        a[n][m] = str(a[n][m] * multiplier)
print("\n".join([" ".join(row) for row in a]))
