"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        INT32_MIN = -2**31
        INT32_MAX = 2**31 - 1

        print(8463847412 * -1)
        print(f"INT32_MIN: {INT32_MIN}, INT32_MAX: {INT32_MAX}")

        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_num = 0

        while x_abs != 0:
            pop = x_abs % 10
            x_abs //= 10

            # Check for overflow before multiplying/adding
            """
            # Check if appending the next digit would cause overflow for 32-bit signed integer
            if (reversed_num > INT32_MAX // 10 if already greater than INT32_MAX // 10
            or
                if last second digit is equal to INT32_MAX last second digit, check if the last digit is greater than INT32_MAX last digit
                (reversed_num == INT32_MAX // 10 and pop > INT32_MAX % 10)):
                return 0
            """
            if (reversed_num > INT32_MAX // 10 or
                (reversed_num == INT32_MAX // 10 and pop > INT32_MAX % 10)):
                return 0

            """Yes, exactly. INT32_MIN (-2**31) has one more in absolute value than INT32_MAX (2**31-1), 
            so its reverse (8463847412) exceeds the positive limit. 
            Since the reversal logic builds the number as positive, checking against INT32_MAX is enough
            """

            reversed_num = reversed_num * 10 + pop

        return sign * reversed_num


if __name__ == "__main__":
    solution = Solution()
    n = -2147483647
    result = solution.reverse(n)
    print(f"The reverse of number {n}  is: {result}")