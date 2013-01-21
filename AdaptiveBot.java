import java.util.*;

/* A bot which adapts its behaviour according to the environment characteristics.
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
 * 1. Can you modify or extend the environment variables we use? Maybe other things are interesting other than the number of neutral planets, and the average planet size of these neutral planets.
 * 2. The table in AdaptivityMap.java is filled by us (randomly) with only two simple bots. But how should the table really look like? 
 * This means you should collect data on how all your previous bots (BullyBot, RandomBot, HillclimbingBot, LookaheadBot and/or others) perform in different environments
 * 3. Can you implement your other bot implementations in AdaptiveBot.java? Currently the only strategies are BullyBot ('DoBullyBotTurn') and RandomBot ('DoRandomBotTurn').
 * Implement the bot strategies you used to fill AdaptivityMap.java here as well.
 */

public class AdaptiveBot {
	
	/**
	 * The main method for issuing your commands. Here, the best strategy is selected depending on the environment characteristics
	 * @param pw
	 */
	public static void DoTurn(PlanetWars pw) {
				
		//Retrieve environment characteristics
		//Are there characteristics you want to use instead, or are there more you'd like to use? Try it out!
		int neutralPlanets = pw.NeutralPlanets().size();
		int totalPlanetSize = 0;
		for (Planet p : pw.NeutralPlanets()) {
			totalPlanetSize += p.GrowthRate();
		}
		int averagePlanetSize = Math.round(totalPlanetSize/pw.NeutralPlanets().size());
			
		//Use AdaptivityMap to get the bot which matches the current environment characteristics  
		String thisTurnBot = AdaptivityMap.get(neutralPlanets, averagePlanetSize);
		
		if (thisTurnBot == null) {
			System.err.println("WARNING: You have not entered bot data for this case. Using default bot");
			DoRandomBotTurn(pw);
		} else {
			if (thisTurnBot.equals("BullyBot")) {
				System.err.println("BullyBot is going to play this turn");
				DoBullyBotTurn(pw);
			} else if (thisTurnBot.equals("RandomBot")) {
				System.err.println("RandomBot is going to play this turn");
				DoRandomBotTurn(pw);
			} else {
				System.err.println("WARNING: Adaptivity map wants " + thisTurnBot +
									" to play this turn, but this strategy is not implemented in this bot! Using default bot");
				DoRandomBotTurn(pw);
			}
		}
	}
	
	/**
	 * Implementation of the bullybot strategy (copy pasted from the regular BullyBot.java)
	 * @param pw
	 */
	public static void DoBullyBotTurn(PlanetWars pw) {
		Planet source = null;
		double sourceScore = Double.MIN_VALUE;
		//Select my strongest planet to send ships from
		for (Planet myPlanet : pw.MyPlanets()) {
			if (myPlanet.NumShips() <= 1)
				continue;
			double score = (double) myPlanet.NumShips();
			if (score > sourceScore) {
				sourceScore = score;
				source = myPlanet;
			}
		}
		
		Planet dest = null;
		double destScore = Double.MAX_VALUE;
		//Select weakest destination planet
		for (Planet notMyPlanet : pw.NotMyPlanets()) {
			double score = (double) (notMyPlanet.NumShips());

			if (score < destScore) {
				destScore = score;
				dest = notMyPlanet;
			}
		}
		
		if (source != null && dest != null) {
			pw.IssueOrder(source, dest);
		}
	}
	
	/**
	 * Implementation of the RandomBot strategy (copy pasted from the regular RandomBot.java)
	 * @param pw
	 */
	public static void DoRandomBotTurn(PlanetWars pw) {

		Random random = new Random();
		
		Planet source = null;
		List<Planet> myPlanets = pw.MyPlanets();
		//Randomly select source planet
		if (myPlanets.size() > 0) {
			Integer randomSource = random.nextInt(myPlanets.size());
			source = myPlanets.get(randomSource);
		}
		
		Planet dest = null;
		List<Planet> allPlanets = pw.NotMyPlanets();
		//Randomly select destication planets
		if (allPlanets.size() > 0) {
			Integer randomTarget = random.nextInt(allPlanets.size());
			dest = allPlanets.get(randomTarget);
		}

		if (source != null && dest != null) {
			pw.IssueOrder(source, dest);
		}
	}


	public static void main(String[] args) {
		String line = "";
		String message = "";
		int c;
		try {
			while ((c = System.in.read()) >= 0) {
				switch (c) {
				case '\n':
					if (line.equals("go")) {
						PlanetWars pw = new PlanetWars(message);
						DoTurn(pw);
						pw.FinishTurn();
						message = "";
					} else {
						message += line + "\n";
					}
					line = "";
					break;
				default:
					line += (char) c;
					break;
				}
			}
		} catch (Exception e) {

		}
	}
}
