Matrices have a wide range of applications in programming: they're used for digital image processing, graph representation and algorithms on a graph, graphic effects, applied math, statistics, and much more.

Since matrices are tables of numbers, they are usually presented in code as 2D-arrays. In this project, you will learn how to read and output matrices, do operations on them, and compute the determinant of a square matrix. At first, you will work with matrices with integer elements, and later the elements will be floating-point numbers.
#  Description

Let’s start with matrix addition.

For two matrices to be added, they must have an equal number of rows and columns. The sum of matrices ![alt](https://latex.codecogs.com/svg.latex?A) and ![alt](https://latex.codecogs.com/svg.latex?B) will be a matrix with the same number of rows and columns as ![alt](https://latex.codecogs.com/svg.latex?A) or ![alt](https://latex.codecogs.com/svg.latex?B). The sum of ![alt](https://latex.codecogs.com/svg.latex?A) and ![alt](https://latex.codecogs.com/svg.latex?B), denoted ![alt](https://latex.codecogs.com/svg.latex?A) + ![alt](https://latex.codecogs.com/svg.latex?B) or ![alt](https://latex.codecogs.com/svg.latex?B) + ![alt](https://latex.codecogs.com/svg.latex?A), is computed by adding the corresponding elements of ![alt](https://latex.codecogs.com/svg.latex?A) and ![alt](https://latex.codecogs.com/svg.latex?B): ![alt](https://latex.codecogs.com/svg.latex?(A%20+%20B)_{n,m}%20=%20A_{n,%20m}%20+%20B_{n,%20m}). Notice that ![alt](https://latex.codecogs.com/svg.latex?n) in the index ![alt](https://latex.codecogs.com/svg.latex?_{n,m}) represents the row and ![alt](https://latex.codecogs.com/svg.latex?m) represents the column.

Here is a simple example with numbers:

![alt](https://latex.codecogs.com/svg.latex?\begin{pmatrix}%202%20&%204%20&5%20&%206%20\\%206%20&%206%20&7%20&%208%20\\%205%20&%200%20&0%20&%201%20\\%208%20&%208%20&2%20&%209%20\\%20\end{pmatrix}%20+\begin{pmatrix}%207%20&%207%20&0%20&%201%20\\%209%20&%209%20&9%20&%202%20\\%205%20&%204%20&3%20&%2012%20\\%200%20&%206%20&5%20&%206%20\\%20\end{pmatrix}%20=%20\begin{pmatrix}%202+7%20&%204+7%20&5+0%20&%206+1%20\\%206+9%20&%206+9%20&7+9%20&%208+2%20\\%205+5%20&%200+4%20&0+3%20&%201+12%20\\%208+0%20&%208+6%20&2+5%20&%209+6%20\\%20\end{pmatrix})
#  Objectives

In this stage, you should write a program that:

1.    Reads matrix A A A from the input.
2.    Reads matrix B B B from the input.
3.    Outputs their sum if it is possible to add them. Otherwise, it should output the ERROR message.

Each matrix in the input is given in the following way: the first line contains the number of rows nnn and the number of columns mmm. Then nnn lines follow, each containing mmm integers representing one row of the matrix.

Output the result in the same way but don't print the dimensions of the matrix.
#  Examples

Example 1:

Input:

    4 5
    1 2 3 4 5
    3 2 3 2 1
    8 0 9 9 1
    1 3 4 5 6
    4 5
    1 1 4 4 5
    4 4 5 7 8
    1 2 3 9 8
    1 0 0 0 1

Output:

    2 3 7 8 10
    7 6 8 9 9
    9 2 12 18 9
    2 3 4 5 7

Example 2:

Input:

    2 3
    1 4 5
    4 5 5
    4 5
    0 1 0 4 5
    1 7 8 9 4
    1 2 3 5 6
    1 3 4 3 8

Output:

    ERROR