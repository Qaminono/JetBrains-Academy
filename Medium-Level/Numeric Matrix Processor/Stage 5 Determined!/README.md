#  Description

In this stage, you should write a program that calculates a determinant of a matrix. You can check out some [videos about linear algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) to understand the essence of the determinant and why it is important. To see how to calculate the determinant of any square matrix, watch a video about [minors and cofactors](https://www.youtube.com/watch?v=KMKd993vG9Q) and [computing the nxn determinant](https://www.youtube.com/watch?v=H9BWRYJNIv4). Also, here's [nice graphic explanation](https://www.mathsisfun.com/algebra/matrix-determinant.html) on minors and cofactors.

A determinant is a single number that can be computed from the elements of a square matrix. There is a classical way to find the determinant of a matrix with an order < 3.

A determinant of a 2-order matrix is equal to the difference between the product of elements on the main diagonal and the product of elements on the side diagonal:

![](https://i.gyazo.com/c2ec3a45ac1cdd126f01e0da78a9eca7.png)

Now let's move on to the minor and the cofactor of a matrix.

![](https://latex.codecogs.com/svg.latex?Minor_{(i,%20j)}) of a matrix is the determinant of the submatrix we get from the remaining elements after removing the i row and j column from this matrix.

Below is an example of Minor(2,2)​ for matrix ![](https://latex.codecogs.com/svg.latex?A_{3%20x%203}):

![](https://i.gyazo.com/31b294d5c9181aa0da98cdb240295819.png)

![](https://latex.codecogs.com/svg.latex?Cofactor_{(i,%20j)} )​ of a matrix is the corresponding ![](https://latex.codecogs.com/svg.latex?Minor_{(i,%20j)}) multiplied by ![](https://latex.codecogs.com/svg.latex?(-1)^{i+j}). Notice that the cofactor is always preceded by a positive + or negative − sign.

We often need to find the determinant of a matrix of the order greater than 2. In this case, we have to use expansion by rows or columns where the determinant is equal to a sum of a single row or a single column multiplied by the cofactors of the elements in the corresponding row or column. To do this, you should use a recursive method.

Below is an example of computing the determinant of a matrix of order 4 by first-row expansion, where ccc stands for the Cofactor:

![](https://i.gyazo.com/be709572081188c0755ec9066d72c27a.png)

#  Objectives

In this stage, your program should support calculating the determinant of a matrix. Refer to the example to see how it should be implemented.
#  Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    0. Exit
    Your choice: > 5
    Enter matrix size: > 3 3
    Enter matrix:
    > 1 7 7
    > 6 6 4
    > 4 2 1
    The result is:
    -16
    
    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    0. Exit
    Your choice: > 5
    Enter matrix size: > 5 5
    Enter matrix:
    > 1 2 3 4 5
    > 4 5 6 4 3
    > 0 0 0 1 5
    > 1 3 9 8 7
    > 5 8 4 7 11
    The result is:
    191
    
    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    0. Exit
    Your choice: > 0