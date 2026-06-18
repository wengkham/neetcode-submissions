class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        match = hold = 0
        for num in nums:
            if num == 1:
                match += 1
            else:
                if match > hold:
                    hold = match
                match = 0
        return max(match, hold)

            