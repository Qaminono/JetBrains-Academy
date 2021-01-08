#  Description

Let's compute all the parameters of the loan. There are at least two kinds of loan: those with annuity payment and those with differentiated payment. In this stage, you are going to calculate only the annuity payment which is fixed during the whole loan term.

Here is the formula:

![alt](https://latex.codecogs.com/svg.latex?A_{ordinary\_annuity}%20=%20P%20*%20\dfrac{i%20*%20(1+i)^n}{(1+i)^n-1})

Where:

![alt](https://latex.codecogs.com/svg.latex?A) = annuity payment;
    
![alt](https://latex.codecogs.com/svg.latex?P) = loan principal;

![alt](https://latex.codecogs.com/svg.latex?i) = nominal (monthly) interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage. For example, if your annual interest rate = 12%, then i = 0.01;

![alt](https://latex.codecogs.com/svg.latex?n) = number of payments. This is usually the number of months in which repayments will be made.

You are interested in four values: the number of monthly payments required to repay the loan, the monthly payment amount, the loan principal, and the loan interest. Each of these values can be calculated if others are known:

Loan principal:

![alt](https://latex.codecogs.com/svg.latex?P%20=%20\dfrac{A}{\left(%20\dfrac{i%20*%20(1+i)^n}{(1+i)^n-1}%20\right)})

The number of payments:

![alt](https://latex.codecogs.com/svg.latex?n%20=%20\log_{1+i}%20\left(%20\dfrac{A}{A%20-%20i*P}%20\right))
#  Objectives

In this stage, you should add new behavior to the calculator:

1.    First, you should ask the user which parameter they want to calculate. The calculator should be able to calculate the number of monthly payments, the monthly payment amount, and the loan principal.
2.    Then, you need to ask them to input the remaining values.
3.    Finally, compute and output the value that they wanted.

Note that the user inputs the interest rate as a percentage, for example, 11.7, so you should divide this value by 100 to use it in the formula above.

Please be careful converting "X months" to "Y years and Z months". Avoid writing "0 years and 11 months" (output "11 months" instead) and "1 years and 0 months" (output "1 year" instead).

Note that in this stage, you have to ask the user to input parameters in a specific order which is provided below. Simply skip the value the user wants to calculate:

-    The first is the loan principal.
-    The second is the monthly payment.
-    The next is the number of monthly payments.
-    The last is the loan interest.

Examples

The greater-than symbol followed by a space (> ) represents the user input. Note that this is not part of the input.

Example 1

    What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal:
    > n
    Enter the loan principal:
    > 1000000
    Enter the monthly payment:
    > 15000
    Enter the loan interest:
    > 10
    It will take 8 years and 2 months to repay this loan!

Let’s take a closer look at Example 1.

You know the loan principal, the loan interest and want to calculate the number of monthly payments. What do you do?

1) You need to know the nominal interest rate. It is calculated like this:

    ![alt](https://latex.codecogs.com/svg.latex?i%20=%20\dfrac{10\%}{12%20*%20100\%}%20=%200.008333...)

2) Now you can calculate the number of months:

    ![alt](https://latex.codecogs.com/svg.latex?n%20=%20\log_{1%20+%200.008333...}%20\left(%20\dfrac{15000}{15000-0.008333...%20*%201000000}%20\right)%20=%2097.71...)

3) You need an integer number, so let’s round it up. Notice that the user will pay the same amount every month for 97 months, and in the 98th month the user will pay 0.71... of the monthly payment. So, there are 98 months to pay.

    ![alt](https://latex.codecogs.com/svg.latex?n%20=%2098)

4) Finally, you need to convert “98 months” to “8 years and 2 months” so that it is more readable and understandable for the user.

Example 2

    What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal:
    > a
    Enter the loan principal:
    > 1000000
    Enter the number of periods:
    > 60
    Enter the loan interest:
    > 10
    Your monthly payment = 21248!

Example 3

    What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal:
    > p
    Enter the annuity payment:
    > 8721.8
    Enter the number of periods:
    > 120
    Enter the loan interest:
    > 5.6
    Your loan principal = 800000!