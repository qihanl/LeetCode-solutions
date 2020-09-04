# Original problem: https://leetcode.com/problems/two-sum/



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        
        for i in range(0, len(nums)):
            if (target - nums[i]) not in dictionary.keys():
                dictionary[nums[i]] = i
            else:
                return [dictionary[target-nums[i]], i]
            
        # e.g.: nums = [2,7,11,15], target = 9
        # first iteration: i = 0, nums[i] = 2, dictionary = {}
        # (9-2) = 7 is not in {}: dictionary[2] = 0
        # second itration: i = 1, nums[i] = 7, dictionary = {[2:0]}
        # (9-7) = 2 is in dictionary, go to else: return [0, 1]
        
