
import collections
import random
import time
import tkinter as tk

class Queue:

  def __init__(self):
    self.items = collections.deque()

  def empty(self):
    return not self.items

  def push(self, x):
    self.items.append(x)

  def popleft(self):
    return self.items.popleft()

  def pop(self):
    return self.items.pop()


class Grid:

  def __init__(self, nr, nc):
    self.nr = nr
    self.nc = nc

  def in_range(self, cp):
    (r, c) = cp
    return 0 <= r < self.nr and 0 <= c < self.nc

  def adj(self, cp, seen):
    (r, c) = cp
    steps = [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]
    res = []
    for np in steps:
      if self.in_range(np) and np not in seen:
        res.append(np)
    return res


class MainForm(tk.Frame):

  def __init__(self, parent):
    super().__init__(parent)
    self.parent = parent
    self.pack(fill="both", expand=1)

    self.fwidth = 400
    self.fheight = 400
    self.nx, self.ny = 8, 8
    self.dx = self.fwidth // self.nx
    self.dy = self.fheight // self.ny
    self.x0, self.x1 = 0, self.fwidth
    self.y0, self.y1 = 0, self.fheight

    self.canvas = tk.Canvas(self, width=self.fwidth, height=self.fheight, bg="#636553")
    self.canvas.place(x=25, y=25)

    self.draw_grid_lines()

    grid = Grid(self.ny, self.nx)
    start = (0, 0)
    its = 0
    while 1:
      self.canvas.delete('path')
      path = find_saw(grid, start)

      # Draw Path
      y0, x0 = None, None
      for cp in path:
        if not x0:
          y0 = cp[0] * self.dy + self.dy // 2
          x0 = cp[1] * self.dx + self.dx // 2
        y1 = cp[0] * self.dy + self.dy // 2
        x1 = cp[1] * self.dx + self.dx // 2
        coords = x0, y0, x1, y1
        self.canvas.create_line(coords, fill="#a5d920", width=7, tag="path")
        y0, x0 = y1, x1

      if its % 1000 == 0:
        self.canvas.update()
        time.sleep(0.1)

      if len(path) == self.ny * self.nx:
        break

      its += 1
      if its > 1000000:
        break

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


def find_saw(graph, start):
  seen = []
  cp = start
  while 1:
    seen.append(cp)
    steps = graph.adj(cp, seen)
    if not steps:
      break
    cp = random.choice(steps)
  return seen


def main():
  root = tk.Tk()
  root.title('Grid Search')
  root.geometry('450x450+800+100')
  MainForm(root)
  root.mainloop()


if __name__ == "__main__":
  main()
