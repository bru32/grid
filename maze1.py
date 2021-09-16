"""
Run a maze
Bruce Wernick
12 September 2021
"""

from pqueue import Queue
from ugrid import Grid
from upath import retrace_path


def find_path(graph, start, goal):
  """dfs path through graph"""
  que = Queue(start)
  trail = {start: None}
  while not que.empty():
    cp = que.popleft()
    if cp == goal:
      break
    for np in graph.adj(cp):
      if np not in trail:
        que.push(np)
        trail[np] = cp
  return retrace_path(trail, start, goal)


def main():
  grid = Grid(10, 20)
  grid.walls = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12),
                (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18),
                (0, 19), (1, 0), (1, 2), (1, 9), (1, 19), (2, 0),
                (2, 2), (2, 4), (2, 19), (3, 0), (3, 2), (3, 4), (3, 5),
                (3, 6), (3, 7), (3, 9), (3, 19), (4, 0), (4, 2), (4, 7),
                (4, 9), (4, 14), (4, 16), (4, 17), (4, 18), (4, 19),
                (5, 0), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7),
                (5, 9), (5, 14), (6, 0), (6, 7), (6, 9), (6, 14),
                (6, 15), (6, 16), (6, 17), (6, 18), (6, 19), (7, 0),
                (7, 1), (7, 2), (7, 9), (7, 19), (8, 0), (8, 1), (8, 2),
                (8, 9), (8, 19), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4),
                (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10),
                (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 16),
                (9, 17), (9, 18), (9, 19)]

  start, goal = (1, 1), (5, 19)
  path = find_path(grid, start, goal)
  for item in path:
    print(item, end=', ')


# ---------------------------------------------------------------------

if __name__ == "__main__":
  main()
