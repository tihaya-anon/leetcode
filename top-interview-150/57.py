"""
57. Insert Interval
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Two intervals are considered overlapping if they share at least one point.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        new_start, new_end = newInterval
        eff_start, eff_end = newInterval
        pref = []
        suff = []
        for interval in intervals:
            start, end = interval
            if end >= new_start:
                eff_start = min(start, new_start)
                break
            pref.append(interval)
        for interval in reversed(intervals):
            start, end = interval
            if start <= new_end:
                eff_end = max(end, new_end)
                break
            suff.insert(0, interval)
        return [*pref, [eff_start, eff_end], *suff]


print(
    Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]), [[1, 5], [6, 9]]
)

print(
    Solution().insert(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
    ),
    [[1, 2], [3, 10], [12, 16]],
)
