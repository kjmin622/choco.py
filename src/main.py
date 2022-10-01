import sys, os
import pygame

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"stage2"))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"stage4"))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"stage5"))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"script"))

import stage2 as s2
import stage4 as s4
import stage5 as s5
from scriptmodule import stage_start1, stage_start2, stage1_2, stage2_3, stage_end
from scriptmodule.blackscreen import *
from mainUI import ui


pygame.init()
pygame.mixer.init()
pygame.display.set_caption("catSPY")
pygame.display.set_icon(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),"gameicon.png")))
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1024,768),0,32)

DIR_SAVE_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "game_data")
SAVE_FILE = os.path.join(DIR_SAVE_FILE, "save")

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


def emptyfunc():
    pass

def main():
    # UI & command
    while(True):
        command = ui.main(ui.init(screen, clock))
        start_stage = 0
        if(command == 1):
            pass
        elif(command == 2):
            start_stage = int(road_save_file())
        elif(command == 3): sys.exit()

        # game play
        blackscreen = BlackScreen(screen, clock)
        if(start_stage <= 0):
        #     # 스크립트 보여주고 첫번째 스테이지 실행, 그 과정에서 게임 종료되는 상황 있으면 exit 시키고, 게임 잘 끝냈으면 첫번째 스테이지 클리어 정보 저장
            result = False
            while(result is not True):
                record_save_file("1") if (stage_start1.main(stage_start1.init(screen,clock)) and blackscreen.start(1.5) and stage_start2.main(stage_start2.init(screen,clock)) and blackscreen.start(1)) else sys.exit()
                result = s5.main(s5.init(screen,clock))
                if(result == None): sys.exit()
                blackscreen.start(1)

        if(start_stage <= 1):
            # 스크립트 보여주고 두번째 스테이지 실행, 그 과정에서 게임 종료되는 상황 있으면 exit 시키고, 게임 잘 끝냈으면 두번째 스테이지 클리어 정보 저장
            record_save_file("2") if (stage1_2.main(stage1_2.init(screen,clock)) and blackscreen.start(1) and s4.main(s4.init(screen,clock))) else sys.exit()
            blackscreen.start(1)

        if(start_stage <= 2):
            # 스크립트 보여주고 세번째 스테이지 실행, 그 과정에서 게임 종료되는 상황 있으면 exit 시키고, 게임 잘 끝냈으면 엔딩 보여주기
            stage_end.main(stage_end.init(screen,clock)) if (blackscreen.start(1) and stage2_3.main(stage2_3.init(screen,clock)) and blackscreen.start(1) and s2.main(s2.init(screen,clock))) else sys.exit()
            blackscreen.start(2)
main()