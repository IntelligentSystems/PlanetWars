#!/usr/bin/env python
#
import sys
""" LookaheadBot - Another smarter kind of bot, which implements a minimax algorithm with look-ahead of two turns.
 * It simulates the opponent using the BullyBot strategy and simulates the possible outcomes for any
 * choice of source and destination planets in the attack. The simulated outcome states are ranked by
 * the evaluation function, which returns the most promising one.
 * 
 * Try to improve this bot. For example, you can try to answer some of this questions. 
 * Can you come up with smarter heuristics/scores for the evaluation function? 
 * What happens if you run this bot against your bot from week1? 
 * How can you change this bot to beat your week1 bot? 
 * Can you extend the bot to look ahead more than two turns? How many turns do you want to look ahead?
 * Is there a smart way to make this more efficient?
"""
# Import the PlanetWars class from the PlanetWars module.
from PlanetWars import PlanetWars

def DoTurn(pw): 
	try:
	  # The source variable will contain the planet from which we send the ships.
	  source = None 

	  # The dest variable will contain the destination, the planet to which we send the ships.
	  dest = None 

	  # We try to simulate each possible action and its outcome after two turns
	  # considering each of my planets as a possible source 
	  # and each enemy planet as a possible destination.
	  score = -999999.0

	  for my_planet in pw.MyPlanets():
		# Skip planets with only one ship
		if my_planet.NumShips() <= 1:
		  continue

		for not_my_planet in pw.NotMyPlanets():
		  # Create simulation environment - need to create one for each simulation.
		  simulated_pw = SimulatedPlanetWars(pw)

		  # (1) simulate my turn with the current couple of source and destination
		  simulated_pw.SimulateAttack(my_planet, not_my_planet)
		  # (2) simulate the growth of ships that happens in each turn
		  simulated_pw.SimulateGrowth()

		  # (3) simulate the opponent's turn, assuming that the opponent is the BullyBot   
		  # here you can add other opponents.
		  simulated_pw.SimulateBullyBot()
		  # (4) simulate the growth of ships that happens in each turn
		  simulated_pw.SimulateGrowth()
		  
		  # (5) evaluate how the current simulated state is
		  # here you can change how a state is evaluated as good
		  scoreMax = simulated_pw.EvaluateState();

		  #(6) find the planet with the maximum evaluated score
		  # this is the most promising future state
		  if scoreMax > score:        
			score = scoreMax
			source = my_planet
			dest = not_my_planet

	  #(3) Attack.
	  # If the source and dest variables contain actual planets, then 
	  # send half of the ships from source to dest.
	  if (not source is None and not dest is None) :
		pw.IssueOrder(source, dest)
	except Exception, e:
	  pw.log(e.message, e.__doc__)



