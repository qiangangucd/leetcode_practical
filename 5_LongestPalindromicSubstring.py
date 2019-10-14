'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


class Solution():
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""

        # create list of 2n-1 possible centres, each letter and between each pair
        # even indices represent letters, odd represent between letters
        # start with middle index that potentially creates longest paliindrome
        centres = [len(s) - 1]
        for diff in range(1, len(s)):  # build list of indices from long to short
            centres.append(centres[0] + diff)
            centres.append(centres[0] - diff)

        for centre in centres:

            if (min(centre + 1, 2 * len(s) - 1 - centre) <= len(longest)):
                break  # return if cannot make a longer palindrome

            if centre % 2 == 0:
                left, right = (centre // 2) - 1, (centre // 2) + 1
            else:
                left, right = centre // 2, (centre // 2) + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left and right are now beyond the ends of the substring

            if right - left - 1 > len(longest):
                longest = s[left + 1:right]

        return longest


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('ababcabd'))
