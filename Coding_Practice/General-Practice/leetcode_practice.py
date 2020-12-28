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

    def diagonalSum(self, mat) -> int:
        side = len(mat)
        row = col = res = 0
        col2 = side - 1
        while row < side:
            res += (mat[row][col] + mat[row][col2])
            row += 1
            col += 1
            col2 -= 1
        if side%2 == 0:
            return res
        return res - mat[side//2][side//2] #124 ms -- while loop is actually a bit slower than for in python!

    def destCity(self, paths) -> str:
        record = {}
        for pair in paths:
            start = pair[0]
            stop = pair[1]
            record[start] = stop
        for city in record.values():
            if city not in record.keys():
                return city
        return None

        # better solution? - use sets!
        # A, B = map(set, zip(*paths))
        # return (B - A).pop()

    def maxProduct(self, nums: list) -> int:
        return  (nums.pop(nums.index(max(nums)))-1) * (nums.pop(nums.index(max(nums))) - 1)

    def countNegatives(self, grid) -> int:
        # grid rows are sorted in descending order
        total = 0 
        for row in grid:
            # go until -1 
            for i in range(len(row)-1, -2, -1):
                # if we reached out of index, then all were negative numbers 
                if i == -1:
                    total += len(row)
                    break
                # else run until you find a positive number
                if row[i] >= 0:
                    total += len(row) - i - 1 # this will be the number of negative numbers in the row
                    break
        return total

    def sortArrayByParity(self, A):
        evens = []
        odds = []
        for num in A:
            if num % 2 == 0: evens.append(num)
            else: odds.append(num)
        evens.extend(odds)
        return evens

        # AWESOME one-liner: return sorted(A, key=lambda x: x & 1)

    def minWindow(self, s: str, t: str) -> str:
        for char in set(t):
            if char not in set(s):
                return ""
        l = len(t)
        while True:
            for i in range(l -1, len(s)):
                charCount = 0
                for char in set(t):
                    if char in set(s[i-l+1:i+1]):
                        charCount +=1 
                if charCount == len(t): return s[i-l+1:i+1]
            l += 1
            if l > len(s): break

    def intersection_naive(self, nums1, nums2):
        setA, setB = set(nums1), set(nums2)
        return list(setA.intersection(setB))

if __name__ == "__main__":
    sol = Solution()
    # past testing:
        # print(sol.findNumbers([12,345,2,6,7896]))
        # print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
        # print(sol.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
        # print(sol.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
        # print(sol.maxProduct([1,5,4,5]))
        # print(sol.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
        # print(sol.sortArrayByParity([3,1,2,4]))
    import time
    print(sol.minWindow("A", "T"))
