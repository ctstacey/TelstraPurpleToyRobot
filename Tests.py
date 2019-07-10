#-------------------------------------------------------------------------
# Python 3.7
# Date:   30 June 2019
# Author: c stacey
#-------------------------------------------------------------------------

# the library we are testing
from ReadifyToyRobot import *

import io
import sys

# for copying function __name__ etc from wrapped func to wrapper func
from functools import wraps

# for parsing command line arguments
import argparse



class Tester:
  '''A class for performing basic testing of functions return values.'''

  def __init__(s):
    s.capturedOutput = None
  
  def start_logging(s) -> None:
    s.capturedOutput = io.StringIO()
    sys.stdout = s.capturedOutput
    
  def stop_logging(s) -> None:
    sys.stdout = sys.__stdout__

  def get_log(s) -> str:
    '''returns the captured output thus far (a string)
       (does not consume the stream, thus this method is idempotent)'''
    return s.capturedOutput.getvalue()

  # technically this is a static method
  def capture_calls_and_returns(s, func, func_name):
    '''decorator function used to print names of functions called.
       Note: arguments passed in are captured in their repr form.
             (ie. calls will not be identical to that made in code)'''

    @wraps(func)
    def wrapped(*args, **kwargs):
      s1  = ', '.join( [f'{v!r}' for v in args] )
      s2  = ', '.join( [f'{k}={v!r}' for k, v in kwargs.items()] )
      sep = ', ' if s1 != '' and s2 != '' else ''

      call = f"{func_name}({s1}{sep}{s2})"
      print(call)

      r = func(*args, **kwargs)
      print(' returned:\n',r)

    return wrapped



def testA():

  t = Tester()
 
  # create table and robot that will be used in testing
  table = FlatSurface()
  robot = Character()

  # Wrap methods of THIS INSTANCE of Character (to print calls to console)
  # Second arg is used because passing in the variable name 'robot'
  # makes the output easier to read (no better way to get variable name).
  robot.report = t.capture_calls_and_returns(robot.report, 'robot.report')
  robot.right  = t.capture_calls_and_returns(robot.right,  'robot.right')
  robot.left   = t.capture_calls_and_returns(robot.left,   'robot.left')
  robot.place  = t.capture_calls_and_returns(robot.place,  'robot.place')
  robot.move   = t.capture_calls_and_returns(robot.move,   'robot.move')

  t.start_logging()

  print(f"table = {table}")
  robot.report(); print()

  robot.place(table, 0, 0, 'north')
  robot.move()
  robot.report()
 
  t.stop_logging()
    
  if t.get_log() == \
    "\n".join(
      ['''table = FlatSurface(width=5, depth=5)'''
      ,'''robot.report()'''
      ,'''None, None, None'''
      ,''' returned:'''
      ,''' None, None, None'''
      ,''''''
      ,'''robot.place(FlatSurface(width=5, depth=5), 0, 0, 'north')'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.move()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''0,1,NORTH'''
      ,''' returned:'''
      ,''' 0,1,NORTH'''
      ,''''''
      ]):
    print("testA PASSED")
    return True
  else:
    print("testA *FAILED*")
    return False


def testB():

  t = Tester()

  # create table and robot that will be used in testing
  table = FlatSurface()
  robot = Character()

  # Wrap methods of THIS INSTANCE of Character (to print calls to console)
  # Second arg is used because passing in the variable name 'robot'
  # makes the output easier to read (no better way to get variable name).
  robot.report = t.capture_calls_and_returns(robot.report, 'robot.report')
  robot.right  = t.capture_calls_and_returns(robot.right,  'robot.right')
  robot.left   = t.capture_calls_and_returns(robot.left,   'robot.left')
  robot.place  = t.capture_calls_and_returns(robot.place,  'robot.place')
  robot.move   = t.capture_calls_and_returns(robot.move,   'robot.move')

  t.start_logging()

  print(f"table = {table}")
  robot.report(); print()

  robot.place(table, 0, 0, 'north')
  robot.left()
  robot.report()

  t.stop_logging()
  
  if t.get_log() == \
    "\n".join(
      ['''table = FlatSurface(width=5, depth=5)'''
      ,'''robot.report()'''
      ,'''None, None, None'''
      ,''' returned:'''
      ,''' None, None, None'''
      ,''''''
      ,'''robot.place(FlatSurface(width=5, depth=5), 0, 0, 'north')'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.left()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''0,0,WEST'''
      ,''' returned:'''
      ,''' 0,0,WEST'''
      ,''''''
      ]):
    print("testB PASSED")
    return True
  else:
    print("testB *FAILED*")
    return False


