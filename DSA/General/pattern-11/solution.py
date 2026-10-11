class Solution:
    def pattern11(self, n):
        for row in range(1, n + 1):
            values = []
            start = 1 if row % 2 == 1 else 0

            for col in range(row):
                values.append(str(start))
                start = 1 - start

            print(" ".join(values))