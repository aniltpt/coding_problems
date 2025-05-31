# 5/31/2025
class Solution:
    def evenlyDivides(self, n):
        return self.divide_by_all_digits(n, n, 0)

    def divide_by_all_digits(self, n, new_number, divisible_count):
        quotient = new_number // 10
        remainder = new_number % 10
        if remainder != 0:
            if n % remainder == 0:
                divisible_count += 1

        if quotient == 0:
            return divisible_count
        return self.divide_by_all_digits(n, quotient, divisible_count)


if __name__ == "__main__":
    solution = Solution()
    n = 12
    result = solution.evenlyDivides(n)
    print(f"The number of digits in {n} that evenly divide it is: {result}")