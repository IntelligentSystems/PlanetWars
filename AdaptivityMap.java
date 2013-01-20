import java.util.*;

public class AdaptivityMap {
	
	private static HashMap<List<Integer>, String> map = new HashMap<List<Integer>, String>();
	private static int[] neutralPlanetsKey = {0, 1, 2, 3, 4, 4, 4, 7, 8, 9};
	private static int[] planetsSizeKey = {3, 3, 3, 3, 3, 3, 3, 3, 3, 3};
	private static String[] botValue = {"RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot", "RandomBot", "BullyBot", "BullyBot", "BullyBot"};
	
	static {
		for (int i = 0; i < neutralPlanetsKey.length; i++) {
			ArrayList<Integer> a = new ArrayList<Integer>();
			a.add(neutralPlanetsKey[i]);
			a.add(planetsSizeKey[i]);
			put(a, botValue[i]);
		}
	}
	
	public static void put(ArrayList<Integer> keys, String value) {
		ArrayList<Integer> key = new ArrayList<Integer>();		
		map.put(key, value);
	}
	
	public static String get(ArrayList<Integer> keys) {		
		return map.get(keys);
	}	
}
