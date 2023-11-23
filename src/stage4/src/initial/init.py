import os, sys, pygame
from pygame.locals import *
import pygame.mixer
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from data.constant import *
import data.globalvariable as g
from data.constant import *
import data.globalvariable as g
from map.map import *
import data.eventdata as eventdata
import engine.sprite as sprite
import event.button as button
import event.script as script



def stage4_init(screen, clock):
    screen_scaled = pygame.Surface((WINDOW_SIZE[0]/4,WINDOW_SIZE[1]/4))

    spriteSheet_player = sprite.SpriteSheet("character.png", 16,16,8,8,12)
    spriteSheet_player2 = sprite.SpriteSheet("character2.png",16,16,8,8,12)
    spriteSheet_ground = sprite.SpriteSheet("ground.png",8,8,48,8,6)
    spriteSheet_object = sprite.SpriteSheet("object.png", 8,8,80,8,10)

    spr_player = {}
    spr_player["stay"] = sprite.create_sprite_set(spriteSheet_player, [0])
    spr_player['run'] = sprite.create_sprite_set(spriteSheet_player, 1, 8)
    spr_player['jump'] = sprite.create_sprite_set(spriteSheet_player, [9, 10, 11])

    spr_player2 = {}
    spr_player2["stay"] = sprite.create_sprite_set(spriteSheet_player2, [0])
    spr_player2['run'] = sprite.create_sprite_set(spriteSheet_player2, 1, 8)
    spr_player2['jump'] = sprite.create_sprite_set(spriteSheet_player2, [9, 10, 11])

    mapManager = Map(screen_scaled, spriteSheet_ground)

    # 최초 스폰 위치
    player_spawn_x, player_spawn_y = g.g_mapdocumant["spawn"]
    mapImage = mapManager.create_map_image()

    # 엔드포인트 리스트
    endpoint_list = [pygame.Rect((point[0]*TILE_SIZE, point[1]*TILE_SIZE), (8,8)) for point in g.g_mapdocumant["endpoint"]]

    # event list
    eventList = []
    scriptEventList = []

    # event func
    ## button_ground
    for event in eventdata.g_button_ground_list:
        eventfunc = button.FuncSetGround(mapManager, event[2], event[3], g.g_mapdocumant)
        if(not event[4]):
            eventList.append(button.Button(pygame.Rect((event[0]*TILE_SIZE, event[1]*TILE_SIZE), (8,8)), spriteSheet_object, eventfunc.appendfunc, eventfunc.removefunc))
        else:
            eventList.append(button.Button(pygame.Rect((event[0]*TILE_SIZE, event[1]*TILE_SIZE), (8,8)), spriteSheet_object, eventfunc.removefunc, eventfunc.appendfunc))
            
    ## script event
    for event in eventdata.g_script_text_list:
        eventfunc = script.ScriptEvent(pygame.Rect((event[0]*TILE_SIZE, event[1]*TILE_SIZE),(8,8)), spriteSheet_object, event[2])
        scriptEventList.append(eventfunc)
        eventList.append(eventfunc)

    # event image
    event_image = pygame.Surface((TILE_MAPSIZE[0]*TILE_SIZE, TILE_MAPSIZE[1]*TILE_SIZE))
    for event in eventList:
        event_image = event.event_image(event_image)

    keyLeft = False
    keyRight = False
    keyLeft2 = False
    keyRight2 = False

    player_sponOK = True
    player2_sponOK = True

    camera_scroll = [player_spawn_x * TILE_SIZE-WINDOW_SIZE[0]/2, player_spawn_y * TILE_SIZE-WINDOW_SIZE[1]/2]

    player_rect = pygame.Rect((player_spawn_x * TILE_SIZE, player_spawn_y * TILE_SIZE), (6,14))
    player_movement = [0,0]
    player_vspeed = 0
    player_flytime = 0

    player2_rect = pygame.Rect((player_spawn_x * TILE_SIZE+8, player_spawn_y * TILE_SIZE), (6,14))
    player2_movement = [0,0]
    player2_vspeed = 0
    player2_flytime = 0

    player_action = "stay"
    player_frame = 0
    player_frameSpeed = 1
    player_frameTimer = 0
    player_flip = False
    player_animationMode = True
    player_walkSoundToggle = False
    player_walkSoundTimer = 0

    player2_action = "stay"
    player2_frame = 0
    player2_frameSpeed = 1
    player2_frameTimer = 0
    player2_flip = False
    player2_animationMode = True
    player2_walkSoundToggle = False
    player2_walkSoundTimer = 0

    camera_scroll_standard = 1

    button_on_sound = pygame.mixer.Sound(os.path.join(DIR_SOUND,"ButtonOn.wav"))
    button_off_sound = pygame.mixer.Sound(os.path.join(DIR_SOUND,"ButtonOff.wav"))
    jump_sound = pygame.mixer.Sound(os.path.join(DIR_SOUND,"Jump.wav"))
    jump_sound2 = pygame.mixer.Sound(os.path.join(DIR_SOUND,"Jump.wav"))
    back_music = pygame.mixer.Sound(os.path.join(DIR_SOUND,"backmusic.wav"))
    return {'screen':screen, 'clock':clock, 'screen_scaled':screen_scaled, 'spriteSheet_player':spriteSheet_player, 'spriteSheet_player2':spriteSheet_player2, 'spriteSheet_ground':spriteSheet_ground, 'spriteSheet_object':spriteSheet_object, 'spr_player':spr_player, 'spr_player2':spr_player2, 'mapManager':mapManager, 'player_spawn_x':player_spawn_x, 'player_spawn_y':player_spawn_y, 'mapImage':mapImage, 'endpoint_list':endpoint_list, 'eventList':eventList, 'scriptEventList':scriptEventList, 'event_image':event_image, 'keyLeft':keyLeft, 'keyRight':keyRight, 'keyLeft2':keyLeft2, 'keyRight2':keyRight2, 'player_sponOK':player_sponOK, 'player2_sponOK':player2_sponOK, 'camera_scroll':camera_scroll, 'player_rect':player_rect, 'player_movement':player_movement, 'player_vspeed':player_vspeed, 'player_flytime':player_flytime, 'player2_rect':player2_rect, 'player2_movement':player2_movement, 'player2_vspeed':player2_vspeed, 'player2_flytime':player2_flytime, 'player_action':player_action, 'player_frame':player_frame, 'player_frameSpeed':player_frameSpeed, 'player_frameTimer':player_frameTimer, 'player_flip':player_flip, 'player_animationMode':player_animationMode, 'player_walkSoundToggle':player_walkSoundToggle, 'player_walkSoundTimer':player_walkSoundTimer, 'player2_action':player2_action, 'player2_frame':player2_frame, 'player2_frameSpeed':player2_frameSpeed, 'player2_frameTimer':player2_frameTimer, 'player2_flip':player2_flip, 'player2_animationMode':player2_animationMode, 'player2_walkSoundToggle':player2_walkSoundToggle, 'player2_walkSoundTimer':player2_walkSoundTimer, 'camera_scroll_standard':camera_scroll_standard,'button_on_sound':button_on_sound, 'button_off_sound':button_off_sound, 'jump_sound':jump_sound, 'jump_sound2':jump_sound2, 'back_music':back_music}    