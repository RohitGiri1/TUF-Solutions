class Solution:
    def pattern7(self, n):
        for i in range(n):
            for j in range(n-1-i):
               print(" ",end="")
            for k in range(i*2+1):
                print("*",end="")
            print()