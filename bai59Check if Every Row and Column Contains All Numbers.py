class Solution(object):
    def checkValid(self, matrix):
	
        for i in range(len(matrix)):
            if len(set(matrix[i])) != len(matrix) or len(set([r[i] for r in matrix])) != len(matrix):   return False
            
        return True
