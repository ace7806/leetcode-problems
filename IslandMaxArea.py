grid =[
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# = 6

def countArea(grid):
    queue = []
    output = 0
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            count = 0
            if grid[row][column]==1:
                queue.append((row,column))
                count+=1
                grid[row][column] = 0
                while queue:
                    size = len(queue)
                    for i in range(size):
                        x1,y1 = queue.pop(0)
                        for x,y in directions:
                            x+=x1
                            y+=y1
                            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1:
                                queue.append((x,y))
                                grid[x][y]=0
                                count+=1
            output=max(output,count)
    return output
print(countArea(grid))
