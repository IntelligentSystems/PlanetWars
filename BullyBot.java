import java.util.*;

/* A bit smarter kind of bot, who searches for its strongest planet and then attacks the weakest planet.
 The score is computed based on the number of ships and the inverse of the growth rate.
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
			double score = (double) myPlanet.NumShips() / (1 + myPlanet.GrowthRate());
			
				
			if (score > sourceScore) {
				//we want to maximize the score, so store the planet with the best score
				sourceScore = score;
				source = myPlanet;
			}
		}
		
		
		
		// (2) Find the weakest enemy or neutral planet.
		Planet dest = null;
		double destScore = Double.MIN_VALUE;
		for (Planet notMyPlanet : pw.NotMyPlanets()) {
			//This score is one way of defining how 'bad' the other planet is. 
			//Avoiding dividing by zero.
			double score = (double) (1 + notMyPlanet.GrowthRate()) / (notMyPlanet.NumShips()+Double.MIN_VALUE);
			//if you want to debug how the score is computed, decomment the System.err.instructions
//			System.err.println("Planet: " +notMyPlanet.PlanetID()+ " Score: "+ score);
//			System.err.flush();
			if (score > destScore) {
				//The way the score is defined, is that the weaker a planet is, the higher the score. 
				//So again, we want to select the planet with the best score
				destScore = score;
				dest = notMyPlanet;
			}
		}
		
//		System.err.println("Selected Planet: " +dest.PlanetID()+ " Score: "+ destScore);
//		System.err.flush();
		
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
			// Owned.
		}
	}
}
