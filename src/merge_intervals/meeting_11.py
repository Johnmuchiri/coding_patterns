from typing import List

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        count = 0

        if len(intervals) == 1:
            return 1
        if not intervals:
            return 0

        used_rooms = 0
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted([i[1] for i in intervals])
        l = len(intervals)

        start_pointer = 0
        end_pointer = 0

        while start_pointer < l:
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -= 1
                end_pointer += 1
            used_rooms += 1
            start_pointer += 1
        return used_rooms
