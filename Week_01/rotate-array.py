class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums);
        nums[:] = nums[(length-k):] + nums[:(length-k)];