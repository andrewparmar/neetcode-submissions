class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        create a set of numbers in nums
        for each num in seen
        if num-1 in seen, pass
        else 
            counter until num+1 not in set
        keep track of max_lenght
        """
        numbers = set(nums)
        longest = 0
        for num in nums:
            if num-1 in numbers:
                pass
            else:
                counter = 1
                while (num + counter) in numbers:
                    counter += 1
                longest = max(longest, counter)
        return longest
