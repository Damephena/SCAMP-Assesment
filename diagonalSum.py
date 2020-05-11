'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix (3 x 3) is shown below:
1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1 + 5 + 9 = 15
The right to left diagonal =  3 + 5 + 9 = 17
Their absolute difference is = |15 - 17| = 2

Write a function called diagonalDifference in your editor. It must return an integer representing the absolute diagonal difference
Note that this function takes an array as a parameter..

Test Cases:
A) 11 2 4  
   4 5 6
   10 8 -12
B) -1 1 -7 -8
   -10 -8 -5 -2
    0 9 7 -1
    4 4 -2 1
C) -10 3 0 5 -4
    2 -1 0 2 -8
    9 -2 -5 6 0
    9 -7 4 8 -2
    3 7 8 -5 0
D) 6 8
  -6 9

Excepted output for all test cases:
A) 15
B) 1
C) 3
D) 13

'''

def diagonalSums(arr):
    if not arr: return None # check if list is empty

    n = len(arr)
    
    if(n != len(arr[0])): raise ValueError('Input must be a valid square matrix')

    # right diagonal
    i, ltrSum = 0, 0

    while(i < len(arr)):
        ltrSum += arr[i][i]
        i += 1

    # left diagonal
    j, k, rtlSum = 0, n-1, 0

    while (j < n and k >= 0):
        rtlSum += arr[j][k]
        j += 1
        k -= 1
    
    return abs(ltrSum - rtlSum)

arr1 = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
arr2 = [[-1, 1, -7, -8], [-10, -8, -5, -2], [0, 9, 7, -1], [4, 4, -2, 1]]
arr3 = [[-10, 3, 0, 5, -4], [2, -1, 0, 2, -8], [9, -2, -5, 6, 0], [9, -7, 4, 8, -2], [3, 7, 8, -5, 0]]
arr4 = [[6, 8], [-6, 9]]

print(diagonalSums([]))
print(diagonalSums(arr1))
print(diagonalSums(arr2))
print(diagonalSums(arr3))
print(diagonalSums(arr4))