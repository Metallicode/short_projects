import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation
from random import choice

class GameBoard:
    def __init__(self, c, r):
        self.counter = 0
        self.grids = []
        self.grids.append(self._make_grid(c, r, rnd=True))
        self.grids.append(self._make_grid(c, r))

    def get_grid(self):
        self.counter+=1
        if (not self.counter-1==0):     
            return self._clear_grid(self.grids[(self.counter-1)%2])
        return self.grids[(self.counter-1)%2]

    def _clear_grid(self, g):
        for i in range(len(g)):
            for j in range(len(g[i])):
                g[i][j] = 0
        return g

    def _make_grid(self, x, y, rnd = False):
        if(rnd==False):
            return [[0 for i in range(x)] for j in range(y)]
        else:
            return [[choice([0,1]) for i in range(x)] for j in range(y)]

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
    a = scan_grid(a)
    z.set_array(a)


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
                    interval=200)

plt.show()