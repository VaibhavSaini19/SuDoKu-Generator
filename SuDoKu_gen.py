import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


class Board:
    def __init__(self, seed=None):
        # Initialize an empty grid
        self.grid = np.zeros((9, 9), dtype=int)

    def is_Valid(self, num, row, col):
        '''
        Method to check whether the passed number is valid to be put in the corresponding cell (i.e. if it does 
        not clashes within its row / column / 3x3 grid)
        '''
        if num > 9:
            return False
        three_by_three = (row//3, col//3)
        start_row, end_row = three_by_three[0]*3, three_by_three[0]*3 + 3
        start_col, end_col = three_by_three[1]*3, three_by_three[1]*3 + 3

        if num in self.grid[start_row: end_row, start_col:end_col]:
            return False
        if num in self.grid[:, col] or num in self.grid[row, :]:
            return False
        return True

    def fill_grid(self):
        '''
        Method to create a solution (not Solve) a SuDoKu 9x9 grid.
            Reduce computation by first filling 3 3x3 grids on the diagonal, as they won't have
        any row / col constraints as such at this (beginning) stage.
            Then start filling remaining cells from top-to-bottom, left-to-right, with allowable
        numbers, backtrack when required.
        '''
        for i in range(3):                      # Fill Diagonal 3x3s
            arr = np.arange(1, 10)
            np.random.shuffle(arr)
            arr = np.reshape(arr, (3, 3))
            self.grid[i*3:i*3+3, i*3:i*3+3] = arr

        i = j = 0                               # start filling rest of the grid
        prev_i = list()
        prev_j = list()
        prev_k = list()
        k = 1
        while i < 9:
            j = 0
            flag = 0
            while j < 9:
                if self.grid[i, j] == 0:
                    if not flag:
                        temp = [x for x in range(1, 10)]
                    else:
                        temp = [x for x in range(k, 10)]
                    for ele in self.grid[i, :]:
                        try:
                            temp.remove(ele)
                        except:
                            pass
                    for k in temp:
                        # print(i, j, k)
                        # print(self.grid)
                        if self.is_Valid(k, i, j):
                            self.grid[i, j] = k
                            prev_i.append(i)
                            prev_j.append(j)
                            prev_k.append(k)
                            temp.remove(k)
                            flag = 0
                            break
                    else:
                        i = prev_i.pop()
                        j = prev_j.pop()
                        self.grid[i, j] = 0
                        k = prev_k.pop() + 1
                        flag = 1
                        j -= 1
                j += 1
            if 0 in self.grid[i, :]:
                break
            i += 1

        # print("*"*50)
        print(self.grid)

    def create_puzzle(self):
        '''
        Method to create a SuDoKu puzzle by randomly revealing cells from the completely filled grid.
        Generate 15 random positions in the 9x9 grid, reveale them and their mirror cells across a diagonal
        (Though its not necessary, but a symmetric board is more appealing and appreciated, apparently)
        '''
        self.puzzle = np.zeros((9, 9), dtype=str)
        
        n = 0
        while n < 15:
            i = np.random.randint(9)
            j = np.random.randint(9)
            if self.puzzle[i, j] == '':
                self.puzzle[i, j] = self.grid[i, j]
                self.puzzle[j, i] = self.grid[j, i]
                n += 1
        for row in range(9):
            for col in range(9):
                if self.puzzle[row, col] == '':
                    self.puzzle[row, col] = ' '
        '''
        self.puzzle = np.zeros((9, 9), dtype=int)
        n = 0
        while n < 15:
            i = np.random.randint(9)
            j = np.random.randint(9)
            if self.puzzle[i, j] == 0:
                self.puzzle[i, j] = self.grid[i, j]
                self.puzzle[j, i] = self.grid[j, i]
                n += 1
        '''
        print(self.puzzle)

    def show_puzzle(self):
        fig, ax = plt.subplots()
        ax.set_ylim(ax.get_ylim()[::-1])

        for i in range(0, 9):
            for j in range(0, 9):
                val = self.puzzle[j, i]
                ax.text(i+0.5, 9-(j+0.5), str(val), fontweight='bold', va='center', ha='center')

        ax.set_xlim(0, 9)
        ax.set_ylim(0, 9)
        ax.set_xticks(np.arange(9))
        ax.set_yticks(np.arange(9))
        # ax.grid()
        ax.xaxis.set_major_locator(MultipleLocator(3))
        ax.xaxis.set_minor_locator(MultipleLocator(1))

        ax.yaxis.set_major_locator(MultipleLocator(3))
        ax.yaxis.set_minor_locator(MultipleLocator(1))

        ax.xaxis.grid(True,'minor')
        ax.yaxis.grid(True,'minor')
        ax.xaxis.grid(True,'major',linewidth=3)
        ax.yaxis.grid(True,'major',linewidth=3)

        plt.show()


if __name__ == "__main__":
    board = Board()
    board.fill_grid()
    board.create_puzzle()
    board.show_puzzle()
