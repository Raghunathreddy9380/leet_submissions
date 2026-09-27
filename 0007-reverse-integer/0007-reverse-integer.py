class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 -1
        MAX_INT_DIV_10 = MAX_INT //10

        sign = 1 if x>=0 else -1
        x= abs(x)
        result = 0

        while x != 0:
            digit = x % 10
            x //= 10

            if result > MAX_INT_DIV_10:
                return 0
            result = (result * 10) + digit
        return sign * result