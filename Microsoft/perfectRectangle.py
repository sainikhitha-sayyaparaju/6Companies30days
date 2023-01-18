# Perfect Rectangle : https://leetcode.com/problems/perfect-rectangle/

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = defaultdict(int)
        for i in rectangles:
            corners[(i[0], i[1])] += 1
            corners[(i[2], i[3])] += 1
            corners[(i[0], i[3])] -= 1
            corners[(i[2], i[1])] -= 1
            print(corners)
        cnt = 0
        print(corners)
        for i in corners:
            if abs(corners[i]) == 1:
                cnt += 1
            elif abs(corners[i]) != 0:
                return False
        return cnt == 4


# Just used map to keep the count of edges.
# Increasing the count of bottom left and top right vertices.
# Decreasing the count of bottom right and top left vertices.
# At Last We sum all the values of map.
# If the value is 4 then return true as four vertices are there, else return false.
