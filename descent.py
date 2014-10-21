## This is intended to be the file run by the end user.

from assets.Game import Descent_Game

def main():
    
    game = Descent_Game()
    game.players = int(raw_input("How many players?"))

    game.overlord = False
    

if __name__ == "__main__":
    main()
