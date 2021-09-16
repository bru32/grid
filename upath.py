
def retrace_path(trail, start, goal):
  """rebuild path from trail
  """
  path = []
  cp = goal
  while cp and cp != start:
    path.append(cp)
    cp = trail.get(cp, None)
  return path

