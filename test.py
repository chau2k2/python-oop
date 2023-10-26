#this program is test bfs algorithm for codingame
#copy 

import sys
import queue
class Cell:
    def __init__(self, x, y, dist, prev) :
        #constructor
        self.x = x 
        self.y = y
        self.dist = dist; #distance to start (khoảng cách để bắt đầu)
        self.prev = prev; #parent cell in the path ( ô cha trên đường đi)
        
    def __str__(self):
        return "("+ str(self.x) + "," + str(self.y) + ")" 
    
class ShortestPathBetweenCellsBFS:
    #BFS, Time O(n^2), Space O(n^2)
    def shortestPath(self, matrix, start, end) :
        sx = start[0]
        sy = start[1]
        dx = end[0]
        dy = end[1]
		#if start or end value is 0, return ( trường hợp trùng điểm start với điểm end => no path)
        if matrix[sx][sy] == 0 or matrix[dx][dy] == 0 :
            print("There is no path.")
            return  
		#initialize the cells khởi tạo các cell
        m = len(matrix) #self.height
        n = len(matrix[0]) #self.width
        #print (m, n)
        cells = [] #dãy arrays
        for i in range (0, m):
            #duyệt từng cells
            row = []
            for j in range(0, n):               
                if matrix[i][j] != 0 :#trường hợp các ô trong ma trận khác 0
                    row.append(Cell(i, j, sys.maxsize, None))
                else:
                    row.append(None)
            cells.append(row) 
	    #breadth first search ( theo chiều rộng)
        '''tìm đường đi'''
        queue = []   #khởi tạo dãy hàng đợi  
        src = cells[sx][sy] #khởi tạo cell cho đầu vào là các cell đã duyệt
        src.dist = 0
        queue.append(src)
        dest = None
        p = queue.pop(0)
        while p != None :
            #find destination tìm điểm đến
            if p.x == dx and p.y == dy : 
                dest = p
                break	             
	        # moving up 
            self.visit(cells, queue, p.x-1, p.y, p)    
            # moving left
            self.visit(cells, queue, p.x, p.y-1, p)     
	        # moving down
            self.visit(cells, queue, p.x+1, p.y, p)             
	        #moving right
            self.visit(cells, queue, p.x, p.y+1, p)
            if len(queue) > 0:
                p = queue.pop(0)
            else:
                p = None       
	    #compose the path if path exists soạn đường dẫn nếu đường dẫn tồn tại
        if dest == None :
            print("there is no path.")
            return
        else :
            path = []
            p = dest
            while p != None :
                path.insert(0, p)	      
                p = p.prev	       
            for i in path:
                print(i)
	
    #function to update cell visiting status, Time O(1), Space O(1)
    # fuction update call tình trạng ô đến
    def visit(self, cells, queue, x, y, parent) :	
        	
        #out of boundary( ngoài danh giới)
        if x < 0 or x >= len(cells) or y < 0 or y >= len(cells[0]) or cells[x][y] == None :
            return
	    #update distance, and previous node (update khoảng cách và node trước đó)
        dist = parent.dist + 1
        p = cells[x][y]
        if dist < p.dist :
            p.dist = dist
            p.prev = parent
            queue.append(p)
matrix = [
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1],
    [0, 1, 1]]
myObj = ShortestPathBetweenCellsBFS()   
#case1, there is no path
start = [0, 0]
end = [1, 1]
print("case 1: ")
myObj.shortestPath(matrix, start, end)

#case 2, there is path
start1 = [0, 2]
end1 = [1, 1]
print("case 2: ")
myObj.shortestPath(matrix, start1, end1)