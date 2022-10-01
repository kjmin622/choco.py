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

DIR_SAVE_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "game_data")
SAVE_FILE = os.path.join(DIR_SAVE_FILE, "save.txt")

print(SAVE_FILE)

def road_save_file():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            stage_save = f.read()
            f.close
            return stage_save
    else:
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            f.write("0")
            f.close
            return "0"

def record_save_file(save_data):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        f.write(save_data)
        f.close


def excute(current_stage):
    if current_stage == "0":
        return_value = s1.stage1_main(s1.stage1_init(screen,clock))
        if return_value == True:
            current_stage = "1"
            record_save_file(current_stage)
            excute(current_stage)
        else:
            sys.exit()

    elif current_stage == "1":
        return_value = s2.stage2_main(s2.stage2_init(screen,clock))
        if return_value == True:
            current_stage = "2"
            record_save_file(current_stage)
            excute(current_stage)
        else:
            sys.exit()

    elif current_stage == "2":
        return_value = s3.stage3_main(s3.stage3_init(screen,clock))
        if return_value == True:
            current_stage ="3"
        else:
            sys.exit()


def main():
    current_stage = road_save_file()
    excute(current_stage)

main()