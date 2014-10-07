class Descent_Game():
    """The overall initial game state"""
    def __init__(self, many):
        self.game_ID = ""
        self.players = many
        self.who = 0
        self.lives = 0
        self.SKELETONS = []
        self.SORCERORS = []