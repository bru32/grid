# Translation from JavaScript
# Dan Shiffman, Coding Train
# https://editor.p5js.org/codingtrain/sketches/dRWS3A9nq

import time
import random
from dataclasses import dataclass
import tkinter as tk



def draw_grid_lines():
  x = dx
  while x < width:
    canvas.create_line(x, 0, x, height, width=1, fill='#60849f')
    x += dx
  y = dy
  while y < height:
    canvas.create_line(0, y, width, y, width=1, fill='#60849f')
    y += dy


def do_plot(path):
  #canvas.delete('path')
  if len(path) >= 4:
    coords = []
    for p in path:
      y = p.r * dy + dy // 2
      x = p.c * dx + dx // 2
      xy = x, y
      coords.append(xy)
    #canvas.create_line(coords, fill="yellow", width=13, tag="path")
    #canvas.update()
    #time.sleep(0.01)


def is_valid(r, c):
  return 0 <= r < rows and 0 <= c < cols and not grid[r][c].seen


@dataclass
class Step:
  dr: int
  dc: int
  tried: bool


@dataclass
class Cell:
  r: int
  c: int
  seen: bool = False
  steps = (Step(1, 0, False), Step(-1, 0, False), Step(0, 1, False), Step(0, -1, False))

  def clear(self):
    self.steps = (Step(1, 0, False), Step(-1, 0, False), Step(0, 1, False), Step(0, -1, False))
    self.seen = False

  def rand_step(self):
    arr = []
    for step in self.steps:
      if not step.tried:
        if is_valid(self.r+step.dr, self.c+step.dc):
          arr.append(step)
    print(f"{self.r,self.c}: {arr}")
    if arr:
      np = random.choice(arr)
      np.tried = True
      return grid[self.r+np.dr][self.c+np.dc]
    else:
      return None


def find_path(cp):
  path = [cp]
  cp.seen = True
  while True:
    cp = cp.rand_step()
    if cp:
      path.append(cp)
      cp.seen = True
    else:
      stuck = path.pop(-1)
      stuck.clear()
      cp = path[-1] # backtrack 1 step
    #do_plot(path)
    if len(path) == cols * rows:
      print('Solved!')
      return path


"""
root = tk.Tk()
root.geometry('450x450+1050+50')
frame = tk.Frame(root)
frame.pack(fill="both", expand=1)
"""
rows, cols = 5, 5
"""
width, height = 400, 400
dx = width / cols
dy = height / rows
canvas = tk.Canvas(frame, width=width, height=height, bg="#636553")
canvas.place(x=25, y=25)
draw_grid_lines()
"""
grid = [[Cell(r,c) for c in range(cols)] for r in range(rows)]
start = grid[0][0]
path = find_path(start)
"""
do_plot(path)
root.mainloop()
"""
