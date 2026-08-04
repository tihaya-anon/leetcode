"""
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        maxLen = 0
        contain = set()
        for r in range(n):  # [l,r]
            while s[r] in contain:
                contain.discard(s[l])
                l += 1
            contain.add(s[r])
            # print(s, l, r, s[l : r + 1])
            maxLen = max(maxLen, r - l + 1)
        return maxLen


if __name__ == "__main__":
    s = "pwwkew"
    sol = Solution()
    ret = sol.lengthOfLongestSubstring(s)
    print(ret)
