#-------------------------------------------------------------------------
# Python 3.7
# Date:   30 June 2019
# Author: c stacey
#-------------------------------------------------------------------------

from ReadifyToyRobot import *

from functools import wraps


def logit(func, func_name):
  '''decorator function used to print names of functions called'''

  @wraps(func)
  def wrapped(*args, **kwargs):
    s1  = ', '.join( [f'{v!r}' for v in args] )
    s2  = ', '.join( [f'{k}={v!r}' for k, v in kwargs.items()] )
    sep = ', ' if s1 != '' and s2 != '' else ''

    print(f"{func_name}(", s1, sep, s2, ")", sep='', end='\n')
    func(*args, **kwargs)

  return wrapped


def testA():

  # create table and robot that will be used in testing
  table = FlatSurface()
  robot = Character()

  # Wrap methods of THIS INSTANCE of Character (to print calls to console)
  # Second arg is used because passing in the variable name 'robot'
  # makes the output easier to read (no better way to get variable name).
  robot.report = logit(robot.report, 'robot.report')
  robot.right  = logit(robot.right,  'robot.right')
  robot.left   = logit(robot.left,   'robot.left')
  robot.place  = logit(robot.place,  'robot.place')
  robot.move   = logit(robot.move,   'robot.move')

  print(f"table = {table}")
  robot.report(); print()

  robot.place(table, 0, 0, 'north')
  robot.move()
  robot.report()

  '''
  >>> testA()
  table = FlatSurface(width=5, depth=5)
  robot.report()
  None, None, None

  robot.place(FlatSurface(width=5, depth=5), 0, 0, 'north')
  robot.move()
  robot.report()
  0,1,NORTH
  '''


def testB():

  # create table and robot that will be used in testing
  table = FlatSurface()
  robot = Character()

  # Wrap methods of THIS INSTANCE of Character (to print calls to console)
  # Second arg is used because passing in the variable name 'robot'
  # makes the output easier to read (no better way to get variable name).
  robot.report = logit(robot.report, 'robot.report')
  robot.right  = logit(robot.right,  'robot.right')
  robot.left   = logit(robot.left,   'robot.left')
  robot.place  = logit(robot.place,  'robot.place')
  robot.move   = logit(robot.move,   'robot.move')

  print(f"table = {table}")
  robot.report(); print()

  robot.place(table, 0, 0, 'north')
  robot.left()
  robot.report()

  '''
  >>> testB()
  table = FlatSurface(width=5, depth=5)
  robot.report()
  None, None, None

  robot.place(FlatSurface(width=5, depth=5), 0, 0, 'north')
  robot.left()
  robot.report()
  0,0,WEST
  '''


def testC():

  # create table and robot that will be used in testing
  table = FlatSurface()
  robot = Character()

  # Wrap methods of THIS INSTANCE of Character (to print calls to console)
  # Second arg is used because passing in the variable name 'robot'
  # makes the output easier to read (no better way to get variable name).
  robot.report = logit(robot.report, 'robot.report')
  robot.right  = logit(robot.right,  'robot.right')
  robot.left   = logit(robot.left,   'robot.left')
  robot.place  = logit(robot.place,  'robot.place')
  robot.move   = logit(robot.move,   'robot.move')

  print(f"table = {table}")
  robot.report(); print()

  robot.place(table, 1, 2, 'east')
  robot.move()
  robot.move()
  robot.left()
  robot.move()
  robot.report()

  '''
  >>> testC()
  table = FlatSurface(width=5, depth=5)
  robot.report()
  None, None, None

  robot.place(FlatSurface(width=5, depth=5), 1, 2, 'east')
  robot.move()
  robot.move()
  robot.left()
  robot.move()
  robot.report()
  3,3,NORTH
  '''


