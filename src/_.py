
# In the main project I'm using the underscore to denote global constants.
# Appearently that's not really done in Python (I'm not a Python guy obviously)
# so putting all globals into a file that everything imports seems like the way
# to go. By naming this module "_" globals can be referenced like _.TILE_SIZE
# elsewhere.

TILE_SIZE = 128

N = 'N'
S = 'S'
E = 'E'
W = 'W'

DIRECTION_MAP = [N,S,E,W]

CHANEL = 'C'
HALL = 'H'
ROOM = 'R'
STONE = 'S'
