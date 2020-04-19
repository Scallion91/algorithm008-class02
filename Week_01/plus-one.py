class Solution:
    def plusOne(self, digits):
        nums = ''
        for i in digits:
            nums = nums + str(i) 
        nums = int(nums) + 1
        return list(map(int, str(nums)))