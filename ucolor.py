
def hex_to_rgb(value):
  hx = value.lstrip('#')
  return tuple(int(hx[i: i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
  return f'#{r:02x}{g:02x}{b:02x}'


def rgb_lerp(rgb1, rgb2, f):
  r = int(rgb1[0] + f * (rgb2[0] - rgb1[0]))
  g = int(rgb1[1] + f * (rgb2[1] - rgb1[1]))
  b = int(rgb1[2] + f * (rgb2[2] - rgb1[2]))
  return r, g, b


def hex_lerp(a, b, f):
  a = hex_to_rgb(a)
  b = hex_to_rgb(b)
  rgb = rgb_lerp(a, b, f)
  return rgb_to_hex(*rgb)