def testC():

  t = Tester()

  # create table and robot that will be used in testing
  table = FlatSurface()
  robot = Character()

  # Wrap methods of THIS INSTANCE of Character (to print calls to console)
  # Second arg is used because passing in the variable name 'robot'
  # makes the output easier to read (no better way to get variable name).
  robot.report = t.capture_calls_and_returns(robot.report, 'robot.report')
  robot.right  = t.capture_calls_and_returns(robot.right,  'robot.right')
  robot.left   = t.capture_calls_and_returns(robot.left,   'robot.left')
  robot.place  = t.capture_calls_and_returns(robot.place,  'robot.place')
  robot.move   = t.capture_calls_and_returns(robot.move,   'robot.move')

  t.start_logging()

  print(f"table = {table}")
  robot.report(); print()

  robot.place(table, 1, 2, 'east')
  robot.move()
  robot.move()
  robot.left()
  robot.move()
  robot.report()

  t.stop_logging()
    
  if t.get_log() == \
    "\n".join(
      ['''table = FlatSurface(width=5, depth=5)'''
      ,'''robot.report()'''
      ,'''None, None, None'''
      ,''' returned:'''
      ,''' None, None, None'''
      ,''''''
      ,'''robot.place(FlatSurface(width=5, depth=5), 1, 2, 'east')'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.move()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.move()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.left()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.move()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''3,3,NORTH'''
      ,''' returned:'''
      ,''' 3,3,NORTH'''
      ,''''''
      ]):
    print("testC PASSED")
    return True
  else:
    print("testC *FAILED*")
    return False


