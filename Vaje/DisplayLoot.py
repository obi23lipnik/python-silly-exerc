__author__ = 'obi'
import sys, pygame, lootgen, os, random

pygame.init()

screen = pygame.display.set_mode((800,140))
font = pygame.font.SysFont("monospace",45)
colors = (60, 60, 60), (0, 200, 0), (200, 0, 0), (30, 30, 120), (200, 200, 0), (255,255,255)
item = ("ROLL!",4)
clock = pygame.time.Clock()
mod = 5
def buttons():
    mestobutton = pygame.image.load(os.path.join("lootgen", "mesto.png"))
    gozdbutton = pygame.image.load(os.path.join("lootgen", "gozd.png"))
    brunbutton = pygame.image.load(os.path.join("lootgen", "brunarice.png"))
    sefbutton = pygame.image.load(os.path.join("lootgen", "safe.png"))
    medbutton = pygame.image.load(os.path.join("lootgen", "medbox.png"))
    screen.blit(sefbutton, (220, 100))
    screen.blit(medbutton, (250, 100))
    screen.blit(gozdbutton,(10,70))
    screen.blit(brunbutton,(80,70))
    screen.blit(mestobutton,(150,70))

while 1:
    mestobutton = pygame.image.load(os.path.join("lootgen", "mesto.png"))
    gozdbutton = pygame.image.load(os.path.join("lootgen", "gozd.png"))
    brunbutton = pygame.image.load(os.path.join("lootgen", "brunarice.png"))
    clock.tick(60)
    screen.fill((20,10,10))
    buttons()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mod+=1
                print("+")
            if event.key == pygame.K_DOWN:
                mod-=1
                print("-")
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #Gozd button
    if 250+30 > mouse[0] > 250 and 100+30 > mouse[1] > 100:
        if click[0] == 1:
            rollnum = random.randint(30,45)
            for a in range(0, rollnum, 3):
                item = lootgen.medbox(mod)
                label1 = font.render(item[0], 1, colors[item[1]])
                screen.fill((20,10,10))
                buttons()
                pygame.time.delay(a*10)
                screen.blit(label1, (10, 10))
                screen.blit(label2, (220,50))
                pygame.display.flip()
    if 220+30 > mouse[0] > 220 and 100+30 > mouse[1] > 100:
        if click[0] == 1:
            rollnum = random.randint(30,45)
            for a in range(0, rollnum, 3):
                item = lootgen.sef(mod)
                label1 = font.render(item[0], 1, colors[item[1]])
                screen.fill((20,10,10))
                buttons()
                pygame.time.delay(a*10)
                screen.blit(label1, (10, 10))
                screen.blit(label2, (220,50))
                pygame.display.flip()
    if 10+60 > mouse[0] > 10 and 70+60 > mouse[1] > 70:
        gozdbutton = pygame.image.load(os.path.join("lootgen", "gozdroll.png"))
        if click[0] == 1:
            gozdbutton = pygame.image.load(os.path.join("lootgen", "gozddown.png"))
            screen.blit(gozdbutton, (10, 70))
            pygame.display.flip()
            pygame.time.delay(100)
            rollnum = random.randint(30,45)
            for a in range(0, rollnum, 3):
                item = lootgen.gozd(mod)
                label1 = font.render(item[0], 1, colors[item[1]])
                screen.fill((20,10,10))
                buttons()
                pygame.time.delay(a*10)
                screen.blit(label1, (10, 10))
                screen.blit(label2, (220,50))
                pygame.display.flip()
    if 80+60 > mouse[0] > 80 and 70+60 > mouse[1] > 70:
        brunbutton = pygame.image.load(os.path.join("lootgen", "brunariceroll.png"))
        if click[0] == 1:
            brunbutton = pygame.image.load(os.path.join("lootgen","brunaricedown.png"))
            screen.blit(brunbutton, (80, 70))
            pygame.display.flip()
            pygame.time.delay(100)
            rollnum = random.randint(30,45)
            for a in range(0, rollnum, 3):
                item = lootgen.brune(mod)
                label1 = font.render(item[0], 1, colors[item[1]])
                screen.fill((20,10,10))
                buttons()
                pygame.time.delay(a*10)
                screen.blit(label1, (10, 10))
                screen.blit(label2, (220,50))
                pygame.display.flip()

    if 150+60 > mouse[0] > 150 and 70+60 > mouse[1] > 70:
        mestobutton = pygame.image.load(os.path.join("lootgen", "mestoroll.png"))
        if click[0] == 1:
            mestobutton = pygame.image.load(os.path.join("lootgen","mestodown.png"))
            screen.blit(mestobutton,(150,70))
            pygame.display.flip()
            pygame.time.delay(100)
            rollnum = random.randint(30,45)
            for a in range(0,rollnum,3):
                item = lootgen.mesto(mod)
                label1 = font.render(item[0],1,colors[item[1]])
                screen.fill((20,10,10))
                buttons()
                pygame.time.delay(a*10)
                screen.blit(label1,(10,10))
                screen.blit(label2, (220,50))
                pygame.display.flip()



    label1 = font.render(item[0]+" <-", 1, colors[item[1]])
    label2 = font.render("Mod: "+str(mod), 1, colors[4])
    #380-400
    #405-425
    #85-105
    screen.blit(label2, (220,50))
    screen.blit(label1,(10,10))
    screen.blit(gozdbutton,(10,70))
    screen.blit(brunbutton,(80,70))
    screen.blit(mestobutton,(150,70))
    pygame.display.flip()


