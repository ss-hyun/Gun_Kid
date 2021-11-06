import os
import sys
import pygame
import button
import stage1

pygame.init

# loading 
path = os.path.dirname(os.path.realpath(__file__))
gname_image = pygame.image.load(path + "/image/start_gname.jpg")
bg_image = pygame.image.load(path + "/image/start_background.jpg")
bt_image_st1_up = pygame.image.load(path + "/image/start_button_stage1_up.jpg")
bt_image_st1_down = pygame.image.load(path + "/image/start_button_stage1_down.jpg")

# setting
display_size = bg_image.get_rect().size
name = "game"
speed = 100
running = True
gname_pos = ((display_size[0]-gname_image.get_rect().size[0])/2, (display_size[1]-gname_image.get_rect().size[1])/2)
bt_st1_pos = ((display_size[0]-bt_image_st1_up.get_rect().size[0])/2, display_size[1]*3/4-bt_image_st1_up.get_rect().size[1]/2)

fps = pygame.time.Clock()
event_key = []
event_mouse = []
button_list = []
button_list.append(button.Button(bt_image_st1_up, bt_image_st1_down, bt_st1_pos, stage1.stage1, name, path, fps, speed))

while running:
    background = pygame.display.set_mode(display_size)
    pygame.display.set_caption(name)
    fps.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            event_mouse.append(pygame.mouse.get_pos())
            for b in button_list:
                b.click()
        elif event.type == pygame.KEYDOWN:
            event_key.append(event)

    
    background.blit(bg_image, (0, 0))
    background.blit(gname_image, gname_pos)
    for b in button_list:
        b.draw(background)
    pygame.display.update()
    event_mouse.clear()
    event_key.clear()