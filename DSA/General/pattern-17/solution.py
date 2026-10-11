class Solution:
    def pattern17(self, n):
        for i in range(1,n+1):
            print(" "*(n-i),end="")
            for j in list(range(i)) + list(range(i-2,-1,-1)):
                print(chr(65+j),end="")
            print()