class SimulatedPlanetWars:
  """ An environment that simulates the object PlanetWars.
  Has the same interface as PlanetWars, except for the Fleets.
  It allows to simulate the actions before executing them and evaluate the
  consequences, including the growth in the planets.
  """
  def __init__(self, original_pw):
    """ Constructs a PlanetWars object instance, given a string containing a
        description of a game state.
    """
    self._planets =  []
    for p in original_pw.Planets():
      self._planets.append(p.clone())

  def SimulateGrowth(self):
    """Simulates the growth of all the non neutral planets."""
    for p in self._planets:
      if p.Owner() == 0:
        # Neutral planets don't grow.
        continue
      p.NumShips(p.NumShips() + p.GrowthRate())


  def SimulateAttack(self, source, dest, player_id = 1):
    self.SimulateAttackById(source.PlanetID(), dest.PlanetID(), player_id)

  def SimulateAttackById(self, source_id, dest_id, player_id = 1):
    """Simulates the attack by player_id from planet source to planet dest."""
    source = self._planets[source_id]
    dest = self._planets[dest_id]

    if source.Owner() != player_id:
      return
    
    # Simulate attack.
    if (not source is None and not dest is None) :
      sent_ships = source.NumShips()/2
      source.NumShips(sent_ships)
      if (dest.NumShips() < sent_ships):
        # Change owner.
        dest.Owner(player_id)

      # Compute the remaining ships after the attack.
      remaining_ships = abs(dest.NumShips() - sent_ships)
      dest.NumShips(remaining_ships)

  def SimulateBullyBot(self):  
    # The source variable will contain the planet from which we send the ships.
    source = None 

    # The dest variable will contain the destination, the planet to which we send the ships.
    dest = None 

    # Put a very low value as the initial source score.
    source_score = -999999.0

    # Put a very high value as the initial dest score.
    dest_score = +999999.0

    for planet in self._planets:
      # Simulate that the opponent is a bully bot. 
      # So it uses its strongest planet to attack the other weakest planet.
      if planet.Owner() == 2:
        # Skips its planets with only one ship
        if planet.NumShips() <= 1:
          continue

        # Store the score of the current planet, i.e. the number of its ships.
        # This score is one way of defining how 'good' my planet is. 
        score_max = planet.NumShips()

        if score_max > source_score:
          source_score = score_max
          # We want to maximize the score, so store the planet with the best score.
          source = planet
      else:
        # Among the not yours, choose the weakest.
        score_min = planet.NumShips()
        if score_min < dest_score:
          dest_score = score_min
          dest = planet

    #(3) Simulate attack.
    if (not source is None and not dest is None) :
      self.SimulateAttack(source, dest, 2)

  def EvaluateState(self):
    """ Evaluates how promising a simulated state is.

    CHANGE HERE: 
    Currently it computes the total number of my ships/total number of enemy ships.
    This means that the biggest the proportion of my ships, 
    the highest the score of the evaluated state.
    You can change it to anything that makes sense, using combinations 
    of number of planets, ships or growth rate.
    Returns score of the final state of the simulation
    """   
    enemyShips = 1.0;
    myShips = 1.0;
    
    for enemy_planet in self.EnemyPlanets():
      enemyShips += enemy_planet.NumShips()
    
    for my_planet in self.MyPlanets():
      myShips += my_planet.NumShips()
    
    return myShips/enemyShips


  ###
  # The rest is a simplified version of PlanetWars.
  ###
  def NumPlanets(self):
    """ Returns the number of planets. Planets are numbered starting with 0."""
    return len(self._planets)

  def GetPlanet(self, planet_id):
    """ Returns the planet with the given planet_id. There are NumPlanets()
        planets. They are numbered starting at 0.
    """
    return self._planets[planet_id]

  def Planets(self):
    """ Returns a list of all the planets."""
    return self._planets

  def MyPlanets(self):
    """ Return a list of all the planets owned by the current player. By
        convention, the current player is always player number 1.
    """
    r = []
    for p in self._planets:
      if p.Owner() != 1:
        continue
      r.append(p)
    return r

  def NeutralPlanets(self):
    """ Return a list of all neutral planets."""
    r = []
    for p in self._planets:
      if p.Owner() != 0:
        continue
      r.append(p)
    return r

  def EnemyPlanets(self):
    """ Return a list of all the planets owned by rival players. This excludes
        planets owned by the current player, as well as neutral planets.  
    """
    r = []
    for p in self._planets:
      if p.Owner() <= 1:
        continue
      r.append(p)
    return r
 
  def NotMyPlanets(self):
    """ Return a list of all the planets that are not owned by the current
        player. This includes all enemy planets and neutral planets.   
    """
    r = []
    for p in self._planets:
      if p.Owner() == 1:
        continue
      r.append(p)
    return r

  def Distance(self, source_planet, destination_planet):
    source = self._planets[source_planet]
    destination = self._planets[destination_planet]
    dx = source.X() - destination.X()
    dy = source.Y() - destination.Y()
    return int(ceil(sqrt(dx * dx + dy * dy)))


  def IssueOrderById(self, source_planet_id, destination_planet_id):
    """ Sends an order to the game engine using the ids of the planets.
    
    An order is composed of a source planet number, a destination planet number, and a number of ships. 
    A few things to keep in mind:
           * you can issue many orders per turn if you like.
           * the planets are numbered starting at zero, not one.
           * you must own the source planet. If you break this rule, the game
             engine kicks your bot out of the game instantly.
           * you can't move more ships than are currently on the source planet.
           * the ships will take a few turns to reach their destination. Travel
             is not instant. See the Distance() function for more info.
      
    NOTICE: modified to always send half the number of ships on source planet.
    """
    stdout.write("%d %d \n" % \
     (source_planet_id, destination_planet_id))
    stdout.flush()

  def IssueOrder(self, source_planet, destination_planet):
    """ Sends an order to the game engine. 
    
    An order is composed of a source planet, a destination planet and a number of ships. 
    A few things to keep in mind:
           * the planets are numbered starting at zero, not one.
           * you must own the source planet. If you break this rule, you skip this turn
           * you can't move more ships than are currently on the source planet.
        
    NOTICE: modified to always send half the number of ships on source planet.
    """
    self.IssueOrderById(source_planet.PlanetID(), destination_planet.PlanetID())

  def IsAlive(self, player_id):
    """ Returns true if the named player owns at least one planet or fleet.
        Otherwise, the player is deemed to be dead and false is returned.
    """
    for p in self._planets:
      if p.Owner() == player_id:
        return True
    return False


  def Winner(self):
    """ Return the winner of the game.
    If the game is not yet over (ie: at least two players have planets or
    fleets remaining), returns -1. If the game is over (ie: only one player
    is left) then that player's number is returned. If there are no
    remaining players, then the game is a draw and 0 is returned.
    """
    remaining_players = []
    for p in self._planets:
      remaining_players.append(p.Owner())

    if len(remaining_players) == 0:
      return 0
    if len(remaining_players) == 1:
      return remaining_players[0]
    return -1

  def NumShips(self, player_id):
    """ Returns the number of ships that the current player has, either located
        on planets or in flight.
    """
    num_ships = 0
    for p in self._planets:
      if p.Owner() == player_id:
        num_ships += p.NumShips()

    return num_ships



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

