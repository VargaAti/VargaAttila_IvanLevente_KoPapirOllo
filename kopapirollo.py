"""
Task Description: Rock, Paper, Scissors Game
Create a Rock, Paper, Scissors game where the player competes against the computer. The program should meet the following requirements:

Task Requirements:
1. Introduction:
The program should greet the player when it starts, e.g., "Welcome to Rock, Paper, Scissors!".

2. Player's Choice:
The player should input their choice (e.g., "rock", "paper", or "scissors") as a text string.

"o". Computer's Choice:
The program should randomly select one of the three options: "rock", "paper", or "scissors".

4. Determine the Winner:
The program should decide if the player won, lost, or tied based on the rules of the game: "Rock" beats scissors but loses to paper. "Paper" beats rock but loses to scissors. "Scissors" beat paper but lose to rock.

5.Track Results:
The program should keep a running tally of how many games the player has won, lost, or tied: Increment the "wins" counter for a victory. Increment the "losses" counter for a defeat. Increment the "ties" counter for a draw.

6. Option to Play Again:
After each round, the program should ask the player if they want to play another game: If the answer is "y", the game continues. If the answer is "n", the program ends.

7. End of Game:
Before exiting, the program should display the total results (wins, losses, ties).

Example Execution:
Welcome to Rock, Paper, Scissors!
Choose your character: Rock, Paper, Scissors ->rock
Computer's choice: paper
You lost
Wins: 0, Losses: 1, Ties: 0
Do you want to play again? (y/n) y
Bonus Ideas for Improvement:
Make the input case-insensitive (e.g., "rock" and "ROCK" should both work).
Add error handling to prompt the user for a valid input if they enter something incorrect.
Display a farewell message with a summary, such as: "Thanks for playing! Final score: "o" wins, 2 losses, 1 tie."
Challenge: Modify the game to allow a "best of N" format, where the first to win a certain number of rounds (e.g., 5) becomes the overall winner!
"""
import random as r

felhasznalo = input("Kő (k), papír (p) vagy olló (o)? ")

l_betu = ["k", "p", "o"]
gep_szam = r.choice(l_betu)


print(f"Gép: {gep_szam}")
if felhasznalo == "k" and gep_szam == k:
    print("Döntetlen")
elif felhasznalo == "k" and gep_szam == p:
    print("Vesztettél!")
elif felhasznalo == "k" and gep_szam == "o":
    print("Nyertél!")

if felhasznalo == "p" and gep_szam == k:
    print("Nyertél!")
elif felhasznalo == "p" and gep_szam == p:
    print("Döntetlen!")
elif felhasznalo == "p" and gep_szam == "o":
    print("Vesztettél")

if felhasznalo == "o" and gep_szam == k:
    print("Vesztettél!")
elif felhasznalo == "o" and gep_szam == p:
    print("Nyertél!")
elif felhasznalo == "o" and gep_szam == "o":
    print("Döntetlen!")