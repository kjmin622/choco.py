# 상수 모음
import os
DIR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
DIR_IMAGE = os.path.join(DIR_PATH, 'image')
DIR_SOUND = os.path.join(DIR_PATH, 'sound')
DIR_FONT = os.path.join(DIR_PATH, 'font')

WINDOW_SIZE = (1024,768)
TILE_SIZE = 8

TILE_MAPSIZE = (2000,500)

BACKGROUND_COLOR = (27,25,25)

DEFAULT_FONT_NAME = "Sunflower-Medium.ttf"

PLAYER_ROWSPEED = 2
PLAYER_MAXCOLSPEED = 3
PLAYER_COLACCELERATE = 0.2

PLAYER_NAME1 = "냥이1"
PLAYER_NAME2 = "냥이2"

TESTMODE = False