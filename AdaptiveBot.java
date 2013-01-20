import java.util.*;

/* A more generic kind of bot, which adapts its behaviour according to the environment status.
 * It needs some previously collected knowledge about the environment (e.g. number of neutral planets in the map,
 * number of ships, etc.) and what strategy performs better in these conditions. This knowledge has to be 
 * collected beforehand (running a number of simulations of your bots in these environments) and manually coded 
 * in a data structure. Then, the DoTurn method can use it to know what strategy should be used in this turn. In 
 * this example we provide two environment variables: number of neutral planets in the map, and average growth
 * ratio of all planets in the map.
 * 
 * We provide a possible implementation using the hash adaptivityMap, which maps lists of integers (representing 
 * the environmnent) with names of bots. Its first entry can be read as: "if the map has 0 neutral planets and
 * the average growth rate is 3, then use a RandomBot this turn".  
 * 
 * Complete this bot:
 * 1. Extend the list of environment variables you consider interesting for adaptivity
 * 2. Collect data on how all your previous bots (BullyBot, RandomBot, HillclimbingBot, LookaheadBot and/or others) 
 * 	  perform in all maps
 * 3. Code these data in adaptivityMap
 * 4. Complete the DoTurn method, adding all your previous bot implementations 
 */

public class AdaptiveBot {
	
	private static HashMap<List<Integer>, String> adaptivityMap = new HashMap<List<Integer>, String>();
	private static int[] neutralPlanetsKey = {0, 1, 2, 3, 4, 4, 4, 7, 8, 9};
	private static int[] planetsSizeKey = {3, 3, 3, 3, 3, 3, 3, 3, 3, 3};
	private static String[] botValue = {"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot", "BullyBot"};
	static {
		for (int i = 0; i < neutralPlanetsKey.length; i++) {
			ArrayList<Integer> key = new ArrayList<Integer>();
			key.add(neutralPlanetsKey[i]);
			key.add(planetsSizeKey[i]);
			adaptivityMap.put(key, botValue[i]);
		}
	}
		
	public static void DoTurn(PlanetWars pw) {
				
		//Retrieve environment status
		int neutralPlanets = pw.NeutralPlanets().size();
		int planetsSize = 0;
		for (Planet p : pw.Planets()) {
			planetsSize += p.GrowthRate();
		}
		planetsSize = planetsSize/pw.Planets().size();
			
		//Access adaptivity map using this status as key
		ArrayList<Integer> turnKey = new ArrayList<Integer>();
		turnKey.add(neutralPlanets);
		turnKey.add(planetsSize);
		String thisTurnBot = adaptivityMap.get(turnKey);
		
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
				System.err.println("WARNING: Adaptivity wants " + thisTurnBot +
									" to play this turn, but not implemented. Using default bot");
				DoRandomBotTurn(pw);
			}
		}
	}
	
	public static void DoBullyBotTurn(PlanetWars pw) {
		Planet source = null;
		double sourceScore = Double.MIN_VALUE;
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
	
	public static void DoRandomBotTurn(PlanetWars pw) {

		Random random = new Random();
		Planet source = null;
		List<Planet> myPlanets = pw.MyPlanets();

		if (myPlanets.size() > 0) {
			Integer randomSource = random.nextInt(myPlanets.size());
			source = myPlanets.get(randomSource);
		}
		
		Planet dest = null;

		List<Planet> allPlanets = pw.NotMyPlanets();

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
