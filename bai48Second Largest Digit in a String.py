class Solution(object):
    def secondHighest(self, s):
        #step 1: filter out letters and duplicates, and then leave us with a list of only numbers
        numberList = [int(num) for num in list(set(s)) if num.isnumeric()]
        #step 2: check if list has at least two values
        if len(numberList) < 2:
            return -1
        #step 3: sort the list
        sortedNums = sorted(numberList)
        #step 4: return 2nd largest
        return sortedNums[-2]
