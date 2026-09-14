from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left_higher = [0]
        for i in range(N - 1):
            last = left_higher[i]
            h = height[i]
            left_higher.append(max(last, h))
        right_higher = [0]
        for i in range(N - 1):
            last = right_higher[i]
            h = height[-1 - i]
            right_higher.append(max(last, h))
        right_higher.reverse()
        # print(height)
        # print(left_higher)
        # print(right_higher)
        ret = 0
        for h, L, R in zip(height, left_higher, right_higher):
            min_h = min(L, R)
            if h >= min_h:
                continue
            ret += min_h - h
        return ret


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([4, 2, 0, 3, 2, 5]))
