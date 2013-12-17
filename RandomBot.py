#!/usr/bin/env python
#

"""
// RandomBot - an example bot that picks up one of his planets and send half of the ships 
// from that planet to a random target planet.
//
// Not a very clever bot, but showcases the functions that can be used.
// Overcommented for educational purposes.
"""

# Import the module that implements the random number generator.
import random
# Import the PlanetWars class from the PlanetWars module.
from PlanetWars import PlanetWars

# DoTurn: function that gets called every turn.
# This is where to implement the strategies.
def DoTurn(pw):  

  # The source variable will contain the planet from which we send the ships.
  source = None 

  # The dest variable will contain the destination, the planet to which we send the ships.
  dest = None 

  # Get a list of all my planets and store it in the variable my_planets. 
  my_planets = pw.MyPlanets()

  # The number of planets I own is the length of this list.
  number_of_my_planets = len(my_planets)

  # If I own at least a planet, i.e. there is at least one planet in the list.
  if number_of_my_planets > 0:
    # Pick the index of a planet at random by choosing a random integer
    # between 0 (index of the first element of the list) and the last index
    # (number_of_my_planets - 1).
    random_my_planet_index = random.randint(0, number_of_my_planets - 1)
    # Get the planet at that index.
    source = my_planets[random_my_planet_index]

  # Get a list of all planets which are either enemy or neutral (not mine).
  not_my_planets = pw.NotMyPlanets()

  # The number of planets I don't own is the length of this list.
  number_of_not_my_planets = len(not_my_planets)

  # If there is at least a planet I don't own, i.e. there is at least one planet in the list.
  if number_of_not_my_planets > 0:
    # Pick the index of a planet at random by choosing a random integer
    # between 0 (index of the first element of the list) and the last index
    # (number_of_my_planets - 1).
    random_not_my_planet_index = random.randint(0, number_of_not_my_planets - 1)
    # Get the planet at that index.
    dest = not_my_planets[random_not_my_planet_index]

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
