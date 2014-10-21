class Descent_Game():
    """The overall initial game state"""
    def __init__(self, many, overlordYN):
        self.game_ID = ""
        self.players = many
        self.who = 0
        self.lives = 0
        self.overlord = overlordYN
        self.SKELETONS = []
        self.SORCERORS = []

        for i in range(0,self.players):
            