def testD():

  t = Tester()

  # create table and robot that will be used in testing
  table = FlatSurface(width=3, depth=3)
  robot = Character()

  # Wrap methods of THIS INSTANCE of Character (to print calls to console)
  # Second arg is used because passing in the variable name 'robot'
  # makes the output easier to read (no better way to get variable name).
  robot.report = t.capture_calls_and_returns(robot.report, 'robot.report')
  robot.right  = t.capture_calls_and_returns(robot.right,  'robot.right')
  robot.left   = t.capture_calls_and_returns(robot.left,   'robot.left')
  robot.place  = t.capture_calls_and_returns(robot.place,  'robot.place')
  robot.move   = t.capture_calls_and_returns(robot.move,   'robot.move')

  t.start_logging()

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

  t.stop_logging()
      
  if t.get_log() == \
    "\n".join(
      ['''table = FlatSurface(width=3, depth=3)'''
      ,'''robot.report()'''
      ,'''None, None, None'''
      ,''' returned:'''
      ,''' None, None, None'''
      ,''''''
      ,'''robot.right()'''
      ,''' returned:'''
      ,''' False'''
      ,'''robot.report()'''
      ,'''None, None, None'''
      ,''' returned:'''
      ,''' None, None, None'''
      ,''''''
      ,'''robot.left()'''
      ,''' returned:'''
      ,''' False'''
      ,'''robot.report()'''
      ,'''None, None, None'''
      ,''' returned:'''
      ,''' None, None, None'''
      ,''''''
      ,'''robot.move()'''
      ,''' returned:'''
      ,''' False'''
      ,'''robot.report()'''
      ,'''None, None, None'''
      ,''' returned:'''
      ,''' None, None, None'''
      ,''''''
      ,'''robot.place(FlatSurface(width=3, depth=3), 10, 10, 'NORTH')'''
      ,''' returned:'''
      ,''' False'''
      ,'''robot.report()'''
      ,'''None, None, None'''
      ,''' returned:'''
      ,''' None, None, None'''
      ,''''''
      ,'''robot.place(FlatSurface(width=3, depth=3), 2, 2, 'JUNK')'''
      ,''' returned:'''
      ,''' False'''
      ,'''robot.report()'''
      ,'''None, None, None'''
      ,''' returned:'''
      ,''' None, None, None'''
      ,''''''
      ,'''robot.place(FlatSurface(width=3, depth=3), 2, 2, 'north')'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''2,2,NORTH'''
      ,''' returned:'''
      ,''' 2,2,NORTH'''
      ,''''''
      ,'''robot.move()'''
      ,''' returned:'''
      ,''' False'''
      ,'''robot.report()'''
      ,'''2,2,NORTH'''
      ,''' returned:'''
      ,''' 2,2,NORTH'''
      ,''''''
      ,'''robot.right()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''2,2,EAST'''
      ,''' returned:'''
      ,''' 2,2,EAST'''
      ,''''''
      ,'''robot.move()'''
      ,''' returned:'''
      ,''' False'''
      ,'''robot.report()'''
      ,'''2,2,EAST'''
      ,''' returned:'''
      ,''' 2,2,EAST'''
      ,''''''
      ,'''robot.right()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''2,2,SOUTH'''
      ,''' returned:'''
      ,''' 2,2,SOUTH'''
      ,''''''
      ,'''robot.move()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''2,1,SOUTH'''
      ,''' returned:'''
      ,''' 2,1,SOUTH'''
      ,''''''
      ,'''robot.right()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''2,1,WEST'''
      ,''' returned:'''
      ,''' 2,1,WEST'''
      ,''''''
      ,'''robot.move()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''1,1,WEST'''
      ,''' returned:'''
      ,''' 1,1,WEST'''
      ,''''''
      ,'''robot.move()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''0,1,WEST'''
      ,''' returned:'''
      ,''' 0,1,WEST'''
      ,''''''
      ,'''robot.move()'''
      ,''' returned:'''
      ,''' False'''
      ,'''robot.report()'''
      ,'''0,1,WEST'''
      ,''' returned:'''
      ,''' 0,1,WEST'''
      ,''''''
      ,'''robot.left()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''0,1,SOUTH'''
      ,''' returned:'''
      ,''' 0,1,SOUTH'''
      ,''''''
      ,'''robot.move()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''0,0,SOUTH'''
      ,''' returned:'''
      ,''' 0,0,SOUTH'''
      ,''''''
      ,'''robot.move()'''
      ,''' returned:'''
      ,''' False'''
      ,'''robot.report()'''
      ,'''0,0,SOUTH'''
      ,''' returned:'''
      ,''' 0,0,SOUTH'''
      ,''''''
      ,'''robot.place(FlatSurface(width=3, depth=3), 10, 10, 'north')'''
      ,''' returned:'''
      ,''' False'''
      ,'''robot.report()'''
      ,'''0,0,SOUTH'''
      ,''' returned:'''
      ,''' 0,0,SOUTH'''
      ,''''''
      ,'''robot.place(FlatSurface(width=3, depth=3), 1, 1, 'west')'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''1,1,WEST'''
      ,''' returned:'''
      ,''' 1,1,WEST'''
      ,''''''
      ,'''robot.right()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''1,1,NORTH'''
      ,''' returned:'''
      ,''' 1,1,NORTH'''
      ,''''''
      ,'''robot.right()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''1,1,EAST'''
      ,''' returned:'''
      ,''' 1,1,EAST'''
      ,''''''
      ,'''robot.left()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''1,1,NORTH'''
      ,''' returned:'''
      ,''' 1,1,NORTH'''
      ,''''''
      ,'''robot.left()'''
      ,''' returned:'''
      ,''' True'''
      ,'''robot.report()'''
      ,'''1,1,WEST'''
      ,''' returned:'''
      ,''' 1,1,WEST'''
      ,''''''
      ,''''''
      ]):
    print("testD PASSED")
    return True
  else:
    print("testD *FAILED*")
    return False



def parse_args_using_argparse() ->  argparse.Namespace:
  '''Parse cmd line args using rules defined by
     argparse.ArgumentParser().add_argument() calls.
     (argparse makes --help txt, outputs error msgs for invalid args, etc)
     
     Returns object (argparse.Namespace) containing member variables whose
     values have been set via the parsing process.
     
     Use method operator to access args via returned object (eg args.arg1)
     Names of methods follow "long" cmd line option name,
     or "dest" parameter of .add_argument() call if supplied.
     
     https://docs.python.org/3/howto/argparse.htm
     https://docs.python.org/3/library/argparse.html#the-add-
     argument-method'''
  
  parser = argparse.ArgumentParser()
 
  # only adding one argument
  parser.add_argument('-t'                 # short
                     ,'--test_all'         # long (test_all is default
                                           #       var name in progrma)
                     ,action='store_true'  # True if flag found else False
                                           # help str shown when -h used
                     ,help='run all tests in the module. output to stdout'
                     )
 
  # Can add extra cmd line args here (as if you had passed them into main)
  # example:
  #   parser.parse_args(['--date_range','05/05/2005','06/06/2006'])
  args = parser.parse_args()                  # haven't set any extra args
 
  return args


if __name__ == "__main__":

  args = parse_args_using_argparse()
 
  if args.test_all:
    testA()
    testB()
    testC()
    testD()

#-------------------------------------------------------------------------
# END OF FILE
#-------------------------------------------------------------------------