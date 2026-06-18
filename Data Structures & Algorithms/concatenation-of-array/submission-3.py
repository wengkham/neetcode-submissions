class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums * 2
        copyNumbs = list(nums)
        for num in nums:
            copyNumbs.append(num)
        return copyNumbs