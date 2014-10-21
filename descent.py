## This is intended to be the file run by the end user.

from assets.Game import Descent_Game

def main():
    players = int(raw_input("How many players?"))
    

    overlord = "n"
    while(overlord.upper() != "Y"):
        overlord = raw_input("Will you be supplying a human overlord?")

    game = Descent_Game(players,overlord)    

if __name__ == "__main__":
    main()
