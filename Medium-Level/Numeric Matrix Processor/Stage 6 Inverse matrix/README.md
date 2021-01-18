#  Description

In this stage, you should find the inverse of a matrix.

The inverse matrix is the matrix whose product with the original matrix is equal to the identity matrix.

![](https://latex.codecogs.com/svg.latex?A%20\times%20A^{-1}%20=%20A^{-1}%20\times%20A%20=%20I)

Watch a video about [the inverse of a matrix](https://www.youtube.com/watch?v=AMLUikdDQGk) to get the basic idea. To get a deeper understanding, check out the [3Blue1Brown channel](https://www.youtube.com/watch?v=uQhTuRlWMxw&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=7).

The identity matrix is a matrix where all elements of the main diagonal are ones, and other elements are zeros. Here is an example of a 4,4 identity matrix:

![](https://i.gyazo.com/8e5b9cbdc9233b8aad1d8428c7afd60f.png)

The inverse of a matrix can be found using this formula:

![](https://latex.codecogs.com/svg.latex?A^{-1}%20=%20\dfrac{1}{det(A)}%20\times%20C^T)

As you can see, it contains a lot of operations you implemented in the previous stages: finding cofactors of all the elements of the matrix, transposition of the matrix, finding the determinant of a matrix, and multiplication of a matrix by a constant.

![](https://latex.codecogs.com/svg.latex?det(A)) is the determinant of matrix ![](https://latex.codecogs.com/svg.latex?A), and ![](https://latex.codecogs.com/svg.latex?C^T) is the matrix consisting of cofactors of all elements of the matrix ![](https://latex.codecogs.com/svg.latex?A) transposed along the main diagonal. The inverse matrix can’t be found if ![](https://latex.codecogs.com/svg.latex?det(A)) equals zero. You can look up a calculation example.
#  Objectives

In this stage, your program should support finding the inverse of a matrix. Refer to the example to see how it should be implemented.

Note that in some cases the inverse of a matrix does not exist. In such cases, your program should output a warning message.
Additional improvements

Although it's not required in this stage and we won't check, you can implement a method that prints a matrix in a readable way so that every column is correctly aligned and all elements are rounded to a fixed number of digits.
#  Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    6. Inverse matrix
    0. Exit
    Your choice: > 6
    Enter matrix size: > 3 3
    Enter matrix:
    > 2 -1 0
    > 0 1 2
    > 1 1 0
    The result is:
     0.33   0  0.33
    -0.33   0  0.66
     0.16 0.5 -0.33
    
    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    6. Inverse matrix
    0. Exit
    Your choice: > 6
    Enter matrix size: > 2 2
    Enter matrix:
    > 2 1
    > 4 2
    This matrix doesn't have an inverse.
    
    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    6. Inverse matrix
    0. Exit
    Your choice: > 0