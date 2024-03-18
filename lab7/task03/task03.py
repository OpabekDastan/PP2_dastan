import time
import pygame as pg
pg.init()

q1 = "/Users/Дастан/Desktop/pp2/lab7/task03/Another.mp3"
q2 = "/Users/Дастан/Desktop/pp2/lab7/task03/Bohemian.mp3"
q3 = "/Users/Дастан/Desktop/pp2/lab7/task03/Champions.mp3"
sc = pg.display.set_mode((800, 600))
pg.display.set_caption("Cpotiphy")
clock = pg.time.Clock()
bitethedust = pg.mixer.music.load(q3)
champions = pg.mixer.music.load(q2)
bohemian = pg.mixer.music.load(q1)
musicList = [q1, q2, q3]
pg.mixer.music.play(-1)
background = pg.image.load("/Users/Дастан/Desktop/pp2/lab7/task03/background.png")
background = pg.transform.scale(background, (800, 600))
sc.blit(background, (0, 0))
flPlay = False
run = True
index = 0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                flPlay = not flPlay
                if flPlay:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key == pg.K_RIGHT:
                
                index += 1
                if index == len(musicList):
                    index = 0
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(musicList)-1
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()


    pg.display.flip()
    clock.tick(60)