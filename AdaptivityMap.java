import java.util.*;

public class AdaptivityMap {
	
	private static HashMap<List<Integer>, String> map = new HashMap<List<Integer>, String>();
	
	
	public static void put(ArrayList<Integer> keys, String value) {
		ArrayList<Integer> key = new ArrayList<Integer>();		
		map.put(key, value);
	}
	
	public static String get(ArrayList<Integer> keys) {		
		return map.get(keys);
	}	
}
