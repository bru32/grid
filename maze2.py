import random
import time
import tkinter as tk
from pqueue import Queue
from ugrid import Grid
from upath import retrace_path
from ucolor import hex_lerp


class MainForm(tk.Frame):

  def __init__(self, parent):
    super().__init__(parent)
    self.parent = parent
    self.pack(fill="both", expand=1)

    self.fwidth = 400
    self.fheight = 400
    self.nx, self.ny = 10, 10
    self.dx = self.fwidth // self.nx
    self.dy = self.fheight // self.ny
    self.x0, self.x1 = 0, self.fwidth
    self.y0, self.y1 = 0, self.fheight


    self.canvas = tk.Canvas(self, width=self.fwidth, height=self.fheight, bg="#636553")
    self.canvas.place(x=25, y=25)

    self.draw_grid_lines()

    grid = Grid(self.ny, self.nx)
    start, goal = (0, 0), (self.ny-1, self.nx-1)

    self.shade_cell(start, "#c5635e")
    self.shade_cell(goal, "#81d180")

    n_tries = 0
    best_path = None
    while 1:
      path = self.find_path(grid, start, goal)
      n = len(path)
      if not best_path or n > len(best_path):
        best_path = path.copy()


        self.canvas.delete('path')
        last_x = None
        for i, cp in enumerate(best_path):
          color = hex_lerp("#81d180", "#c5635e", i/(n-1))
          self.shade_cell(cp, color=color, tag="path")

          if not last_x:
            last_y = cp[0] * self.dy + self.dy // 2
            last_x = cp[1] * self.dx + self.dx // 2

          this_y = cp[0] * self.dy + self.dy // 2
          this_x = cp[1] * self.dx + self.dx // 2

          coords = last_x, last_y, this_x, this_y
          self.canvas.create_line(coords, width=3, fill="white", tag='path')
          last_y = this_y
          last_x = this_x

          y = cp[0] * self.dy
          x = cp[1] * self.dx
          coords = x + self.dx//2, y + self.dy//2
          self.canvas.create_text(coords, text=f"{i}", font='Consolas, 12', tag='path')
        self.canvas.update()

      if len(path) == self.nx * self.ny - 4:
        break
      if n_tries > 1000000000:
        break
      n_tries += 1
      if n_tries % 1000 == 0:
        self.canvas.update()
        self.parent.title(f"{n_tries:,} its")


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

  def find_path(self, graph, start, goal):
    que = Queue(start)
    seen = [start]
    trail = {start: None}
    while not que.empty():
      cp = que.popleft()
      if cp == goal:
        break
      steps = graph.possibles(cp, seen)
      if len(steps) <= 0:
        goal = cp
        break
      np = random.choice(steps)
      seen.append(np)
      que.push(np)
      trail[np] = cp
    return retrace_path(trail, start, goal)


def main():
  root = tk.Tk()
  root.title('Grid Search')
  root.geometry('450x450+800+100')
  MainForm(root)
  root.mainloop()


# ---------------------------------------------------------------------

if __name__ == "__main__":
  main()
