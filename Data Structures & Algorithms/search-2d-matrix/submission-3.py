class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bot = len(matrix) - 1


        while (top <= bot):
            # mid = top + (bot-top) // 2
            # if target > matrix[mid][0] and target < matrix[mid][-1]:
            #     sm = matrix[mid]
            # elif target > matrix[mid][-1]:
            #     top = mid + 1
            # else:
            #     bot = mid - 1
            row = top + (bot-top) // 2
            print(row)
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        row = (top + bot) // 2
        sm = matrix[row]
        l = 0
        r = len(sm)-1
        while (l <= r):
            mid = l + (r-l) // 2
            if target == sm[mid]:
                return True
            elif target > sm[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return False