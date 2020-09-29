# Original problem: https://leetcode.com/problems/longest-palindromic-substring/

# Solution is insired by https://www.youtube.com/watch?v=XYQecbcd6_c

# For each letter in the string, start from the letter itself, go one letter aside (left and right) to check if there's a palindrom near the letter. Be aware of the even-length string corner case.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = "" #the resulting palindromic substring
        longest = 0 #the length of the current longest palindromic substring
        
        for i in range(len(s)):
            #odd-length case:
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left]==s[right]:
                if(right - left + 1) > longest:
                    result = s[left:right+1]
                    longest = right - left + 1
                left = left - 1
                right = right + 1
            
            #even-length case:
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left]==s[right]:
                if(right - left + 1) > longest:
                    result = s[left:right+1]
                    longest = right - left + 1
                left = left - 1
                right = right + 1
        return result
