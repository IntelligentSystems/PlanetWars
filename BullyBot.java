import java.io.PrintWriter;
import java.io.StringWriter;
import java.util.*;

/* A bit smarter kind of bot, who searches for its strongest planet and then attacks the weakest planet.
 The score is computed based on the number of ships.
 */

public class BullyBot {
	public static void DoTurn(PlanetWars pw) {
		// (1) Find my strongest planet.
		Planet source = null;
		double sourceScore = Double.MIN_VALUE;
		for (Planet myPlanet : pw.MyPlanets()) {
			// skip planets with only one ship
			if (myPlanet.NumShips() <= 1)
				continue;
			
			//This score is one way of defining how 'good' my planet is. 
			double score = (double) myPlanet.NumShips();
			
			if (score > sourceScore) {
				//we want to maximize the score, so store the planet with the best score
				sourceScore = score;
				source = myPlanet;
			}
		}
		
		// (2) Find the weakest enemy or neutral planet.
		Planet dest = null;
		double destScore = Double.MAX_VALUE;
		for (Planet notMyPlanet : pw.NotMyPlanets()) {
			//This score is one way of defining how 'good' the planet is. 
			// You can change it to something different and experiment with it.
			double score = (double) (notMyPlanet.NumShips());
			//if you want to debug how the score is computed, decomment the System.err.instructions
//			System.err.println("Planet: " +notMyPlanet.PlanetID()+ " Score: "+ score);
//			System.err.flush();
			if (score < destScore) {
				//We want to select the planet with the lowest score
				destScore = score;
				dest = notMyPlanet;
			}
		}
		
		// (3) Attack!
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
			StringWriter writer = new StringWriter();
			e.printStackTrace(new PrintWriter(writer));
			String stackTrace = writer.toString();
			System.err.println(stackTrace);
			System.exit(1); //just stop now. we've got a problem
		}
	}
}
