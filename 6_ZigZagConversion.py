'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        row = 0
        direction = -1
        zigzag = [[] for _ in range(numRows)]
        for c in s:
            zigzag[row].append(c)
            if row == 0 or row == numRows - 1:
                direction = -direction
            row += direction
        return ''.join([c for r in zigzag for c in r])


if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    c = Solution()
    print(c.convert(s, 5))
