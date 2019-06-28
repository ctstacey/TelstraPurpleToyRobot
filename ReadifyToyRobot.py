# standard map grid: run before you jump (ie. x,y)

class robot

  vector (direction)
  position (tuple (0,1), None == off table)

  (square) board size

  place()
    validate then set
  move()
    validate then set
  left()
    rotate vector 90 left
  right()
    rotate vector 90 right
  output()
    print position and direction
  
  position add(position, vector)
    return position + vector

main
  instructions (board size)
  loop (REPL loop)
    get input
    parse
      if valid parse
        call method
        output the return
      else output debug msg
  
















