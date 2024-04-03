class Solution:
    def countDigits(self, n):
        '''
        :param n: given number
        :return: count of digits of n.
        '''
        # code here
        
        if n == 0:
            return 0
        return 1 + self.countDigits(n // 10)