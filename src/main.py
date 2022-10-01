import sys, os
import pygame

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"stage2"))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"stage4"))

import stage1 as s1
import stage2 as s2
import stage3 as s3


pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1024,768),0,32)

def road_save_file():
    if os.path.exists("game_data/save.txt"):
        with open("game_data/save.txt", "r", encoding="utf-8") as f:
            stage_save = f.read()
            f.close
            return stage_save
    else:
        with open("game_data/save.txt", "w", encoding="utf-8") as f:
            f.write("0")
            f.close
            return "0"

def record_save_file(save_data):
    with open("game_data/save.txt", "w", encoding="utf-8") as f:
        f.write(save_data)
        f.close


def excute(current_stage):
    if current_stage == "0":
        if s1.stage1_main(s1.stage4_init(screen,clock)):
            record_save_file(current_stage)
            excute(current_stage)
        else:
            sys.exit()
    elif current_stage == "1":
        if s2.stage2_main(s2.stage2_init(screen,clock)):
            record_save_file(current_stage)
            excute(current_stage)
        else:
            sys.exit()
    elif current_stage == "2":
        if s3.stage5_main(s3.stage5_init(screen,clock)):
            current_stage += 1
        else:
            sys.exit()


def main():
    current_stage = road_save_file()
    excute(current_stage)

main()

    
            



