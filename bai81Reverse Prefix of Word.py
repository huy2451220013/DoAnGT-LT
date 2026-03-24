class Solution(object):
    def reversePrefix(self, word, ch):
        break_index = word.find(ch)
    
        if break_index != -1:
            n = word[:break_index + 1][::-1]  # reversing the digits which are up to break_index 
            z = word[break_index + 1:] # words starting from break_index to the end 
            return n + z
        return word
        
        
