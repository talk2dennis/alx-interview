# 0x07. Rotate 2D Matrix
> - Algorithm
> - Python

# Matrix Rotation

This repository contains a Python function that rotates a square matrix 90 degrees clockwise. The rotation is performed using a list comprehension, providing a concise and efficient solution.

## Function Description

### `rotateMatrix(matrix)`

- **Purpose**: Rotates a given square matrix 90 degrees clockwise.
- **Parameters**:
  - `matrix` (list of lists of int): A 2D square matrix represented as a list of lists.
- **Returns**: A new matrix (list of lists of int) that is the original matrix rotated 90 degrees clockwise.

## Usage

To use the `rotateMatrix` function, follow these steps:

1. **Import the Function**: Copy the function definition into your Python script.
2. **Prepare Your Matrix**: Define a square matrix as a list of lists.
3. **Call the Function**: Pass your matrix to the `rotateMatrix` function and capture the result.
4. **Print or Use the Result**: Display the rotated matrix or use it in subsequent calculations.

### Example

# Original matrix
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Rotate the matrix
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]

