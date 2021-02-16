import pygame,random
from pygame.locals import *
import time
pygame.init()
# colors
grey = (117,120,118)
dark_red = (255,0,0)
light_red = (170,0,0)
light_blue = (0,255,240)
dark_blue = (0,100,183)
dark_green = (0,255,0)
light_green = (0,100,0)
# global variable
screen_width,screen_height = 800,600
fps = 40
clock = pygame.time.Clock()
cars = {}
score = 0
#  booleans
pause = False
welcome_bool = True
control_run = False
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("carGame")

# loading assests
start_bg =pygame.transform.scale( pygame.image.load("img/background.jpg"),(screen_width,screen_height))
pause_bg =pygame.transform.scale( pygame.image.load("img/background2.jpg"),(screen_width,screen_height))
green_strip =pygame.transform.scale( pygame.image.load("img/green.jpg"),(screen_width // 5,screen_height)).convert_alpha()
strip =pygame.image.load("img/strip.jpg").convert_alpha()
white_strip = pygame.transform.scale( strip,(strip.get_rect().width,screen_height)).convert_alpha()
yellow_strip =pygame.image.load("img/yellow.jpg").convert_alpha()

cars["car"] = (
    pygame.image.load("img/car0.jpg").convert_alpha(),
    pygame.image.load("img/car1.jpg").convert_alpha(),
    pygame.image.load("img/car2.jpg").convert_alpha(),
    pygame.image.load("img/car3.jpg").convert_alpha(),
    pygame.image.load("img/car4.jpg").convert_alpha(),
    pygame.image.load("img/car5.jpg").convert_alpha(),
    pygame.image.load("img/car6.jpg").convert_alpha(),
)
green_width = green_strip.get_rect().width
player_width =cars["car"][1].get_rect().width
player_height =  cars["car"][1].get_rect().height
playerx = screen_width//2 - cars["car"][6].get_rect().centerx 
playery = screen_height - player_width
# welcome and pause screen
def welcome():
    global pause,welcome_bool,control_run
    
    
    while pause or welcome_bool or control_run:
        # a = screen.blit(pause_bg,(0,0)) if pause else screen.blit(start_bg,(0,0))
        if control_run:
            screen.blit(pause_bg,(0,0))
        if welcome_bool or pause:
            screen.blit(start_bg,(0,0))
            screen_text("CAR GAME",(0,0,0),screen_width//2,screen_height//2.3,100)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()   
                exit()
        if welcome_bool:
            button("PLAY",(screen_width//6.5)-(70//2),screen_height//1.3,70,30,light_red,dark_red,"play")
            button("CONTROLS",(screen_width//2.191780821917808)-(120/4),screen_height//1.3,120,30,light_blue,dark_blue,"control")
            button("QUIT",((screen_width - screen_width//6.5)- 70)+(70//2),screen_height//1.3,70,30,light_green,dark_green,"quit")
        elif pause:
            button("RESUME",(screen_width//6.5)-(90//2),screen_height//1.3,90,30,light_red,dark_red,"resume")
            button("RESTART",(screen_width//2.191780821917808)-(90/4),screen_height//1.3,90,30,light_blue,dark_blue,"play")
            button("HOME SCREEN",((screen_width - screen_width//6.5)- 160)+(160//2),screen_height//1.3,160,30,light_green,dark_green,"home")
        elif control_run:
            screen_text("CONTROLS AND INSTRUCTONS",(0,0,0),screen_width/2,50,60)
            screen_text("1. Use up,down,left,right arrow to move around",(0,0,0),screen_width//2,screen_height // 2.5,30)
            screen_text("2. If you collided with the car or side boundary you will lose ",(0,0,0),screen_width// 2,screen_height // 2.5 + 40,30)
            button("HOME SCREEN",(screen_width//1.2)-(160//2),screen_height// 1.2,160,30,light_green,dark_green,"home")


        pygame.display.update()
    



def button(text,x,y,w,h,lc,dc,work):
    global welcome_bool,pause,control_run
    click = pygame.mouse.get_pressed()[0]
    pos = pygame.mouse.get_pos()
    rec = pygame.draw.rect(screen, lc, [x,y,w,h])
    if rec.collidepoint(pos):
        rec = pygame.draw.rect(screen, dc, [x,y,w,h])
        if click:
            time.sleep(0.5)
            if work == "play":
                game_loop()
            elif work == "control":
                control_run = True
                welcome_bool = False                
            elif work == "quit":
                pygame.quit()   
                exit()
            elif work =="resume":
                unpause()
            elif work == "home":
                welcome_bool = True
                pause = False
            elif work == "pause":
                pause = True
                welcome_bool = False
                welcome()
                
    screen_text(text,(0,0,0),rec.centerx,rec.centery,30)

def unpause():
    global pause,welcome_bool,run,control_run
    run = False
    control_run = False
    pause = False
    


def screen_text(text,color,pos_x,pos_y,size):
    font = pygame.font.SysFont(None, size)
    click = pygame.mouse.get_pressed()[0]
    text = font.render(text,True,color)
    screen.blit(text,(pos_x - text.get_rect().centerx,pos_y - text.get_rect().centery))


def crash():
    time.sleep(1)
    game_loop()

def draw_car():
    carx = random.randint(green_width+10,screen_width - green_width - player_width - 10)
    cary = -100
    car = {
        "x" : carx , "y" : cary
    }
    return car

def game_loop():
    global pause,welcome_bool,score,playerx,playery
    yellow_y = 0
    ops_speed = 7
    ops_num = random.randint(0,6)
    trial = False
    strip_vel = 8
    run = True
    up_btn_down = False
    down_btn_down = False
    left_btn_down = False
    right_btn_down = False

    car_data = draw_car()
    main_car = [
        {"x":car_data["x"],"y":-100},
        {"x":car_data["x"],"y":-300},
        # {"x":car_data["x"],"y":-500},
    ]

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    up_btn_down = True
                if event.key == K_DOWN:
                    down_btn_down = True
                if event.key == K_LEFT:
                    left_btn_down = True
                if event.key == K_RIGHT:
                    right_btn_down = True
                if event.key == K_p:
                    welcome_bool = False
                    pause = True
                    welcome()
            if event.type == KEYUP:
                if event.key == K_UP:
                    up_btn_down = False
                if event.key == K_DOWN:
                    down_btn_down = False
                if event.key == K_LEFT:
                    left_btn_down = False
                if event.key == K_RIGHT:
                    right_btn_down = False
                
        if up_btn_down:
            playery -= 10
            if ops_speed < 14:
                ops_speed += 0.1
        if down_btn_down:
            playery += 10
            if ops_speed > 1:
                ops_speed -= 0.1
        if left_btn_down:
            playerx -= 10
        if right_btn_down:
            playerx += 10
        if strip_vel > 30 or strip_vel < -30:
            strip_vel = 0
        if yellow_y+screen_height - 50  > screen_height:
            yellow_y = -50
        yellow_y += strip_vel 
        
        if playery + player_height  >= screen_height:
            playery = screen_height - player_height
        if playerx <= green_strip.get_rect().right:
            playerx = green_strip.get_rect().right
        if playerx + player_width >= screen_width - (green_strip.get_rect().width):
            playerx = screen_width - (green_strip.get_rect().width) - player_width
        if main_car[0]["y"]  >= screen_height:
            car_data1 = draw_car()
            main_car.append(car_data1)
            main_car.pop(0)
        for i in main_car:
            print(i)
            if playery <i["y"]+player_height and playery+player_height>=i["y"]:
                if i["x"]<playerx+10 <i["x"]+player_width or i["x"]<(playerx -10)+ player_width<i["x"] + player_width:
                    score = 0
                    game_loop()
            
        # for i in range(1,101,4):
        #     if ops_speed < 20:
        #         if score == 5*i:
        #             ops_speed =3 + i
        #             strip_vel = 4+i
            # else:
            #     ops_speed = 
            #     strip_vel = 15
        ops_speed += 0.001
        for car in main_car:
            car["y"] += ops_speed
        screen.fill(grey)
        screen.blit(green_strip,(0,0))
        screen.blit(green_strip,(screen_width - (green_strip.get_rect().width),0))
        screen.blit(white_strip,(green_strip.get_rect().width + 20,0))
        screen.blit(white_strip,(screen_width - green_strip.get_rect().width -20,0))
        for i in range(0,601,100):
            screen.blit(yellow_strip,(screen_width//2 - yellow_strip.get_rect().centerx,yellow_y+i))
        screen.blit(cars["car"][2],(playerx,playery))
        button("PAUSE",screen_width - 100,10,100,30,light_blue,dark_blue,"pause")
        # draw_car(main_car[i]["x"],main_car[i]["y"],ops_num)
        for car in main_car:
            screen.blit(cars["car"][6],(car["x"],car["y"]))
        screen_text(f"score : {score}",(0,0,0),50,20,30)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    exit()
# game_loop()
welcome()
