class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return '{:032b}'.format(n).count('1')