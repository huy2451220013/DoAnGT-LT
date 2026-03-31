class Solution(object):
    def findClosestElements(self, arr, k, x):
        l, r = 0, len(arr) - k

        while l < r:
            mid = l + (r - l) // 2
            if arr[mid + k] - x < x - arr[mid]:
                l = mid + 1
            else:
                r = mid
        return arr[l: l + k]      
