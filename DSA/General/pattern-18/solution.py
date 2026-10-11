class Solution:
    def pattern18(self, n):
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                print(f"{chr(65+j)} ",end = "")
            print()