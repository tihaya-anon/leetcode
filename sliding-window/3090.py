"""
3090. Maximum Length Substring With Two Occurrences
Easy
Topics
premium lock icon
Companies
Hint
Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.


Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".


Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
"""

from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        l = maxL = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            while freq[s[r]] > 2:
                freq[s[l]] -= 1
                l += 1
            # print(l, r, s, freq, s[l : r + 1])
            maxL = max(maxL, r - l + 1)
        return maxL


if __name__ == "__main__":
    s = "bcbbbcba"
    sol = Solution()
    ret = sol.maximumLengthSubstring(s)
    print(ret)
