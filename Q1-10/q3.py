# Original question: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return len(s)
        current = ""
        longest = -1
        
        for letter in s:
            if (letter not in current):
                current = current+letter
            else:
                if len(current) > longest:
                    longest = len(current)
                index = current.find(letter)
                current = current + letter
                current = current[index+1:len(current)]
        return max(longest,len(current))
