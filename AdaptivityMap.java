import java.util.*;

/* An adaptivity map implementation.
 * It maps lists of integers with 
 * 
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
