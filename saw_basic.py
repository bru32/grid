# saw_basic.py
# Author: Bruce Wernick
# date: 14 September 2021

import random
import time
from pqueue import Queue
import tkinter as tk


class Grid:

  def __init__(self, nr, nc):
    self.nr = nr
    self.nc = nc
    self.size = nr * nc

  def in_range(self, cp):
    (r, c) = cp
    return 0 <= r < self.nr and 0 <= c < self.nc

  def adj(self, cp, seen):
    (r, c) = cp
    steps = [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]
    arr = []
    for np in steps:
      if self.in_range(np) and np not in seen:
        arr.append(np)
    return arr


class Chart(tk.Frame):

  def __init__(self, parent):
    super().__init__(parent)
    self.parent = parent
    self.pack(fill="both", expand=1)

    self.fwidth = 400
    self.fheight = 400
    self.nx, self.ny = 5, 5
    self.dx = self.fwidth // self.nx
    self.dy = self.fheight // self.ny
    self.x0, self.x1 = 0, self.fwidth
    self.y0, self.y1 = 0, self.fheight

    self.canvas = tk.Canvas(self, width=self.fwidth, height=self.fheight, bg="#636553")
    self.canvas.place(x=25, y=25)

    self.draw_grid_lines()

    grid = Grid(self.ny, self.nx)
    start = (0, 0)
    self.find_saw(grid, start)


  def draw_grid_lines(self):
    # vertical grid lines
    x = self.x0 + self.dx
    while x < self.x1:
      self.canvas.create_line(x, self.y0, x, self.y1, width=1, fill='#60849f')
      x += self.dx

    # horizontal grid lines
    y = self.y0 + self.dy
    while y < self.y1:
      self.canvas.create_line(self.x0, y, self.x1, y, width=1, fill='#60849f')
      y += self.dy

  def shade_cell(self, cp, color='#cacc71', tag=None):
    g = 4
    y = cp[0] * self.dy
    x = cp[1] * self.dx
    coords = x+g, y+g, x+self.dx-g, y+self.dy-g
    self.canvas.create_rectangle(coords, width=1, outline="#52521e", fill=color, tag=tag)
    self.canvas.update()

  def find_saw(self, graph, start):
    tried = []
    seen = [start]
    que = Queue()
    que.push(start)
    came_from = {start: None}
    while not que.empty():
      cp = que.popleft()
      self.shade_cell(cp, tag=cp)
      time.sleep(1)
      if len(seen) == graph.size:
        break
      steps = graph.adj(cp, seen+tried)
      if not steps:
        tried.append(cp)
        seen.remove(cp)
        self.shade_cell(cp, color="red", tag=cp)
        self.canvas.update()
        time.sleep(1)
        que.pushleft(came_from[cp])
        came_from.pop(cp, None)
        continue
      np = random.choice(steps)
      seen.append(np)
      que.push(np)
      came_from[np] = cp
      #tried.clear()
    return seen


def main():
  root = tk.Tk()
  root.title('Grid Search')
  root.geometry('450x450+800+100')
  Chart(root)
  root.mainloop()


if __name__ == "__main__":
  main()
