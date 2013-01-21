import java.util.*;

/* An adaptivity map implementation.
 * It maps lists of integers with strings using a HashMap. A HashMap is an implementation of an associative
 * array (see http://en.wikipedia.org/wiki/Hash_table for further reference).
 * The list of integers (keys of the hash) represents the environment parameters you want to use for adaptivity. The mapped
 * strings (values of the hash) represent the bot that performs better under those environment parameters.
 * In this example, we provide two environment parameters (number of neutral planets, average growth ratio), and we make them
 * match to a specific bot. The first upper left element of the botValue can be read as: "given that the map has 0 neutral planets
 * and that the average growth rate of all planets in the map is 0, then user the RandomBot"; the next element to the right: "given
 * 0 neutral planets and an average growth of 1, use BullyBot; one down the upper left: given 1 neutral planet and average growth
 * 0, use RandomBot". The given example is random and does not have to be smart at all. We recommend start editing this array to 
 * get used to adaptivity and discover which other features would make your bot more smartly adaptive. * 
 */

public class AdaptivityMap {
	
	private static HashMap<List<Integer>, String> map = new HashMap<List<Integer>, String>();
	private static final int MAX_NEUTRAL_PLANETS = 25;
	private static final int MAX_PLANET_SIZE = 5;
	private static String[] botValue = {"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",
										"BullyBot", "RandomBot", "BullyBot", "BullyBot", "RandomBot",
										"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",
										"RandomBot", "BullyBot", "RandomBot", "RandomBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "BullyBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "RandomBot", "RandomBot",
										"BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",
										"BullyBot", "BullyBot", "RandomBot", "RandomBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "BullyBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "RandomBot", "RandomBot",
										"RandomBot", "BullyBot", "RandomBot", "RandomBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",
										"BullyBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",
										"RandomBot", "BullyBot", "RandomBot", "RandomBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",
										"BullyBot", "RandomBot", "BullyBot", "RandomBot", "BullyBot",
										"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot",
										"BullyBot", "RandomBot", "BullyBot", "BullyBot", "BullyBot"};
	
	static {
		for (int i = 0; i < MAX_NEUTRAL_PLANETS; i++) {
			for (int j = 0; j < MAX_PLANET_SIZE; j++) {
				put(i, j, botValue[i*MAX_PLANET_SIZE + j]);
			}
			
		}
	}
	
	public static void put(ArrayList<Integer> keys, String value) {		
		map.put(keys, value);
	}
	
	public static void put(int neutralPlanets, int planetsSize, String botValue) {
		ArrayList<Integer> keys = new ArrayList<Integer>();
		keys.add(neutralPlanets);
		keys.add(planetsSize);
		put(keys, botValue);
	}
	
	public static String get(ArrayList<Integer> keys) {		
		return map.get(keys);
	}
	
	public static String get(int neutralPlanets, int planetsSize) {
		ArrayList<Integer> keys = new ArrayList<Integer>();
		keys.add(neutralPlanets);
		keys.add(planetsSize);
		return map.get(keys);
	}
	
}
