import pygame
import random
import sys
import os

pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

DIR_PATH = os.path.dirname(__file__)
DIR_IMAGE = os.path.join(DIR_PATH, 'image')

current_time = 0

password = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(password)
password = password[:5]

button_list = []

class Button:
    image = pygame.image.load(os.path.join(DIR_IMAGE,'button.png')).convert()
    size = image.get_rect()
    width = size[0]
    height = size[1]
    
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    def draw_button(self):
        screen.blit(self.image, (self.x_pos, self.y_pos))

    def button_press(self):
        self.image = pygame.image.load(os.path.join(DIR_IMAGE,'button_press.png')).convert()
        self.draw_button()

for i in range(10):
    button_list.append(Button(104 + (i%5)*184, 203 + (i//5)*283))

game_font = pygame.font.Font(None,40)

pygame.display.set_caption("ChoCo")

background = pygame.image.load(os.path.join(DIR_IMAGE,'floor.png')).convert()

character = pygame.image.load(os.path.join(DIR_IMAGE,'character_1.png')).convert()
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = SCREEN_WIDTH/2
character_y_pos = SCREEN_HEIGHT - character_height

dogs = []
for _ in range(4):
    dog = pygame.image.load(os.path.join(DIR_IMAGE,'dog.png')).convert()
    dog_size = dog.get_rect().size
    dog_width = dog_size[0]
    dog_height = dog_size[1]
    dog_x_pos = random.randint(0,SCREEN_WIDTH)
    dog_y_pos = random.randint(0,SCREEN_HEIGHT)
    dogs.append([dog,dog_width,dog_height,dog_x_pos,dog_y_pos])
    
portal = pygame.image.load(os.path.join(DIR_IMAGE,'portal.png')).convert()
portal_size = portal.get_rect().size
portal_width = portal_size[0]
portal_height = portal_size[1]
portal_x_pos = SCREEN_WIDTH - portal_width
portal_y_pos = 0

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

gameover = False
running = True
enter = False

while running:
    screen.blit(background,(0,0))
    dt = clock.tick(60)
    if not enter:#포탈 입장 전
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
        elif character_x_pos > SCREEN_WIDTH - character_width:
            character_x_pos = SCREEN_WIDTH - character_width
        if character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > SCREEN_HEIGHT - character_height:
            character_y_pos = SCREEN_HEIGHT - character_height

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
            elif dog[3] > SCREEN_WIDTH - dog[1]:
                dog[3] = SCREEN_WIDTH - dog[1]
            if dog[4] < 0:
                dog[4] = 0
            elif dog[4] > SCREEN_HEIGHT - dog[2]:
                dog[4] = SCREEN_HEIGHT - dog[2]
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
            
    else:#포탈 입장 후
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for button in button_list:
            button.draw_button()
            
        current_time += 1
        if current_time == 20:
            button_list[password[0]].button_press()
            current_time = 0
            
        
    pygame.display.update()

if gameover:
    msg = game_font.render("Game Over",True,(255,255,0)) # 노란색
    msg_rect = msg.get_rect(center=(int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2)))
    screen.blit(msg,msg_rect)
    pygame.display.update()
    pygame.time.delay(1000)

pygame.quit()
sys.exit()
