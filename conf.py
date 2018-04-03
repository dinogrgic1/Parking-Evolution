import os

# default constants
WIDTH = 1360
HEIGHT = 720
FPS = 30
CAPTION = 'Parking Evolution'

# RGB of most basic colors
BLACK = (0  , 0  , 0  )
WHITE = (255, 255, 255)
RED =   (255, 0  , 0  )
GREEN = (0  , 255, 0  )
BLUE =  (0  , 0  , 255)

# set up assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'assets')
sound_folder = os.path.join(game_folder, 'sounds')