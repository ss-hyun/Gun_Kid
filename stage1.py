from typing import Sized
import pygame
import stage_template
import random



def move_user(ch, game):
    # ch.pos[0] += ch.move_factor
    ch.pos[0] += ch.move_factor_x 
    ch.pos[1] += ch.move_factor_y 

    #print(ch.pos[0])

    if ch.pos[1] < 208:
        ch.pos[1] = 208
    if ch.pos[1] > 620:
         ch.pos[1] = 620
    if ch.pos[0] < 8.5:
        ch.pos[0] = 8.5
    if ch.pos[0] > 860:
        ch.pos[0] = 860

    #if ch.curr_state == 0 and ch.pos[0] > game.display_size[0]:
        #ch.pos[0] = -ch.size[ch.curr_state][0]
    #elif ch.curr_state == 1 and ch.pos[0] + ch.size[ch.curr_state][0] < 0:
        #ch.pos[0] = game.display_size[0]
    speed = 3
    if ch.move_state == True:
        ch.change_count += 1
    
    key_up = False

    for event in game.event_key:
        if event.type == pygame.KEYDOWN:

            ch.move_state = True
                                    
            if event.key == pygame.K_LEFT:
              ch.move_factor_x = -speed            
              ch.curr_state = 6
                  
            elif event.key == pygame.K_RIGHT:
              ch.move_factor_x = speed              
              ch.curr_state = 4

            elif event.key == pygame.K_UP:
              key_up = True
              ch.move_factor_y = -speed              
              ch.curr_state = 10         
                           
            elif event.key == pygame.K_DOWN:
                
                ch.move_factor_y = speed            
                ch.curr_state = 8


        if event.type == pygame.KEYUP:
            ch.move_state = False
            if event.key == pygame.K_UP:               
                ch.move_factor_y = 0
                ch.curr_state = 3

            elif event.key == pygame.K_DOWN:
                ch.move_factor_y = 0
                ch.curr_state = 2


            elif event.key == pygame.K_RIGHT:
                ch.move_factor_x = 0
                ch.curr_state = 0

            elif event.key == pygame.K_LEFT:
                ch.move_factor_x = 0
                ch.curr_state = 1


    if ch.move_state == True:
        if ch.change_count == 10:
            if ch.curr_state % 2 == 0:
               ch.curr_state += 1
            else:
               ch.curr_state -= 1

        if ch.change_count == 20:
            ch.change_count = 0 
    

def user_start(ch, game):
    ch.pos = [ (game.display_size[0]-ch.size[ch.curr_state][0])/2, game.display_size[1]-ch.size[ch.curr_state][1]-10 ]

def user_resize(ch):
    # image_boss = pygame.image.load("/image/exboss.svg")
    l = len(ch.image)
    for i in range(0, l):
        ch.image[i] = pygame.transform.rotozoom(ch.image[i], 0, 0.3)
        # size variable change
        ch.size[i] = ch.image[i].get_rect().size

def user_attack(ch, game):
    for event in game.event_key:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            game.user_attack.append(stage_template.Spherical_Attack(ch.atk_image, 5, ch.pos, 5, user_atk_move))

def user_atk_move(atk, game):
    return 1

# def boss_moving(ch, game):
#     ch.pos[0] += ch.move_factor
#     if ch.pos[0] + ch.size[ch.curr_state][0] > game.display_size[0]:
#         ch.move_factor = -random.randint(0,10)
#     elif ch.pos[0] < 0:
#         ch.move_factor = random.randint(0,10)


def boss_start(ch, game):
    ch.pos = [ (game.display_size[0]-ch.size[ch.curr_state][0])/2, ch.size[ch.curr_state][1]-270 ]


def boss_resize(ch):
    # image_boss = pygame.image.load("/image/exboss.svg")
    l = len(ch.image)
    for i in range(0, l):
        ch.image[i] = pygame.transform.rotozoom(ch.image[i], 0, 1.3)
        # size variable change
        ch.size[i] = ch.image[i].get_rect().size


def arm_move(ch, game):
    ch.change_count += 1
    if ch.change_count == ch.state_change_speed:
        ch.change_count= 0
        if ch.curr_state == 0: ch.change_direc = True
        elif ch.curr_state == ch.state_num-1: ch.change_direc = False
        ch.curr_state += 1 if ch.change_direc else -1


def arm_trans(ch):
    for i in range(0, ch.state_num):
        ch.image[i] = pygame.transform.rotozoom(ch.image[i], 0, 0.65)


def arm1_start(ch, game):
    ch.pos = [ 0, 0 ]
    ch.curr_state = 1


def arm2_start(ch, game):
    ch.pos = [ 500, 0 ]
    ch.curr_state = 1


def laser_field1_start(ch, game):
    ch.pos = [ 0, game.display_size[1] - ch.size[ch.curr_state][1] ]


def laser_field2_start(ch, game):
    ch.pos = [ game.display_size[0] - ch.size[ch.curr_state][0], game.display_size[1] - ch.size[ch.curr_state][1] ]


def stage1(name, path, fps, speed):
    bg_image = pygame.image.load(path + "/image/boss_stage_test.jpg")
    # character info : (name, relative path list, function list, attack image path, group)
    # # name : character name
    # # relative path list : Characters have various states. Images of all possible conditions.
    # # function list : A function of all actions that can be done as a character, including initialization.
    # #                 [move, positioning, attack, image transform] - if it doesn't exist -> None
    # # group : There are user groups(0) and monster groups(1) in the game.

    ch_info_list = [ ("user", [ "/image/오른1.png", "/image/왼1.png", "/image/앞1.png", "/image/뒤1.png" ,"/image/오른2.png", "/image/오른3.png", "/image/왼2.png","/image/왼3.png","/image/앞2.png", "/image/앞3.png", "/image/뒤2.png","/image/뒤3.png"], [ move_user, user_start, user_attack, user_resize ], "/image/bullet.png", 0),
                     ("boss", [ "/image/exboss.svg" ], [ None, boss_start, None, boss_resize ], None, 1),                    
                     ("boss_arm1", [ "/image/forceps_1.png", "/image/forceps_2.png" ], [ arm_move, arm2_start, None, arm_trans ], None, 1),
                     ("boss_arm2", [ "/image/r_forceps_1.png", "/image/r_forceps_2.png" ], [ arm_move, arm1_start, None, arm_trans ], None, 1),
                    ]

    stage1_1 = stage_template.Stage(name, 1-1, path, fps, speed, bg_image, ch_info_list)
    stage1_1.run()
    bg_image = pygame.image.load(path + "/image/stage1_background.jpg")

    ch_info_list = ["user", "boss",
                     ("laser_field1", [ "/image/laser_field.jpg" ], [ None, laser_field1_start, None, None ], None, 1),
                     ("laser_field2", [ "/image/laser_field.jpg" ], [ None, laser_field2_start, None, None ], None, 1)]

    stage1_2 = stage_template.Stage(name, 1-2, path, fps, speed, bg_image, ch_info_list, stage1_1)
    stage1_2.run()
    
