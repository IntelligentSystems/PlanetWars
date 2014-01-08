#!/usr/bin/env python
#

""" PlanetWars machinery - You do not need to worry about anything in this file. 

This is just helper code that does the boring stuff for you, so you can focus on the
interesting stuff. That being said, you're welcome to change anything in
this file if you know what you're doing.

NOTICE: modified to always send half the number of ships on source planet.
"""

from math import ceil, sqrt
import sys

class Fleet:
  """ A fleet is a group of ships flying from one planet to the other.
  For Week 1 we don't need it.
  """
  def __init__(self, owner, num_ships, source_planet = -1, destination_planet = -1, \
   total_trip_length = -1, turns_remaining = -1):
    self._owner = owner
    self._num_ships = num_ships
    self._source_planet = source_planet
    self._destination_planet = destination_planet
    self._total_trip_length = total_trip_length
    self._turns_remaining = turns_remaining

  def Owner(self):
    return self._owner

  def NumShips(self):
    return self._num_ships

  def SourcePlanet(self):
    return self._source_planet

  def DestinationPlanet(self):
    return self._destination_planet

  def TotalTripLength(self):
    return self._total_trip_length

  def TurnsRemaining(self):
    return self._turns_remaining

  def TimeStep(self):
    """ Subtracts one turn remaining. Call this function to make the fleet get
        one turn closer to its destination.
    """
    if self._turns_remaining > 0:
      self._turns_remaining = self._turns_remaining - 1
    else:
      self._turns_remaining = 0

  def compareTo(self, other_fleet):
    return self._num_ships - other_fleet.NumShips()

  def clone(self):
    return Fleet(self._owner, self._num_ships, self._source_planet, \
      self._destination_planet, self._total_trip_length, self._turns_remaining)

class Planet:
  """ Class that represents a planet. """
  def __init__(self, planet_id, owner, num_ships, growth_rate, x, y):
    self._planet_id = planet_id
    self._owner = owner
    self._num_ships = num_ships
    self._growth_rate = growth_rate
    # coordinates in the space.
    self._x = x
    self._y = y

  def PlanetID(self):
    return self._planet_id

  def Owner(self, new_owner=None):
    if new_owner == None:
      return self._owner
    self._owner = new_owner

  def NumShips(self, new_num_ships=None):
    if new_num_ships == None:
      return self._num_ships
    self._num_ships = new_num_ships
    
  def GrowthRate(self):
    return self._growth_rate

  def X(self):
    """ X coordinate in the space. """
    return self._x

  def Y(self):
    """ Y coordinate in the space. """
    return self._y

  def AddShips(self, amount):
    self._num_ships += amount

  def RemoveShips(self, amount):
    self._num_ships -= amount

  def clone(self):
    """ Clone the current planet: return another Planet instance with the same attributes."""
    return Planet(self._planet_id, self._owner, self._num_ships, \
      self._growth_rate, self._x, self._y)

class PlanetWars:
  def __init__(self, gameState):
    """ Constructs a PlanetWars object instance, given a string containing a
        description of a game state.
    """
    self._planets = []
    self._fleets = []
    self.ParseGameState(gameState)

  def NumPlanets(self):
    """ Returns the number of planets. Planets are numbered starting with 0."""
    return len(self._planets)

  def GetPlanet(self, planet_id):
    """ Returns the planet with the given planet_id. There are NumPlanets()
        planets. They are numbered starting at 0.
    """
    return self._planets[planet_id]

  def NumFleets(self):
    """ Returns the number of fleets (groups of ships moving)."""
    return len(self._fleets)

  def GetFleet(self, fleet_id):
    """ Returns the fleet with the given fleet_id. Fleets are numbered starting
        with 0. There are NumFleets() fleets. fleet_id's are not consistent from
        one turn to the next.
    """
    return self._fleets[fleet_id]

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

  def Fleets(self):
    """ Return a list of all the fleets. """
    return self._fleets

  def MyFleets(self):
    """ Return a list of all the fleets owned by the current player. """
    r = []
    for f in self._fleets:
      if f.Owner() != 1:
        continue
      r.append(f)
    return r

  def EnemyFleets(self):
    """ Return a list of all the fleets owned by enemy players. """
    r = []
    for f in self._fleets:
      if f.Owner() <= 1:
        continue
      r.append(f)
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
    sys.stdout.write("%d %d \n" % \
     (source_planet_id, destination_planet_id))
    sys.stdout.flush()

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

  def FinishTurn(self):
    """ Sends the game engine a message to let it know that we're done sending
        orders. This signifies the end of our turn.
    """
    sys.stdout.write("go\n")
    sys.stdout.flush()

  def IsAlive(self, player_id):
    """ Returns true if the named player owns at least one planet or fleet.
        Otherwise, the player is deemed to be dead and false is returned.
    """
    for p in self._planets:
      if p.Owner() == player_id:
        return True
    for f in self._fleets:
      if f.Owner() == player_id:
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

    for f in self._fleets:
      remaining_players.append(f.Owner())

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

    for f in self._fleets:
      if f.Owner() == player_id:
        num_ships += f.NumShips()

    return num_ships


  def ParseGameState(self, s):
    """ Parses a game state from a string. On success, returns 1. On failure, 
        returns 0.
    """
    self._planets = []
    self._fleets = []
    lines = s.split("\n")
    planet_id = 0

    for line in lines:
      line = line.split("#")[0] # remove comments
      tokens = line.split(" ")
      if len(tokens) == 1:
        continue
      if tokens[0] == "P":
        if len(tokens) != 6:
          return 0
        p = Planet(planet_id, # The ID of this planet
                   int(tokens[3]), # Owner
                   int(tokens[4]), # Num ships
                   int(tokens[5]), # Growth rate
                   float(tokens[1]), # X
                   float(tokens[2])) # Y
        planet_id += 1
        self._planets.append(p)
      elif tokens[0] == "F":
        if len(tokens) != 7:
          return 0
        f = Fleet(int(tokens[1]), # Owner
                  int(tokens[2]), # Num ships
                  int(tokens[3]), # Source
                  int(tokens[4]), # Destination
                  int(tokens[5]), # Total trip length
                  int(tokens[6])) # Turns remaining
        self._fleets.append(f)
      else:
        return 0
    return 1
  
  def __str__(self):
    self.ToString()

  def log(self, *args):
    lst=[]
    for arg in args:
	  lst.append(str(arg))
    lst.append('\n')#needed, otherwise line won't show in console
    sys.stderr.write(' '.join(lst))
  
  def ToString(self):
    """ Print the string representing the planets and fleets.   
    """
    s = ''
    for p in self._planets:
      s += "P %f %f %d %d %d\n" % \
       (p.X(), p.Y(), p.Owner(), p.NumShips(), p.GrowthRate())
    # for f in self._fleets:
    #   s += "F %d %d %d %d %d %d\n" % \
    #    (f.Owner(), f.NumShips(), f.SourcePlanet(), f.DestinationPlanet(), \
    #     f.TotalTripLength(), f.TurnsRemaining())
    return s


