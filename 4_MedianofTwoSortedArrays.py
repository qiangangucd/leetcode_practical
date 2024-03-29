'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution():
    def findMedianSortedArrays(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: float
        """

        def get_kth_smallest(a_start, b_start, k):

            if k <= 0 or k > len(A) - a_start + len(B) - b_start:
                raise ValueError('k is out of the bounds of the input lists')

            # base cases
            if a_start >= len(A):
                return B[b_start + k - 1]
            if b_start >= len(B):
                return A[a_start + k - 1]
            if k == 1:
                return min(A[a_start], B[b_start])

            # remove k//2 elements from one list
            # find the smallest of the k//2 - 1th element from both lists and recurse having reduced that list.
            # k//2 - 1th element must exist in at least 1 list
            mid_A, mid_B = float('inf'), float('inf')
            if k // 2 - 1 < len(A) - a_start:
                mid_A = A[a_start + k // 2 - 1]
            if k // 2 - 1 < len(B) - b_start:
                mid_B = B[b_start + k // 2 - 1]

            if mid_A < mid_B:
                return get_kth_smallest(a_start + k // 2, b_start, k - k // 2)
            return get_kth_smallest(a_start, b_start + k // 2, k - k // 2)

        right = get_kth_smallest(0, 0, 1 + (len(A) + len(B)) // 2)
        if (len(A) + len(B)) % 2 == 1:  # odd total length
            return right

        left = get_kth_smallest(0, 0, (len(A) + len(B)) // 2)
        return (left + right) / 2.0


if __name__ == '__main__':
    A = [1, 3, 6, 8, 9]
    B = [2, 3, 4, 5, 5]
    a = Solution()
    print(a.findMedianSortedArrays(A, B))
