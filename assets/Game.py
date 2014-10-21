class Descent_Game():
    """The overall initial game state"""
    def __init__(self):
        self.game_ID = ""       # game instance name (for user connection)
        self.game_pass = ""     # game instance password
        self.players = 0        # number of human players
        self.who = 0            # player whose turn it is
        self.lives = 0          # number of life tokens to start with
        self.overlord = True    # is the overlord a human? (for eventual AI)

        # the following track the number of available monsters of each type
        self.BEASTMAN = {'normal': 0, 'master': 0}
        self.RAZORWING = {'normal': 0, 'master': 0}
        self.SKELETON = {'normal': 0, 'master': 0}
        self.OGRE = {'normal': 0, 'master': 0}
        self.HELLHOUND = {'normal': 0, 'master': 0}
        self.MANTICORE = {'normal': 0, 'master': 0}
        self.SORCERER = {'normal': 0, 'master': 0}
        self.DRAGON = {'normal': 0, 'master': 0}
        self.NAGA = {'normal': 0, 'master': 0}
        self.BANESPIDER = {'normal': 0, 'master': 0}
        self.DEMON = {'normal': 0, 'master': 0}