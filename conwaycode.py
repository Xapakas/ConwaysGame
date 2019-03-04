# Conway's Game of Life

from graphics import *
import time

def getInitialSetup():
    r_file = open("conway.txt", "r")
    l_grid = []
    l_add = []
    s_add = r_file.readline()
    s_add = s_add.strip()
    i_cols = len(s_add)
    i_lines_read = 0
    while s_add != "":
        for i_num in range(len(s_add)):
            l_add.append(s_add[i_num])
        l_grid.append(l_add)
        l_add = []
        i_lines_read += 1
        s_add = r_file.readline()
    i_rows = i_lines_read

    return l_grid, i_rows, i_cols

def drawDisplay(l_grid, i_rows, i_cols, win):
    cover_rectangle = Rectangle(Point(0,0), Point(800, 600))
    cover_rectangle.setOutline("white")
    cover_rectangle.draw(win)
    x_base = 0
    y_base = 0
    for i_row in range(i_rows):
        for i_col in range(i_cols):
            square = Rectangle(Point(x_base, y_base), Point(x_base + 20, y_base + 20))
            if l_grid[i_row][i_col] == "x":
                s_color = "black"
                s_outline = "black"
            elif l_grid[i_row][i_col] == "o":
                s_color = "white"
                s_outline = "white"
            square.setFill(s_color)
            square.setOutline(s_outline)
            square.draw(win)
            x_base += 20
        x_base = 0
        y_base += 20

def CalculateLiveNeighbors(l_grid, i_rows, i_cols):
    l_neighbor_grid = []
    l_add_grid = []
    for i_row in range(i_rows):
        for i_col in range(i_cols):
            i_live_neighbors = 0
            if i_row > 0: # north square exists
                if l_grid[i_row - 1][i_col] == "x": # is there a neighbor in that spot?
                    i_live_neighbors += 1
            if i_row < (i_rows - 1): # south square exists
                if l_grid[i_row + 1][i_col] == "x":
                    i_live_neighbors += 1
            if i_col < (i_cols - 1): # east square exists
                if l_grid[i_row][i_col + 1] == "x":
                    i_live_neighbors += 1
            if i_col > 0: # west square exists
                if l_grid[i_row][i_col - 1] == "x":
                    i_live_neighbors += 1
            if i_row > 0 and i_col < (i_cols - 1): # northeast square exists
                if l_grid[i_row - 1][i_col + 1] == "x":
                    i_live_neighbors += 1
            if i_row > 0 and i_col > 0: #northwest square exists
                if l_grid[i_row - 1][i_col - 1] == "x":
                    i_live_neighbors += 1
            if i_row < (i_rows - 1) and i_col < (i_cols - 1): #southeast square exists
                if l_grid[i_row + 1][i_col + 1] == "x":
                    i_live_neighbors += 1
            if i_row < (i_rows - 1) and i_col > 0: # southwest square exists
                if l_grid[i_row + 1][i_col - 1] == "x":
                    i_live_neighbors += 1
            l_add_grid.append(i_live_neighbors)
        l_neighbor_grid.append(l_add_grid)
        l_add_grid = []
        
    return l_neighbor_grid

def getNextState(l_neighbor_grid, l_grid, i_rows, i_cols):
    l_new_grid = []
    l_add = []
    for i_row in range(i_rows):
        for i_col in range(i_cols):
            if l_neighbor_grid[i_row][i_col] < 2:
                l_add.append("o")
            elif l_neighbor_grid[i_row][i_col] == 2 and l_grid[i_row][i_col] == "x":
                l_add.append("x")
            elif l_neighbor_grid[i_row][i_col] == 2 and l_grid[i_row][i_col] == "o":
                l_add.append("o")
            elif l_neighbor_grid[i_row][i_col] == 3:
                l_add.append("x")
            elif l_neighbor_grid[i_row][i_col] > 3:
                l_add.append("o")
        l_new_grid.append(l_add)
        l_add = []

    return l_new_grid
                

def main():
    win = GraphWin("Conway Window", 800, 600)
    l_grid, i_rows, i_cols = getInitialSetup()
    while True:
        drawDisplay(l_grid, i_rows, i_cols, win)
        l_neighbor_grid = CalculateLiveNeighbors(l_grid, i_rows, i_cols)
        l_grid = getNextState(l_neighbor_grid, l_grid, i_rows, i_cols)
##        time.sleep(0.25)
        win.getMouse()

main()
