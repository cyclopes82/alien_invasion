class Settings:
    """A class to store all settings fro Alien Invasion"""
    
    def __init__(self) -> None:
        """"Initialize the game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (0, 0, 0)
        self.bg_color = (230, 230, 230)
        self.rocket_speed = 3.5