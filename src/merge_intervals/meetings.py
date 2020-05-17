from typing import List

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if len(intervals) < 2:
            return True

        # sort the intervals using starting times

        intervals.sort(key=lambda x: x[0])

        merged = []  ## to store merged intervals

        print("Sorted interval: ", intervals)
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            current_interval = intervals[i]

            if current_interval[0] < end:
                ##end = max(end, current_interval[1])
                return False
            else:
                start = current_interval[0]
                end = current_interval[1]
        return True



