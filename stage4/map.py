import pygame
from constant import *
from globalvariable import *

class Map:
    def __init__(self, screen, sheet_ground):
        global g_mapdocumant
        self.sheet_ground = sheet_ground
        self.screen = screen
        for data in MAPLIST.keys():
            index = data.split(",")
            index = [int(index[0]),int(index[1])]
            if MAPLIST[data]==1 :
                g_mapdocumant["tile"].append((index[0],index[1]))
            if MAPLIST[data]==-1 :
                g_mapdocumant["spawn"] = [index[0],index[1]]

    def _get_suitable_tile(self, row, col):
        tmpimage = None
        aroundTile = [False,False,False,False]
            #T***
        if((row,col-1) in g_mapdocumant["tile"]):
            aroundTile[0]=True
        #*T**
        if((row-1,col) in g_mapdocumant["tile"]):
            aroundTile[1]=True
        #**T*
        if((row,col+1) in g_mapdocumant["tile"]):
            aroundTile[2]=True
        #***T
        if((row+1,col) in g_mapdocumant["tile"]):
            aroundTile[3]=True

        #FFFF
        if(aroundTile == [False,False,False,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[5],0)
        #TFFF
        elif(aroundTile == [True,False,False,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[3],180)
        #FTFF
        elif(aroundTile == [False,True,False,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[3],270)
        #FFTF
        elif(aroundTile == [False,False,True,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[3],0)
        #FFFT
        elif(aroundTile == [False,False,False,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[3],90)
        #TTFF
        elif(aroundTile == [True,True,False,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[2],270)
        #TFTF
        elif(aroundTile == [True,False,True,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[4],90)
        #TFFT
        elif(aroundTile == [True,False,False,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[2],180)
        #FTTF
        elif(aroundTile == [False,True,True,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[2],0)
        #FTFT
        elif(aroundTile == [False,True,False,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[4],0)
        #FFTT
        elif(aroundTile == [False,False,True,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[2],90)
        #TTTF
        elif(aroundTile == [True,True,True,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[1],270)
        #TTFT
        elif(aroundTile == [True,True,False,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[1],180)
        #TFTT
        elif(aroundTile == [True,False,True,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[1],90)
        #FTTT
        elif(aroundTile == [False,True,True,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[1],0)
        #TTTT
        elif(aroundTile == [True,True,True,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[0],0)
        
        return tmpimage

    def create_map_image(self):
        image = pygame.Surface((TILE_MAPSIZE[0]*TILE_SIZE, TILE_MAPSIZE[1]*TILE_SIZE))
        
        for (row,col) in g_mapdocumant["tile"]: 
            image.blit(self._get_suitable_tile(row,col),(row*TILE_SIZE, col*TILE_SIZE))

        image.set_colorkey((0,0,0))
        return image

    def set_ground(self, row, col, remove=False):
        if(not remove):
            g_mapdocumant["tile"].append((row,col))
        else:
            g_mapdocumant["tile"].remove((row,col))
