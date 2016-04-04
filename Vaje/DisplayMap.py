__author__ = 'obi'
import sys, pygame, os, mapgen, random
pygame.init()
screen = pygame.display.set_mode((990,490))
def genmap():
    for i in range(0,49):

        aram = mapgen.map[i]
        for j in range(0,99):
            if aram[j] == "T":
                screen.blit(trava,(j*10,i*10))
            elif aram[j] == "P":
                screen.blit(pot,(j*10,i*10))
    screen.blit(genbut,(40,40))
    pygame.display.flip
    pygame.display.flip()
bruna = pygame.image.load(os.path.join("mapgen", "bruna.jpg"))
mesto = pygame.image.load(os.path.join("mapgen", "mesto.jpg"))
ozadje = pygame.image.load(os.path.join("mapgen", "ozadje.jpg"))
pot = pygame.image.load(os.path.join("mapgen", "pot.jpg"))
trava = pygame.image.load(os.path.join("mapgen", "trava.jpg"))
voda = pygame.image.load(os.path.join("mapgen", "voda.jpg"))
pot2 = pygame.image.load(os.path.join("mapgen","pot2.jpg"))
genbut = pygame.image.load(os.path.join("mapgen","generate.png"))
genmap()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 40 < mouse[0] < 40+80 and 40 < mouse[1] < 40+30:
            print("HIT")
            if click[0] == 1:

                print("KLIK")
                genmap()


