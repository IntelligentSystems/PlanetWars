#!/usr/bin/env python
#

""" AdaptiveBot - A bot which adapts its behaviour according to the environment characteristics.
 * It changes its strategy, based on the current environment (e.g. number of neutral planets in the map,
 * number of ships, etc.). Knowing which strategy to use has to be collected beforehand.
 * This requires running a number of games of your bots, and evaluate which bot performs best for a certain environment.
 * You should then add this to the data structure (in AdaptivityMap.java). 
 * The DoTurn method can then query this data structure to know what strategy should be used for this turn. 
 * This example provides two environment variables: the number of neutral planets on the map, and the average growth
 * ratio of these neutral planets.
 * 
 * We provide a possible implementation using the hash adaptivityMap, which maps lists of integers (representing 
 * the environment) with names of bots. See AdaptivityMap.java
 * 
 * Interesting questions (you can probably come up with other questions yourself as well):
 * 1. Can you modify or extend the environment variables we use? Maybe other things are interesting other than the number of neutral planets, and the average planet growth rate of these neutral planets.
 * 2. The table in AdaptivityMap.java is filled by us (randomly) with only two simple bots. But how should the table really look like? 
 * This means you should collect data on how all your previous bots (BullyBot, RandomBot, HillclimbingBot, LookaheadBot and/or others) perform in different environments
 * 3. Can you implement your other bot implementations in AdaptiveBot.java? Currently the only strategies are BullyBot ('DoBullyBotTurn') and RandomBot ('DoRandomBotTurn').
 * Implement the bot strategies you used to fill AdaptivityMap.java here as well.
"""
# Import the PlanetWars class from the PlanetWars module.
from PlanetWars import PlanetWars
#from AdaptivityMap import AdaptivityMap
# import RandomBot
# import BullyBot

def DoTurn(pw):  
  # Retrieve environment characteristics - features you can use to decide which bot to use for that specific map.
  # Are there characteristics you want to use instead, or are there more you'd like to use? Try it out!
  # In this example we will use the number of neutral planets and the average planet growth rate of neutral planets.
  num_neutral_planets = len(pw.NeutralPlanets())
  average_growth_rate = 0
  for p in pw.NeutralPlanets():
    average_growth_rate += p.GrowthRate()
  average_growth_rate = average_growth_rate / 1 + len(pw.NeutralPlanets())

  # adaptivity_map = AdaptivityMap()
  # # Use AdaptivityMap to get the bot which matches the current environment characteristics  
  # this_turn_bot = adaptivity_map.getBestBot(num_neutral_planets, 
  #                                         average_growth_rate)
    
  # if this_turn_bot is None:
  #   # There is no entry for the specified num_neutral_planets and average_growth_rate.
  #   RandomBot.DoTurn(pw)
  # elif this_turn_bot == "BullyBot":
  #   BullyBot.DoTurn(pw)
  # elif this_turn_bot == "RandomBot":
  #   RandomBot.DoTurn(pw)
  # else:
  #   # The bot in the entry is not supported yet.
  #   RandomBot.DoTurn(pw)


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

