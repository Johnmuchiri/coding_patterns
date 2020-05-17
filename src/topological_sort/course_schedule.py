from typing import  List
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5

"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        sorted_list = []
        if numCourses <= 0:
            return False
        graph = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}

        for i in range(len(prerequisites)):
            parent, child = prerequisites[i][0], prerequisites[i][1]
            graph[parent].append(child)
            in_degree[child] += 1

        print(graph)
        print(in_degree)

        ## find all sources
        sources = []
        for i in in_degree:
            if in_degree[i] == 0:
                sources.append(i)
        ##sort
        while sources:
            vertex = sources.pop()
            sorted_list.append(vertex)

            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

            # if the sorted list doesnt have all the courses the there is a cycle:
            # if scheduling is not possible then there is a cycle
        return len(sorted_list) == numCourses








