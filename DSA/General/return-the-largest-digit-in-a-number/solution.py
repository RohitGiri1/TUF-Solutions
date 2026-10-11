class Solution:
    def largestDigit(self, n):
        number = abs(n)

        if number == 0:
            return 0

        largest = 0
        while number > 0:
            digit = number % 10
            if digit > largest:
                largest = digit
            number //= 10

        return largest