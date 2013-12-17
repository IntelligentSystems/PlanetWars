#!/usr/bin/env python
#

""" BullyBot - A bit smarter kind of bot, who searches for its strongest planet and then attacks the weakest planet.
The score is computed based on the number of ships.
"""
# Import the PlanetWars class from the PlanetWars module.
from PlanetWars import PlanetWars

def DoTurn(pw):  
  # The source variable will contain the planet from which we send the ships.
  source = None 

  # The dest variable will contain the destination, the planet to which we send the ships.
  dest = None 

  # (1) Find my strongest planet (highest score).
  # Put a very low value as the initial source score.
  source_score = -999999.0

  for my_planet in pw.MyPlanets():
    # Skip planets with only one ship
    if my_planet.NumShips() <= 1:
      continue

    # Store the score of the current planet, i.e. the number of its ships.
    # This score is one way of defining how 'good' my planet is. 
    score = my_planet.NumShips()

    if score > source_score:
      source_score = score
      # We want to maximize the score, so store the planet with the best score.
      source = my_planet

  # (2) Find the weakest enemy or neutral planet (lowest score).
  # Put a very high value as the initial dest score.
  dest_score = +999999.0

  for not_my_planet in pw.NotMyPlanets():
    # Store the score of the current planet, i.e. the number of its ships.
    score = not_my_planet.NumShips()

    if score < dest_score:
      dest_score = score
      # We want to minimize the score, so store the planet with the lowest score.
      dest = not_my_planet

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
