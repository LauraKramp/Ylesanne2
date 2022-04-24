import pygame

running = True
pygame.init()
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne2")
screen.fill([204, 255, 204])

bg = pygame.image.load("bg_shop.png")
screen.blit(bg,[0,0])
bg = pygame.image.load("seller.png")
bg = pygame.transform.scale(bg, [300,300])
screen.blit(bg,[90,140])
bg = pygame.image.load("chat.png")
bg = pygame.transform.scale(bg, [240,170])
screen.blit(bg,[260,90])
font = pygame.font.Font(pygame.font.match_font('sample text'), 24)
text = font.render("Tere, olen Laura Kramp", True, [255,255,255])
text_width = text.get_rect().width
text_height = text.get_rect().height
screen.blit(text, [290,160])

pygame.display.flip()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False