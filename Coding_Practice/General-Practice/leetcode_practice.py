# 1295. Find Numbers with Even Number of Digits
class Solution:
    def findNumbers(self, nums) -> int:
        '''
        Given an array nums of integers, return how many of them contain an even number of digits.
        '''
        # return len([x for x in nums if len(str(x))%2==0]) # 56 ms
        res = 0
        for num in nums:
            if len(str(num))%2 == 0:
                res += 1
        return res #92 ms

    def minTimeToVisitAllPoints(self, points) -> int:
        '''
        Given a list of points, find the minimum time needed to travel to all of them.
        1) need to go in order, 2) moving vert, hori, or diag = 1 sec
        '''
        def gettimebetweenpoints(pt1, pt2):
            dist = (abs(pt2[0] - pt1[0]), abs(pt2[1] - pt1[1]))
            diag = min(dist)
            return dist[0] + dist[1] - diag # diag + (dist[0] - diag) + (dist[1] - diag)

        res = 0
        for idx in range(len(points)-1):
            res += gettimebetweenpoints(points[idx], points[idx+1])
        return res #60 ms

if __name__ == "__main__":
    sol = Solution()
    # print(sol.findNumbers([12,345,2,6,7896]))
    print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))