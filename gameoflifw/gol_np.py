import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation
from random import choice
import numpy as np
import json

Mother_Board = []
HashTable = []

class GameBoard:
    def __init__(self, c, r):
        self.counter = 0
        self.grids = []
        self.grids.append(self._make_grid(c, r, rnd=True))
        self.grids.append(self._make_grid(c, r))

    def get_grid(self):
        self.counter+=1
        if (not self.counter-1==0):     
            return self.grids[(self.counter-1)%2]*0
        return self.grids[(self.counter-1)%2]

    def _make_grid(self, x, y, rnd = False):
        if(rnd==False):
            return np.array([np.zeros(x) for j in range(y)])
        else:
            return np.array([np.random.choice([0, 1], size=x) for j in range(y)])

def count_neighbours(x, y, grid):
    neighbours = 0-grid[x][y]
    for i in range(-1,2):
        for j in range(-1,2):
            col = (x+i+cols) % cols
            row = (y+j+rows) % rows

            neighbours += grid[col][row]
            if neighbours > 3:
                break

    return neighbours

def scan_grid(grid):
    global gb
    new_grid = gb.get_grid()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_grid[i][j] = 1 if count_neighbours(i,j,grid)==3 else 0
    return new_grid

def func_animate(i):
    global a
    global Mother_Board
    a = scan_grid(a)   
    z.set_array(a)
    live_cells = count_live_cells(a)
    print(f"live cells:  {live_cells}")
    current_hash = hash(str(a))

    if(live_cells == 0 or current_hash in HashTable):
        with open("test.txt", "w") as fp:
            json.dump(Mother_Board, fp)
        quit()

    Mother_Board.append(a)
    HashTable.append(current_hash)

def count_live_cells(grid):
    live_cells = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==1:
                live_cells+=1
    
    return live_cells

cols = 50
rows = 50

gb = GameBoard(cols,rows)
a = gb.get_grid()

fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot()
z = ax1.imshow(a, interpolation='nearest', cmap=cm.Greys_r)
z.axes.get_xaxis().set_visible(False)
z.axes.get_yaxis().set_visible(False)

ani = FuncAnimation(fig,
                    func_animate,
                    interval=150)

plt.show()