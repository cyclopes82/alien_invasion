class Settings:
    """A class to store all settings for Raindrops"""
    
    def __init__(self) -> None:
        """"Initialize the game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (0, 0, 0)
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        
        #Bullet Settings
        self.bullet_speed = 2.0
        self.bullet_width = 2
        self.bullet_height = 16
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        #Alein Settings
        self.raindrop_speed = 1.0
        self.raindrop_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1