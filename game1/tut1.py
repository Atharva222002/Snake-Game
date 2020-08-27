import pygame
import os
from random import randint
x=pygame.init()
pygame.mixer.init()
window=pygame.display.set_mode((1200,500))
bg=pygame.image.load('start.jfif')
bg=pygame.transform.scale(bg,(1200,500)).convert_alpha()
pygame.display.update()
font=pygame.font.SysFont(None,55)
def plot_snake(list1):
    for j in list1:
        for x,y in list1:
            pygame.draw.rect(window, (255, 0, 255), [x, y, 15, 15])
def screen_text(text,x,y):
    text_screen=font.render(text,True,(255,0,0))
    window.blit(text_screen,[x,y])
clock=pygame.time.Clock()
def welcome():
    quit_game = False
    while not quit_game:
        window.fill((255,255,255))
        window.blit(bg,(0,0))
        screen_text('press space to start',450,400)
        for event in pygame.event.get():
            if event.type==12:
                quit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    window.blit(bg,(0,0))

                    pygame.mixer.music.load('nagin.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(30)
def gameloop():
        x = 50
        y = 60
        velx = 0
        vely = 0
        cord = []
        length = 1
        quit_game = False
        game_over = False
        foodx = randint(20, 1190)
        foody = randint(20, 480)
        fps = 30
        score = 0
        if not os.path.exists('highscore'):
            fhand=open('highscore','w')
            fhand.write('0')
        fhand = open('highscore')
        for line in fhand:
            highscore = int(line)
        while not quit_game:
            if game_over:
                bg = pygame.image.load('over.png')
                bg = pygame.transform.scale(bg, (1200, 500)).convert_alpha()
                window.fill((255, 255, 255))
                window.blit(bg,(0,0))
                screen_text('SCORE : '+str(score), 500, 400)
                screen_text('Enter to continue', 450,450)
                for i in pygame.event.get():
                    if i.type==pygame.KEYDOWN:
                        if i.key==pygame.K_RETURN:
                            welcome()
                    if i.type==12:
                        quit_game=True


            else:
                bg = pygame.image.load('snake.jfif')
                bg = pygame.transform.scale(bg, (1200, 500)).convert_alpha()
                for i in pygame.event.get():
                    if i.type == 12:
                        quit_game=True
                    if i.type==pygame.KEYDOWN:
                        if i.key==pygame.K_RIGHT:
                            velx=15
                            vely=0
                    if i.type==pygame.KEYDOWN:
                        if i.key==pygame.K_LEFT:
                            velx=-15
                            vely=0
                    if i.type==pygame.KEYDOWN:
                        if i.key==pygame.K_DOWN:
                            velx=0
                            vely=15
                    if i.type==pygame.KEYDOWN:
                        if i.key==pygame.K_UP:
                            velx=0
                            vely=-15
                x+=velx
                y+=vely
                window.fill((255, 255, 255))
                window.blit(bg,(0,0))
                if score>highscore:
                    highscore=score
                    fhand=open('highscore','w')
                    fhand.write(str(highscore))
                screen_text('Score : ' + str(score), 5, 5)
                screen_text('HIGH-SCORE : ' + str(highscore), 800, 5)
                if abs(foodx-x)<=9 and abs(foody-y)<=9:
                    score+=10
                    foodx = randint(20, 1180)
                    foody = randint(20, 480)
                    length+=1
                if [x,y] in cord[:-1]:
                    game_over=True
                    pygame.mixer.music.load('expo.mp3')
                    pygame.mixer.music.play()
                cord.append([x,y])
                if x > 1200 or x < 0 or y > 500 or y < 0:
                    game_over=True
                    pygame.mixer.music.load('expo.mp3')
                    pygame.mixer.music.play()
                cord=cord[len(cord) - length:]
                plot_snake(cord)
                pygame.draw.rect(window, (255, 0, 0), [foodx, foody, 15, 15])
            pygame.display.update()
            clock.tick(fps)
        pygame.quit()
        quit()
welcome()