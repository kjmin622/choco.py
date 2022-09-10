import pygame
import random
import sys
import os

pygame.init()

screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))

DIR_PATH = os.path.dirname(__file__)
DIR_IMAGE = os.path.join(DIR_PATH, 'image')

game_font = pygame.font.Font(None,40)

pygame.display.set_caption("ChoCo")

background = pygame.image.load(os.path.join(DIR_IMAGE,'floor.png')).convert()

character = pygame.image.load(os.path.join(DIR_IMAGE,'character_1.png')).convert()
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2
character_y_pos = screen_height - character_height

dogs = []
for _ in range(4):
    dog = pygame.image.load(os.path.join(DIR_IMAGE,'dog.png')).convert()
    dog_size = dog.get_rect().size
    dog_width = dog_size[0]
    dog_height = dog_size[1]
    dog_x_pos = random.randint(0,screen_width)
    dog_y_pos = random.randint(0,screen_height)
    dogs.append([dog,dog_width,dog_height,dog_x_pos,dog_y_pos])
    
portal = pygame.image.load(os.path.join(DIR_IMAGE,'portal.png')).convert()
portal_size = portal.get_rect().size
portal_width = portal_size[0]
portal_height = portal_size[1]
portal_x_pos = screen_width - portal_width
portal_y_pos = 0

buttons = []
for i in range(10):
    button = pygame.image.load(os.path.join(DIR_IMAGE,'button.png')).convert()
    button_size = button.get_rect().size
    button_width = button_size[0]
    button_height = button_size[1]
    button_x_pos = 104 + (i%5)*184
    button_y_pos = 203 + (i//5)*283
    buttons.append([button,button_width,button_height,button_x_pos,button_y_pos])

lights = []
for i in range(5):
    light = pygame.image.load(os.path.join(DIR_IMAGE,'light.png')).convert()
    light_size = light.get_rect().size
    light_width = light_size[0]
    light_height = light_size[1]
    light_x_pos = 432 + i*30
    light_y_pos = 50
    lights.append([light,light_width,light_height,light_x_pos,light_y_pos])

to_x = 0
to_y = 0

clock = pygame.time.Clock()

password = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(password)
password = password[:5]

gameover = False
running = True
enter = False
show1 = False
show2 = False
show3 = False
show4 = False
show5 = False

start_ticks = pygame.time.get_ticks()
total_time = 5

def button_reset(num):
    for i in range(num):
        lights[i][0] = pygame.image.load(os.path.join(DIR_IMAGE,'light_clear.png')).convert()
    for button in buttons:
            screen.blit(button[0],(button[3],button[4]))
    for light in lights:
        screen.blit(light[0],(light[3],light[4]))
    pygame.display.update()
    

def show_password(num):
    for now in password[:num+1]:
        pygame.time.delay(200)
        buttons[now][0] = pygame.image.load(os.path.join(DIR_IMAGE,'button_press.png')).convert()
        screen.blit(buttons[now][0],(buttons[now][3],buttons[now][4]))
        pygame.display.update()
        pygame.time.delay(200)

    for now in password[:num+1]:
        buttons[now][0] = pygame.image.load(os.path.join(DIR_IMAGE,'button.png')).convert()
        screen.blit(buttons[now][0],(buttons[now][3],buttons[now][4]))
        pygame.display.update()
    
while running:
    dt = clock.tick(60)
    screen.blit(background,(0,0))
            
    if not enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    to_x -= 1
                elif event.key == pygame.K_d:
                    to_x += 1
                elif event.key == pygame.K_w:
                    to_y -= 1
                elif event.key == pygame.K_s:
                     to_y += 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    to_x = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    to_y = 0
        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width
        if character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height

        character_x_pos += to_x*dt
        character_y_pos += to_y*dt

        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        portal_rect = portal.get_rect()
        portal_rect.left = portal_x_pos
        portal_rect.top = portal_y_pos

        for dog in dogs:
            if dog[3] < 0:
                dog[3] = 0
            elif dog[3] > screen_width - dog[1]:
                dog[3] = screen_width - dog[1]
            if dog[4] < 0:
                dog[4] = 0
            elif dog[4] > screen_height - dog[2]:
                dog[4] = screen_height - dog[2]
            dir = [[1,0],[-1,0],[0,1],[0,-1]]
            now_dir = random.choice(dir)
            dog[3] += 3*now_dir[0]
            dog[4] += 3*now_dir[1]

            dog_rect = dog[0].get_rect()
            dog_rect.left = dog[3]
            dog_rect.top = dog[4]

            if character_rect.colliderect(dog_rect):
                running = False
                gameover = True
        
        if character_rect.colliderect(portal_rect):
            background = pygame.image.load(os.path.join(DIR_IMAGE,'next.png')).convert()
            dogs = []
            enter = True
        screen.blit(character,(character_x_pos,character_y_pos))
        screen.blit(portal,(portal_x_pos,portal_y_pos))
        for dog in dogs:
            screen.blit(dog[0],(dog[3],dog[4]))
            
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(buttons)):
                    button_rect = buttons[i][0].get_rect()
                    button_rect.left = buttons[i][3]
                    button_rect.top = buttons[i][4]
                    if button_rect.collidepoint(event.pos):
                        pressed.append(i)
                        print(i)
        
        pressed = []
        
        if not show1:
            button_reset(0)
            show_password(0)
            show1 = True

        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

        pygame.time.delay(1000)

        if total_time - elapsed_time <= 0 or pressed != password[:1]:
            running = False
            gameover = True
        
        pressed = []

        if not show2:
            button_reset(1)
            show_password(1)
            show2 = True

        elapsed_time = (pygame.time.get_ticks() - elapsed_time*1000) / 1000

        pygame.time.delay(1000)

        if total_time - elapsed_time <= 0 or pressed != password[:2]:
            running = False
            gameover = True

        pressed = []
        
        if not show3:
            button_reset(2)
            show_password(2)
            show3 = True

        elapsed_time = (pygame.time.get_ticks() - elapsed_time*1000) / 1000

        pygame.time.delay(1000)

        if total_time - elapsed_time <= 0 or pressed != password[:3]:
            running = False
            gameover = True

        pressed = []
        
        if not show4:
            button_reset(3)
            show_password(3)
            show1 = True

        elapsed_time = (pygame.time.get_ticks() - elapsed_time*1000) / 1000

        pygame.time.delay(1000)

        if total_time - elapsed_time <= 0 or pressed != password[:4]:
            running = False
            gameover = True

        pressed = []
        
        if not show5:
            button_reset(4)
            show_password(4)
            show5 = True

        elapsed_time = (pygame.time.get_ticks() - elapsed_time*1000) / 1000

        pygame.time.delay(1000)

        if total_time - elapsed_time <= 0 or pressed != password:
            running = False
            gameover = True

    pygame.display.update()

if gameover:
    msg = game_font.render("Game Over",True,(255,255,0)) # 노란색
    msg_rect = msg.get_rect(center=(int(screen_width/2),int(screen_height/2)))
    screen.blit(msg,msg_rect)
    pygame.display.update()
    pygame.time.delay(1000)

pygame.quit()
sys.exit()
