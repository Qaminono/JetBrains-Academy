#  Description

In this stage, you should implement matrix transposition. Matrix transposition is an operation in linear algebra that replaces rows with columns and returns a new matrix as a result. This is an operation on just a single matrix.

The main diagonal of a matrix is a line with elements from ![alt](https://latex.codecogs.com/svg.latex?a_{1,%201}) to ![](https://latex.codecogs.com/svg.latex?a_{n,n}):

![](https://i.gyazo.com/2079a2bdbf647aeae40cb5ef49aff43c.png)

The side diagonal of a matrix is a line from a1,na_{1, n} a1,n​ to an,1 a_{n, 1} an,1​:

![](https://i.gyazo.com/30965faf063c73dd58f7176f5c9648b4.png)

In math, there is only one type of matrix transposition: transposition along the main diagonal. In this stage, you should implement the other three types of transposition to practice your array skills. These four types are:

-    transposition along the main diagonal
-    transposition along the side diagonal
-    transposition along the vertical line
-    transposition along the horizontal line

Transposition along the main diagonal is shown below:

![](https://i.gyazo.com/3c353231f51f35a76ca7a9f0db7c6872.png)

Here is what transposition along the side diagonal looks like:

![](https://i.gyazo.com/8803bd46a76ac8704f3c4c2e5a74cf00.png)

The matrix below is transposed along the vertical line:

![](https://i.gyazo.com/7619dd95cede6f3cd87f3c8ad03fdfa2.png)

Finally, here is transposition along the horizontal line:

![](https://i.gyazo.com/aa518aa48d0e8159ef2d39879a092660.png)
#  Objectives

In this stage, you should add an option to transpose matrices. If the user chooses this option, your program should provide them with 4 types of transposition and ask them to choose one. Then it should read the matrix, transpose it, and output the result. Refer to the example to see the exact format.

Note that your program should still be able to do all operations on matrices that you've implemented in the previous stage.
#  Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    0. Exit
    Your choice: > 4
    
    1. Main diagonal
    2. Side diagonal
    3. Vertical line
    4. Horizontal line
    Your choice: > 1
    Enter matrix size: > 3 3
    Enter matrix:
    > 1 7 7
    > 6 6 4
    > 4 2 1
    The result is:
    1 6 4
    7 6 2
    7 4 1
    
    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    0. Exit
    Your choice: > 0