def testD():

  # create table and robot that will be used in testing
  table = FlatSurface(width=3, depth=3)
  robot = Character()

  # Wrap methods of THIS INSTANCE of Character (to print calls to console)
  # Second arg is used because passing in the variable name 'robot'
  # makes the output easier to read (no better way to get variable name).
  robot.report = logit(robot.report, 'robot.report')
  robot.right  = logit(robot.right,  'robot.right')
  robot.left   = logit(robot.left,   'robot.left')
  robot.place  = logit(robot.place,  'robot.place')
  robot.move   = logit(robot.move,   'robot.move')


  print(f"table = {table}")
  robot.report(); print()

  # test ignoring commands before valid placement
  robot.right()
  robot.report(); print()

  robot.left()
  robot.report(); print()

  robot.move()
  robot.report(); print()

  # test ignoring invalid place commands
  robot.place(table, 10, 10, 'NORTH')
  robot.report(); print()

  robot.place(table, 2, 2, 'JUNK')
  robot.report(); print()

  # valid place
  robot.place(table, 2, 2, 'north')
  robot.report(); print()

  # test not falling off table
  robot.move()
  robot.report(); print()

  robot.right()
  robot.report(); print()

  robot.move()
  robot.report(); print()

  robot.right()
  robot.report(); print()

  robot.move()
  robot.report(); print()

  robot.right()
  robot.report(); print()

  robot.move()
  robot.report(); print()

  robot.move()
  robot.report(); print()

  robot.move()
  robot.report(); print()

  robot.left()
  robot.report(); print()

  robot.move()
  robot.report(); print()

  robot.move()
  robot.report(); print()

  # test invalid and valid place cmd (after valid place cmd)

  robot.place(table, 10, 10, 'north')
  robot.report(); print()

  robot.place(table, 1, 1, 'west')
  robot.report(); print()

  # test turning left/right past north point
  robot.right()
  robot.report(); print()

  robot.right()
  robot.report(); print()

  robot.left()
  robot.report(); print()

  robot.left()
  robot.report(); print()

  '''
  >>> testD()
  table = FlatSurface(width=3, depth=3)
  robot.report()
  None, None, None

  robot.right()
  robot.report()
  None, None, None

  robot.left()
  robot.report()
  None, None, None

  robot.move()
  robot.report()
  None, None, None

  robot.place(FlatSurface(width=3, depth=3), 10, 10, 'NORTH')
  robot.report()
  None, None, None

  robot.place(FlatSurface(width=3, depth=3), 2, 2, 'JUNK')
  robot.report()
  None, None, None

  robot.place(FlatSurface(width=3, depth=3), 2, 2, 'north')
  robot.report()
  2,2,NORTH

  robot.move()
  robot.report()
  2,2,NORTH

  robot.right()
  robot.report()
  2,2,EAST

  robot.move()
  robot.report()
  2,2,EAST

  robot.right()
  robot.report()
  2,2,SOUTH

  robot.move()
  robot.report()
  2,1,SOUTH

  robot.right()
  robot.report()
  2,1,WEST

  robot.move()
  robot.report()
  1,1,WEST

  robot.move()
  robot.report()
  0,1,WEST

  robot.move()
  robot.report()
  0,1,WEST

  robot.left()
  robot.report()
  0,1,SOUTH

  robot.move()
  robot.report()
  0,0,SOUTH

  robot.move()
  robot.report()
  0,0,SOUTH

  robot.place(FlatSurface(width=3, depth=3), 10, 10, 'north')
  robot.report()
  0,0,SOUTH

  robot.place(FlatSurface(width=3, depth=3), 1, 1, 'west')
  robot.report()
  1,1,WEST

  robot.right()
  robot.report()
  1,1,NORTH

  robot.right()
  robot.report()
  1,1,EAST

  robot.left()
  robot.report()
  1,1,NORTH

  robot.left()
  robot.report()
  1,1,WEST
  '''


#-------------------------------------------------------------------------
# END OF FILE
#-------------------------------------------------------------------------