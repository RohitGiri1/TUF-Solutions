class Solution:
    def pattern19(self, n):
        for i in range(n):
            for j in range(n-i):
                print("*",end="")

            for j in range(i):
                print(" ",end="")

            for k in range(i):
                print(" ",end="")

            for l in range(n-i):
                print("*",end="")
            print()

        for x in range(n):
            for y in range(x+1):
                print("*",end="")
            for z in range(n-x-1):
                print(" ",end="")
            for a in range(n-x-1):
                print(" ",end="")
            for b in range(x+1):
                print("*",end="")
            print()