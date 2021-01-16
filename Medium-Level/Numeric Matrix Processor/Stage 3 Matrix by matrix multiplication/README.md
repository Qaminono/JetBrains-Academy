# Description

The next stage is the multiplication of matrices. This operation is a little more complex because it’s not enough to simply multiply the corresponding elements.

Unlike with addition, the sizes of the matrices can be different: the only restriction is that the number of columns in the first matrix should equal the number of rows for the second matrix. Check out a comprehensive [video by 3Blue1Brown](https://youtube.com/watch?v=XkY2DOUCWMU&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=5) about matrix multiplication.

The multiplication of ![](https://latex.codecogs.com/svg.latex?A) matrix with ![](https://latex.codecogs.com/svg.latex?n) rows and ![](https://latex.codecogs.com/svg.latex?m) columns and ![](https://latex.codecogs.com/svg.latex?B) matrix with ![](https://latex.codecogs.com/svg.latex?m) rows and ![](https://latex.codecogs.com/svg.latex?k) columns is ![](https://latex.codecogs.com/svg.latex?C_{n%20,%20k}%20=%20A_{n%20,%20m}%20\times%20B_{m,%20k}).

The resulting matrix has ![](https://latex.codecogs.com/svg.latex?n) rows and ![](https://latex.codecogs.com/svg.latex?k) columns, where every element is a sum of the multiplication of ![](https://latex.codecogs.com/svg.latex?m) elements across the rows of matrix ![](https://latex.codecogs.com/svg.latex?A) by ![](https://latex.codecogs.com/svg.latex?m) elements down the columns of matrix ![](https://latex.codecogs.com/svg.latex?B).

Take a look at this example of matrix multiplication:

![](https://i.gyazo.com/52104ba3f5ac45075fecaa983126b74b.png)

#  Objectives

In this stage, you should write a program that can do all operations on matrices that you've learned.

Write a program that does the following:

1.    Prints a menu consisting of 4 options. The example shows what the menu should look like.
2.    Reads the user's choice.
3.    Reads all data (matrices, constants) needed to perform the chosen operation. The example shows the input format in each case.
4.    Calculates the result and outputs it. The example shows how your output should look like.
5.    Repeats all these steps.

The program should keep repeating this until the "Exit" option is chosen.

If some operation cannot be performed, output a warning message.

Also, you should support floating-point numbers.
#  Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    0. Exit
    Your choice: > 1
    Enter size of first matrix: > 4 5
    Enter first matrix:
    > 1 2 3 4 5
    > 3 2 3 2 1
    > 8 0 9 9 1
    > 1 3 4 5 6
    Enter size of second matrix: > 4 5
    Enter second matrix:
    > 1 1 4 4 5
    > 4 4 5 7 8
    > 1 2 3 9 8
    > 1 0 0 0 1
    The result is:
    2 3 7 8 10
    7 6 8 9 9
    9 2 12 18 9
    2 3 4 5 7
    
    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    0. Exit
    Your choice: > 2
    Enter size of matrix: > 2 2
    Enter matrix:
    > 1.5 7.0
    > 6.0 5.0
    Enter constant: > 0.5
    The result is:
    0.75 3.5
    3.0 2.5
    
    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    0. Exit
    Your choice: > 3
    Enter size of first matrix: > 3 3
    Enter first matrix:
    > 1 7 7
    > 6 6 4
    > 4 2 1
    Enter size of second matrix: > 3 3
    Enter second matrix:
    > 3 2 4
    > 5 5 9
    > 8 0 10
    The result is:
    94 37 137
    80 42 118
    30 18 44
    
    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    0. Exit
    Your choice: > 1
    Enter size of first matrix: > 2 2
    Enter first matrix:
    > 1 2
    > 3 2
    Enter size of second matrix: > 1 1
    Enter second matrix:
    > 1
    The operation cannot be performed.
    
    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    0. Exit
    Your choice: > 0