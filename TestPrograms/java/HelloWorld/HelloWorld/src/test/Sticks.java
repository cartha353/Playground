package test;

import java.util.Scanner;

public class Sticks {

	static Scanner input = new Scanner (System.in);
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		game();
	}

	public static void game() {
		String playAgain = "y";

		while(playAgain.equalsIgnoreCase("y")){
			System.out.println("Try not to have the last stick.");
			System.out.println("Do you want to go first? y/n");
			int numSticks = 21;
			int sticksTaken = 0;
			String answer = " ";
			boolean playersTurn = false;
			answer = input.next();
			
			if(answer.equalsIgnoreCase("y")){
				playersTurn = true;
			}
			else{
				playersTurn = false;
			}
			
			while(numSticks >= 0){
				if(playersTurn == true) {
				System.out.println(numSticks);
				System.out.println("How many sticks would you like?");
				sticksTaken = input.nextInt();
				if(sticksTaken >= 2) {
				sticksTaken = 2;
				}
				if(sticksTaken <= 1) {
				sticksTaken = 1;	
				}
				if(sticksTaken == 2) {
					numSticks = numSticks - sticksTaken;
					System.out.println("There are " + numSticks + " sticks left\n");
					if(numSticks == 1) {
						System.out.println("Congratulations! You WON!");
						break;
					}
					if(numSticks == 0) {
						System.out.println(" Sorry, you LOSE!");
						break;
					}
					playersTurn = false;
				}
				}
			}
		}
	}
	
}
