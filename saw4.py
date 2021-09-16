# Self Avoiding Random Walk, version #4
# This is not production code, I'm experimenting and tweaking to try
# different strategies with not much concern about appearance.  The
# plot using tkinter as a bit of a stick on that made it simpler to
# use a few unnecessary globals.
# Bruce Wernick
# 19 September 2021
# Based on -
#   Daniel Shiffman, Coding Train - self avoiding walk youtube
#   Amit Patel, Red Blob Games - BFS search using a grid
#   Raymond Hettinger, Simple Spreadsheet based on cells

import random
import sys
import time
import tkinter as tk


rows = 5
cols = 5

root = tk.Tk()
root.title('Self Avoiding Walk #4')
width, height = 300, 300
margin = 20
root.geometry(f"{width+2*margin}x{height+2*margin}+950+50")
frame = tk.Frame(root)
frame.pack(fill="both", expand=1)
dx = width / cols
dy = height / rows

# create a canvas to draw on
canvas = tk.Canvas(frame, width=width, height=height, bg="#636553")
canvas.place(x=margin, y=margin)

# draw vertical grid lines
x = dx
while x < width:
  canvas.create_line(x, 0, x, height, width=1, fill='#60849f')
  x += dx

# draw horizontal grid lines
y = dy
while y < height:
  canvas.create_line(0, y, width, y, width=1, fill='#60849f')
  y += dy


def plot_path(path):
  canvas.delete('path')
  coords = []
  for cp in path:
    y0 = cp[0] * dy + dy // 2
    x0 = cp[1] * dx + dx // 2
    xy = x0, y0
    coords.append(xy)
  canvas.create_line(coords, fill="#e6ac5b", width=5, tag="path")
  canvas.update()


def plot_dot(cp):
  g = 7
  canvas.delete('dot')
  y0 = cp[0] * dy + dy // 2
  x0 = cp[1] * dx + dx // 2
  canvas.create_oval(x0-g, y0-g, x0+g, y0+g, fill="red", width=0, tag="dot")
  canvas.update()


class Cell:

  rows = 0
  cols = 0

  def __init__(self, cp):
    self.r, self.c = cp
    self.tried = []

  @classmethod
  def in_range(cls, cp):
    r, c = cp
    return 0 <= r < cls.rows and 0 <= c < cls.cols

  def rand_step(self, path):
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    random.shuffle(steps)
    possibles = []
    for step in steps:
      r = self.r + step[0]
      c = self.c + step[1]
      cp = (r, c)
      if self.in_range(cp):
        if cp not in path:
          if cp not in self.tried:
            possibles.append(cp)

    if possibles:
      result = random.choice(possibles)
      self.tried.append(result)
      return result

    return None


def findSAW(cp, max_tries=None):
  """find a self avoiding walk
  """
  if not max_tries:
    max_tries = sys.maxsize
  n_steps = Cell.rows * Cell.cols  # target number of steps
  path = [cp]
  hist = {cp: Cell(cp)}
  max_len = 0
  for n_tries in range(max_tries):
    cp = hist[cp].rand_step(path)
    if cp:
      path.append(cp)
      hist[cp] = Cell(cp)
    else:
      xp = path.pop(-1)
      hist[xp] = None  # kill the blocked step
      del xp
      cp = path[-1]  # backtrack 1 step

    if n_tries % 1000000 == 0:
      print(n_tries // 1000000, end=", ")
    plot_dot(cp)

    n = len(path)
    if n > max_len:
      # improvement
      max_len = n
      # print(max_len, end=",")
      plot_path(path)  # plot current path on canvas
      time.sleep(0.1)
      
    if n == n_steps:
      print(f'Solved in {n_tries} tries')
      return path
      
  raise Exception('Max tries reached!')


def main():
  Cell.rows = rows
  Cell.cols = cols
  start = (0, 0)
  path = findSAW(start)
  if path:
    plot_path(path)
  root.mainloop()


if __name__ == '__main__':
  main()
