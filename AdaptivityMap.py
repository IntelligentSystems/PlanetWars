#!/usr/bin/env python
#

""" AdaptivityMap - An adaptivity map implementation.
 * 
 * In this example, we provide two environment parameters (number of neutral planets, average growth ratio of neutral planets), and we match them to a specific bot. 
 * The first upper left element of the botValue can be read as: "given that the map has 0 neutral planets
 * and that the average growth rate of the neutral planets in the map is 0, then use the RandomBot"; the next element to the right: "given
 * 0 neutral planets and an average growth of 1, use BullyBot; one down the upper left: given 1 neutral planet and average growth
 * 0, use RandomBot". The given example is random and does not have to be smart at all. We recommend start editing this array to 
 * get used to adaptivity and discover which other features would make your bot more smartly adaptive. * 
 */
"""
# Import the PlanetWars class from the PlanetWars module.
from PlanetWars import PlanetWars

# Two tunable parameters, the maximum number of neutral planets (depends on the map, currently no map has more than 25) 
# and the maximum growth rate of a planet (in the current game is 5).
# If you wish to change the dimension of the matrix, change also these two values.
MAX_NEUTRAL_PLANETS = 25;
MAX_GROWTH_RATE = 5;

# A matrix in two dimensions: the columns represent different planet growth rates (range: 0-5)
# the rows the number of neutral planets (range: 0-25).
# The values are completely random, you are encourage to fit in the table your own data.
# Possibly you can also add your other bots you developed.
botValue = [ # average growth ratio (planet size) of    
#   0             1          2           3            4           5
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot", # 0 neutral planets on the map
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot",# 1 neutral planet
"BullyBot", "RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",# 2 neutral planets
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "RandomBot",# ...
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot",
"RandomBot", "BullyBot", "RandomBot", "RandomBot", "BullyBot", "RandomBot",
"RandomBot", "BullyBot", "BullyBot", "BullyBot", "BullyBot", "BullyBot",
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "RandomBot", "RandomBot",
"BullyBot",  "BullyBot", "RandomBot", "BullyBot", "BullyBot", "BullyBot",
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "RandomBot",
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot",
"BullyBot",  "BullyBot", "RandomBot", "RandomBot", "BullyBot", "RandomBot",
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot",
"RandomBot", "BullyBot", "BullyBot", "BullyBot", "BullyBot", "BullyBot",
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "RandomBot",
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "RandomBot", "BullyBot",
"RandomBot", "BullyBot", "RandomBot", "RandomBot", "BullyBot", "RandomBot",
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot",
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot",
"BullyBot",  "BullyBot", "BullyBot", "RandomBot", "BullyBot", "RandomBot",
"RandomBot", "BullyBot", "RandomBot", "RandomBot", "BullyBot", "BullyBot",
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot",
"BullyBot",  "RandomBot", "BullyBot", "RandomBot", "BullyBot", "RandomBot",
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot",
"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot",
"BullyBot",  "RandomBot", "BullyBot", "BullyBot", "BullyBot", "BullyBot"] # 25 neutral planets on the map

class AdaptivityMap():
	def __init__(self):
		self.adaptive_map = {}
		# Use the botvalue table and rewrite it into the map for ease of access.
		for num_neutral_planets in range(0, MAX_NEUTRAL_PLANETS + 1):
		  for average_growth_rate in range(0, MAX_GROWTH_RATE + 1):
		    if (num_neutral_planets not in self.adaptive_map):
		    	self.adaptive_map[num_neutral_planets] = {}
		    self.adaptive_map[num_neutral_planets][average_growth_rate] = \
		    	botValue[num_neutral_planets * (MAX_GROWTH_RATE + 1) + average_growth_rate]

	def getBestBot (num_neutral_planets, average_growth_rate):
		if (num_neutral_planets not in self.adaptive_map):
			return None
		return self.adaptive_map[num_neutral_planets][average_growth_rate]
  