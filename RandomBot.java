import java.util.*;

public class RandomBot {
	public static void DoTurn(PlanetWars pw) {
		
		// (1) Pick one of my planets at random.
		Random r = new Random();
		Planet source = null;
		List<Planet> p = pw.MyPlanets();
		if (p.size() > 0) {
			source = p.get(r.nextInt(p.size()));
		}
		
		// (2) Pick a target planet at random.
		Planet dest = null;
		p = pw.Planets();
		if (p.size() > 0) {
			dest = p.get(r.nextInt(p.size()));
		}
		
		// (3) Send half the ships from source to dest.
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
			// Owned.
		}
	}
}
