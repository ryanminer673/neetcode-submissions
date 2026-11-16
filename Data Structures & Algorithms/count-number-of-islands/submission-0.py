class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # loop through each element
        # if it a 1 flood that island complently
        # then continue looping noting evry time you encounter a 1

        # bfs approach for flooding 

        def flood_island(row, col):
            
            #check teh north south east and west cell to see if its a 1
            # if its a 1 the add the cord to the queue of cords 
            # flood teh cell your on and repeat until queue is empty

            queue = deque()

            queue.append((row, col))
            
            while queue:
                row, col = queue.pop()
                grid[row][col] = '0'

                #check north
                if row > 0 and grid[row-1][col] == '1':
                    queue.append((row-1, col))
                #check south
                if row < len(grid)-1 and grid[row+1][col] == '1':
                    queue.append((row+1, col))
                #check west
                if col > 0 and grid[row][col-1] == '1':
                    queue.append((row, col-1))
                #check east
                if col < len(grid[row])-1 and grid[row][col+1] == '1':
                    queue.append((row, col+1))




        
        num_isl = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col] == "1":
                    num_isl += 1
                    flood_island(row, col)

        return num_isl



        