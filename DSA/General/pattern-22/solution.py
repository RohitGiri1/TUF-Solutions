class Solution:
    def pattern22(self, n):
        center = n-1
        size = (n*2)-1
        for i in range(size):
            for j in range(size):
                row = abs(center-i)+1
                column = abs(center-j)+1

                if row > column :
                    print(f"{row} ",end="")
                else :
                    print(f"{column} ",end="")
            print()