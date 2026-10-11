class Solution:
    def pattern9(self, n):
        
        for i in range(n):
            for j in range(n-1-i):
                print(" ",end="")
            for k in range(i*2+1):
                print("*",end="")
            print()

        for i in range(n):
            for j in range (i):
                print(" ",end="")
            for k in range((n-i)*2-1):
                print("*",end = "")
            print()