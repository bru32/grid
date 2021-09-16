
import random
from pqueue import Queue


class Grid:

  def __init__(self, nr, nc):
    self.nr = nr
    self.nc = nc
    self.size = nr * nc

  def in_range(self, cp):
    (r, c) = cp
    return 0 <= r < self.nr and 0 <= c < self.nc

  def adj(self, cp):
    (r, c) = cp
    steps = [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]
    arr = []
    for np in steps:
      if self.in_range(np):
        arr.append(np)
    random.shuffle(arr)
    return arr


def dfs(graph, start):
  path = []
  stack = Queue()
  stack.push(start)
  while not stack.empty():
    cp = stack.popleft()
    if cp in path:
      continue
    path.append(cp)
    for np in graph.adj(cp):
      stack.push(np)
  return path


def main():
  nr, nc = 8, 8
  grid = Grid(nr, nc)
  start = (0, 0)
  path = dfs(grid, start)
  print(path)
  print(len(path))


if __name__ == "__main__":
  main()
