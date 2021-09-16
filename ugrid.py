
class Grid:
  """2D Rect Grid
  """
  def __init__(self, nr, nc):
    self.nr, self.nc = nr, nc
    self.walls = []

  def __in_bounds(self, cp):
    (r, c) = cp
    return 0 <= r < self.nr and 0 <= c < self.nc

  def __passable(self, cp):
    return cp not in self.walls

  def adj(self, cp):
    (r, c) = cp
    res = [(r, c+1), (r-1, c), (r, c-1), (r+1, c)]
    if (r+c) % 2 == 0:
      res.reverse()
    res = filter(self.__in_bounds, res)
    res = filter(self.__passable, res)
    return res

  def possibles(self, cp, seen):
    (r, c) = cp
    # steps = [(r, c+1), (r-1, c), (r, c-1), (r+1, c), (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]
    steps = [(r, c + 1), (r - 1, c), (r, c - 1), (r + 1, c)]
    res = []
    for np in steps:
      if self.__in_bounds(np):
        if np not in self.walls:
          if np not in seen:
            res.append(np)
    return res
