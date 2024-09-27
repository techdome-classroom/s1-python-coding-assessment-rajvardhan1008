class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def zero(i,j):

            if (i!=m and i!=-1 and j!=n and j!=-1 and  grid[i][j]=="L"):
                grid[i][j]="W"
                zero(i+1,j)
                zero(i-1,j)
                zero(i,j+1)
                zero(i,j-1)
            
            return

        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "L":
                    total+=1
                    zero(i,j)

        return total   
