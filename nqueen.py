# https://leetcode.com/problems/n-queens/
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no
# two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both
# indicate a queen and an empty space respectively.

# Just a simple application of recursion with backtracking.
# Leftdiag = diagonals sloping left (negative slope) and rightdiag = diagonals sloping right (positive slope)
# if a row has a queen, then row[i] is true
# if a column has a queen then column[i] is true
# if a queen is at (i,j), then its left diagonal leftDiag[i+j] = true and
# its right diagonal rightDiag[j - i + n -1] = true
# 
def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    L = [[False]*n for k in range(n)]

    leftDiag = [False]*(2*n - 1)
    rightDiag = [False]*(2*n - 1)
    column = [False] * n
    row = [False] * n
    queens = 0
    i = 0
    count = [0]
    helper(L, leftDiag, rightDiag, column, row, queens, i, n, count)
    print(count)


def helper(L, leftDiag, rightDiag, column, row, queens, i, n, count):

    if queens == n:
        return True

    if i == n:
        return False
    
    for j in range(n):  # try everything in row i
        if not leftDiag[i+j] and not rightDiag[j-i+n-1] and not column[j] and not row[i]:
            L[i][j] = True
            leftDiag[i+j] = True
            rightDiag[j-i+n-1] = True
            column[j] = True
            row[i] = True
            queens += 1
            ret = helper(L, leftDiag, rightDiag, column, row, queens, i+1, n, count)
            if ret:
                count[0] += 1
            
            L[i][j] = False
            leftDiag[i+j] = False
            rightDiag[j-i+n-1] = False
            column[j] = False
            row[i] = False
            queens -= 1

    return False

solveNQueens(12)
