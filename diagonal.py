class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonal_sum = 0
        n = len(mat)
        for i in range(n):
            
            diagonal_sum += mat[i][i] + mat[i][n-i-1] 
        
        if n%2 == 1: 
           
            diagonal_sum -= mat[n//2][n//2] 
        return diagonal_sum
