import pygame
import random

pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer= 512)
pygame.init()

#ustawienia
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Banan")
clock = pygame.time.Clock()
font = pygame.font.Font(r"pliki\font1.ttf",40)
start=0
rury=[]
w=0
vptak, gptak, pptak = 0, 0.3, 275

#skoczek
ptak = pygame.image.load(r"pliki\banan.png")
ptak = pygame.transform.scale(ptak,(50,50))
ptakbox=ptak.get_rect(center=(200,275))
ptakbox.width=35
ptakbox.height=35

#tło, podłoga
tlo = pygame.image.load(r"pliki\tło.jpeg")
gruntx = 0

#dźwięki
skok = pygame.mixer.Sound(r"pliki\skok.wav")
fail = pygame.mixer.Sound(r"pliki\fail.wav")
startgry = pygame.mixer.Sound(r"pliki\start.wav")
punkt = pygame.mixer.Sound(r"pliki\punkt.wav")

#przycisk wyjścia
button = pygame.Surface((200,50))
button.set_alpha(0)
buttonbox = button.get_rect(center=(600,500))

#funkcje
def grunt():
    grunt = pygame.image.load(r"pliki\base.png")
    screen.blit(grunt, (gruntx, 560))
    screen.blit(grunt, (gruntx+336, 560))
    screen.blit(grunt, (gruntx+672, 560))
    screen.blit(grunt, (gruntx+1008, 560))

def napis(tekst,x,y):
    wynik = font.render(tekst,True,(255,255,255))
    wynikbox = wynik.get_rect(center=(x,y))
    screen.blit(wynik,wynikbox)

def pokaz_wynik(a):
    wynik = font.render(f'Wynik: {a}',True,(255,255,255))
    wynikbox = wynik.get_rect(center=(400,50))
    screen.blit(wynik,wynikbox)
    
def nowa_rura(list):
    a=random.randint(150,400)
    rura1 = pygame.image.load(r"pliki\pipe-green.png")
    rura1 = pygame.transform.scale(rura1, (70,400))
    rura1box = rura1.get_rect(topleft=(800,600-a))
    ruramid = pygame.Surface((70,175))
    ruramid.set_alpha(0)
    ruramidbox = ruramid.get_rect(bottomleft=(800,600-a))
    rura2 = pygame.transform.flip(rura1, False, True)
    rura2box = rura2.get_rect(bottomleft=(800,425-a))
    list.append((rura1,rura1box,rura2,rura2box,ruramid,ruramidbox))
    return list

def ruch_rur(list):
    for rura in list:
        for i in range(3):
             rura[2*i+1].centerx -= 2
    return list

def rura(list):
    for rura in list:
        for i in range(0,6,2):
            screen.blit(rura[i],rura[i+1])

RURA = pygame.USEREVENT
pygame.time.set_timer(RURA, 2500)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and start == 1:
                vptak=-8
                skok.play()
            if event.key == pygame.K_SPACE and start == 0:
                rury.clear()
                w=0
                startgry.play()
                start = 1
            if event.key == pygame.K_SPACE and start == 2:
                vptak, gptak, pptak = 0, 0.3, 275
                start = 0
                with open(r"pliki\najlepszy_wynik.txt") as f:
                    if int(w/104) > int(f.read()):
                        with open(r"pliki\najlepszy_wynik.txt", "w") as g:
                            g.write(str(int(w/104)))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if( 500 <= mouse_x <= 700
            and 450 <= mouse_y <= 550):
                running = False
            
        if event.type == RURA:
            rury = nowa_rura(rury)

    screen.blit(tlo,(0,0))
    gruntx-=2
    if gruntx < -336:
        gruntx = 0
    
    #3 stany gry
    if start == 1:
        grunt()
        vptak+=gptak
        pptak+=vptak 
        screen.blit(ptak,ptakbox)
        ptakbox.centery = pptak
        rury = ruch_rur(rury)
        rura(rury)
        for r in rury:
            for i in range(2):
                if ptakbox.colliderect(r[2*i+1]) == True:
                    start = 2
                    fail.play()
                elif ptakbox.colliderect(r[5]) == True:
                    w += 1			
        if ptakbox.top <= -100 or ptakbox.bottom >=550:
             start = 2
             fail.play()
        pokaz_wynik(int(w/104))
        if (w+2)%104==0 and w!=0:
            punkt.play()
    elif start == 2:
        gruntx=0
        grunt()
        screen.blit(ptak,ptakbox)
        rura(rury)
        pokaz_wynik(int(w/104))
        napis("Przegrales!",400,200)
        screen.blit(button,buttonbox)
        napis(f"Wyjscie",600,520)
    else:
        grunt()
        screen.blit(ptak,ptakbox)
        napis("FLAPPY BANAN", 400, 100)
        napis("Wcisnij SPACE aby rozpoczac", 400, 375)
        with open(r"pliki\najlepszy_wynik.txt") as f:
            highscore = f.read()
        napis(f"Najlepszy wynik: {highscore}",400,450)
        screen.blit(button,buttonbox)
        napis(f"Wyjscie",600,520)
            
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()