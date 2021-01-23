def determinant(x, matrix, dimensions):
    if dimensions == 1:
        return x * matrix
    else:
        deleted_column = 0
        cofactor = 1
        determ = 0
        for x in matrix[0]:
            if dimensions == 2:
                matrix_to_determ = matrix[1][1]
            else:
                matrix_to_determ = matrix[1:]
                for row in matrix_to_determ:
                    row.pop(deleted_column)
            elem = determinant(matrix[0][0], matrix_to_determ, dimensions - 1)
            determ += elem * cofactor
            cofactor *= -1
            deleted_column += 1
        return determ


matrix = [[1, -4],
          [-2, 5]]
print(determinant(matrix[0][0], matrix, 2))