#-------------------------------------------------------------------------
# Python 3.7
# Date:   30 June 2019
# Author: c stacey
#-------------------------------------------------------------------------


class FlatSurface:
  '''Represents a flat, rectangular surface with a specified width
     (along the surface's x-axis) and depth (along the surface's y-axis).

     Objects are located on the surface using a *map grid* system where
     the co-ordinates of a grid square are given by an (x,y) pair.
     The grid size is arbitrary,
     and is only known by the user of a FlatSurface object.

     For example, if a FlatSurface has width = 5, depth = 5, and the user
     of the FlatSurface imagines the grid squares to be 1x1 in size,
     then the grid square furthest away from grid square (0,0),
     is the grid square (4,4).
     Importantly, grid square (5,5) is *off* the surface.'''

  def __init__(s, width=5, depth=5):

    if width > 0 and depth > 0:
      s._width = width
      s._depth = depth
    else:
      raise ValueError("surface width and depth must be positive values")


  def is_on_surface(s, x, y) -> bool:
    '''returns true if grid (x,y) is atop the flat surface'''

    return (x >= 0 and x < s._width and
            y >= 0 and y < s._depth)


  def __repr__(s) -> str:
    return f"FlatSurface(width={s._width}, depth={s._depth})"



class Character:
  '''Represents a Character that can be placed onto a FlatSurface.
     The location of the Character is specifed using the *grid*
     co-ordinate system of FlatSurface (ie. (x,y) grid co-ords).
     The Character can be moved about the flat surface using the methods:
       PLACE place Character on FlatSurface at some position, facing some
             valid direction.
       MOVE  move forward one unit in direction currently facing
       LEFT  turn left 90 degrees (anticlockwise looking down from above)
       RIGHT turn right 90 degrees
     The Character will ignore any MOVE command that would result in her
     moving off the FlatSurface.
     The Character will ignore any PLACE command that would result in her
     being placed off the FlatSurface.'''

  # assumes north/south/east/west align with local x and y axes of object.
  _NSEW          = ['NORTH', 'EAST', 'SOUTH', 'WEST']
  _unit_vectors  = [(0,1)  , (1,0) , (0,-1) , (-1,0)]


  def __init__(s):
    s._flat_surface = None
    s._position     = None
    s._dir_index    = None


  def place(s, flat_surface, x, y, direction, *args, **kwargs) -> bool:
    '''place Character on FlatSurface. return True if successful (ie. all
       arguments were valid), else return False.'''

    direction = direction.upper()

    if (flat_surface.is_on_surface(x,y) and
        direction in s._NSEW):
      s._flat_surface = flat_surface
      s._position     = (x,y)
      s._dir_index    = s._NSEW.index(direction)
      return True
    else:
      return False


  def move(s, *args, **kwargs) -> bool:
    '''move Character forward one unit (in the direction it's facing),
       making sure to stay on the FlatSurface.
       return True if successful, else return False.'''

    if s._flat_surface:
      newPos = (s._position[0] + s._unit_vectors[s._dir_index][0],
                s._position[1] + s._unit_vectors[s._dir_index][1])

      if (s._flat_surface.is_on_surface(*newPos)):
        s._position = newPos
        return True

    return False


  def left(s, *args, **kwargs) -> bool:
    '''rotate character 90 degrees anti-clockwise about its z-axis
       (looking from above). If successful, return True. If Character is
       not on a FlatSurface, do nothing and return False.'''

    if s._flat_surface:
      s._dir_index = (s._dir_index + 3) % 4
      return True
    else:
      return False


  def right(s, *args, **kwargs) -> bool:
    '''rotate character 90 degrees clockwise about its z-axis
       (looking from above). If successful, return True. If Character is
       not on a FlatSurface, do nothing and return False.'''

    if s._flat_surface:
      s._dir_index = (s._dir_index + 1) % 4
      return True
    else:
      return False


  def report(s, *args, **kwargs) -> str:
    '''print current (x,y) position and direction of Character'''

    if s._flat_surface:
      x,y = s._position
      d   = s._NSEW[s._dir_index]
      ret = f"{x},{y},{d}"
    else:
      ret = "None, None, None"
    
    print(ret)
    return ret


  def __repr__(s) -> str:
    if s._flat_surface:

      fs  = repr(s._flat_surface)
      x,y = s._position
      d   = s._NSEW[s._dir_index]

      return f'Character({fs}, {x}, {y}, {d})'
    else:
      return 'Character()'


#-------------------------------------------------------------------------
# END OF FILE
#-------------------------------------------------------------------------