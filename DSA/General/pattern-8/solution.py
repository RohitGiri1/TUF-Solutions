class Solution:
    def pattern8(self, n):
        for i in range(n):
            for j in range(i):
                print(" ",end="")
            for k in range(((n-i)*2)-1):
                print("*",end="")
            print()