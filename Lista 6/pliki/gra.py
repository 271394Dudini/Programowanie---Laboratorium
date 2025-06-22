import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.g = 0.2
        
    def spadek(self):
            self.rect.y += self.g  
    def update(self, keys):
        if keys[pygame.K_SPACE]:
            self.rect.y = 0
            


            
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Title")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    all_sprites.spadek()
    all_sprites.update(keys)
    screen.fill((0, 128, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()