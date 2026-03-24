class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boats = 0
        people.sort()  # Sort the array in ascending order
        left, right = 0, len(people) - 1
        
        while left <= right:
            if left == right:
                # If there's only one person left
                boats += 1
                break
            
            if people[left] + people[right] <= limit:
                # If the sum of weights of two people can fit in one boat
                left += 1
                right -= 1
            else:
                # If only one person can fit in one boat
                right -= 1
            boats += 1
        
        return boats