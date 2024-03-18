import pygame as pg
import datetime

pg.init()
RES = WIDTH, HEIGHT = 1200, 1000
midle = WIDTH // 2, HEIGHT // 2

screen = pg.display.set_mode(RES)
clock = pg.time.Clock()

pg.display.set_caption("Mickey Clock")

sec = pg.image.load("/Users/Дастан/Desktop/pp2/lab7/task01/left.png").convert_alpha()
minute = pg.image.load("/Users/Дастан/Desktop/pp2/lab7/task01/right.png").convert_alpha()
rectsec = sec.get_rect()
rectmin = minute.get_rect()
rectsec.center = midle 
rectmin.center = midle


background = pg.image.load("/Users/Дастан/Desktop/pp2/lab7/task01/mm.png").convert_alpha()
background = pg.transform.scale(background, (WIDTH, HEIGHT))  
run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    time_now = datetime.datetime.now()
    minute_time = time_now.minute + 10
    second_time = time_now.second

  
    angle1 = -minute_time * 6 
    leg1 = pg.transform.rotate(minute, angle1)
    rect1 = leg1.get_rect(center=rectmin.center)

    angle2 = -second_time * 6  
    leg2 = pg.transform.rotate(sec, angle2)
    rect2 = leg2.get_rect(center=rectsec.center)

    
    screen.blit(background, (0, 0))
    screen.blit(leg1, rect1)
    screen.blit(leg2, rect2)

    pg.display.flip()
    clock.tick(60)
