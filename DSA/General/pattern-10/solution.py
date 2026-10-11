class Solution:
    def pattern10(self, n):
        for i in list(range(n)) + list(range(n-1,-1)):
            for j in range(i+1):
                print("*",end="")
            print()
            
        for k in range(n-1):
            for l in range(n-k-1):
                print("*",end="")
            print()