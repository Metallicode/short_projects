'''
It is not always possible to create a magic square of a given size n with rows, columns, and diagonals that add up to a specified value. This is because the numbers in a magic square must be a permutation of the numbers from 1 to n * n, and not all such permutations will result in a magic square. For example, if n is odd, it is always possible to create a magic square with the desired sum. However, if n is even, it is only possible to create a magic square with the desired sum if the sum is a multiple of n (see the Lo Shu square).

In the function above, if a magic square of the specified size and sum cannot be generated, the function returns an empty array. This indicates that a magic square with the given parameters is not possible.


'''


def generateMagicSquare(n, magic_value):
    # Initialize a 2-dimensional array of size n by n filled with 0s
    magic_square = [[0 for x in range(n)] for y in range(n)]
    
    # Initialize position of 1 in the middle of the top row
    i = 0
    j = n // 2
    
    # Fill in the values of the magic square, starting with 1
    num = 1
    while num <= (n * n):
        # Place the number at the current position
        magic_square[i][j] = num
        num += 1
        
        # Calculate the next position according to the rules of the magic square
        # If the next position is outside of the bounds of the square, wrap around to the opposite side
        # If the next position is already occupied, move down one row
        i -= 1
        j += 1
        if i < 0:
            i = n - 1
        if j == n:
            j = 0
        if magic_square[i][j] != 0:
            i += 2
            j -= 1
            if i >= n:
                i = i - n
            if j < 0:
                j = n - 1
    
    # Check that the magic square adds up to the desired value
    # If not, return an empty array
    if checkMagicSquare(magic_square, n, magic_value):
        return magic_square
    else:
        return []
        
def checkMagicSquare(square, n, magic_value):
    # Check the rows
    for i in range(n):
        row_sum = 0
        for j in range(n):
            row_sum += square[i][j]
        if row_sum != magic_value:
            return False
    
    # Check the columns
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += square[i][j]
        if col_sum != magic_value:
            return False
    
    # Check the diagonals
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += square[i][i]
    if diagonal_sum != magic_value:
        return False
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += square[i][n - i - 1]
    if diagonal_sum != magic_value:
        return False
    
    return True
    
    
print(generateMagicSquare(5, 50))
