import pygame, sys, json

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 32)
data ={
    'red':0,
    'blue':0
}
try:

    with open('clicker_score.json') as file:
        data = json.load(file)
except Exception as e:
    print(e)

red_surf = pygame.Surface([200, 200])
red_surf.fill((240, 80, 54))
red_rect = red_surf.get_rect(center=(150, 180))

blue_surf = pygame.Surface([200, 200])
blue_surf.fill((0, 123, 194))
blue_rect = blue_surf.get_rect(center=(480, 180))


click_red_surf = game_font.render(f"Clicks: {data['red']}", True, 'Black')
click_red_rect = click_red_surf.get_rect(center=(150, 320))

click_blue_surf = game_font.render(f"Clicks: {data['blue']}", True, 'black')
click_blue_rect = click_blue_surf.get_rect(center=(480, 320))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('clicker_score.json','w') as file:
                json.dump(data,file)
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if red_rect.collidepoint(event.pos):
                data['red'] +=1
                click_red_surf = game_font.render(f"Clicks: {data['red']}", True, 'Black')
                click_red_rect = click_red_surf.get_rect(center=(150, 320))
            elif blue_rect.collidepoint(event.pos):
                data['blue'] +=1
                click_blue_surf = game_font.render(f"Clicks: {data['blue']}", True, 'black')
                click_blue_rect = click_blue_surf.get_rect(center=(480, 320))

    screen.fill((245, 255, 252))
    screen.blit(red_surf, red_rect)
    screen.blit(blue_surf, blue_rect)
    screen.blit(click_red_surf, click_red_rect)
    screen.blit(click_blue_surf, click_blue_rect)
    pygame.display.update()
    clock.tick(60)
