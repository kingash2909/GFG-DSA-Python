
class Solution:
    def sumOfDigits(self, n):
        '''
        :param n: given number
        :return: sum of digits of n.
        '''
        # code here

        if n < 10:
            return n
        # Recursive case: sum of digits of n is sum of its last digit and sum of digits of n/10
        return n % 10 + self.sumOfDigits(n // 10)