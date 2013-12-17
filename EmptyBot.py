#!/usr/bin/env python
#

""" EmptyBot - a skeleton of a bot that you can modify.
Overcommented for educational purposes.
"""
# Import the PlanetWars class from the PlanetWars module.
from PlanetWars import PlanetWars

def DoTurn(pw):  
  """ Function that gets called every turn.
  This is where to implement the strategies.

  Notice that a PlanetWars object called pw is passed as a parameter which you could use
  if you want to know what this object does, then read PlanetWars.py.
  """

  # The source variable will contain the planet from which we send the ships.
  # Create a source planet, if you want to know what this object does, then read the Planet
  # class in PlanetWars.py.
  source = None 

  # The dest variable will contain the destination, the planet to which we send the ships.
  dest = None 

  #(1) Implement an algorithm to determine the source planet to send your ships from
  #... code here

  #(2) Implement an algorithm to deterimen the destination planet to send your ships to
  #... code here
  
  #(3) Attack.
  # If the source and dest variables contain actual planets, then 
  # send half of the ships from source to dest.
  if (not source is None and not dest is None) :
    pw.IssueOrder(source, dest)


# Don't change from this point on. Also not necessary to understand all the details.
# Machinery that reads the status of the game and puts it into PlanetWars.
# It calls DoTurn.
def main():
  map_data = ''
  while(True):
    current_line = raw_input()
    if len(current_line) >= 2 and current_line.startswith("go"):
      pw = PlanetWars(map_data)
      DoTurn(pw)
      pw.FinishTurn()
      map_data = ''
    else:
      map_data += current_line + '\n'


if __name__ == '__main__':
  try:
    import psyco
    psyco.full()
  except ImportError:
    pass
  try:
    main()
  except KeyboardInterrupt:
    print 'ctrl-c, leaving ...'
