class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        guess = 0

        while start <= end:
            guess = (start + end) // 2
            num = nums[guess]
            if num < target:
                start = guess + 1
            elif num > target:
                end = guess - 1
            elif num == target:
                return guess
        return -1