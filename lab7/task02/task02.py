import pygame


pygame.init()


screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Moving Ball")

# Define the colors
white = (255, 255, 255)
red = (255, 0, 0)


x = screen_width // 2
y = screen_height // 2
velocity = 20


def draw_ball(x, y):
    pygame.draw.circle(screen, red, (x, y), 25)


running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= velocity
            elif event.key == pygame.K_DOWN:
                y += velocity
            elif event.key == pygame.K_LEFT:
                x -= velocity
            elif event.key == pygame.K_RIGHT:
                x += velocity

    if x < 25:
        x = 25
    elif x > screen_width - 25:
        x = screen_width - 25
    if y < 25:
        y = 25
    elif y > screen_height - 25:
        y = screen_height - 25

   
    screen.fill(white)

    
    draw_ball(x, y)

    
    pygame.display.update()

pygame.quit()