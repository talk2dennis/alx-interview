# 0x05. N Queens
> - Algorithm
> - Python

This directory contains algorithm to solve the nqueen puzzle using python list to keep track of the queens position (row and colomn) and backtracking incase where it is not possible to place the queen in a position and recursion.


## Usage: `nqueens N`
- If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status 1
- where N must be an integer greater or equal to 4
- If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status 1
- If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with the status 1
- The program prints every possible solution to the problem one solution per line
