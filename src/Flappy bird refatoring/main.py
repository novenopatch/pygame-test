import pygame,sys

from Game import Game
from Enumeration import Sounds
def main():
    pygame.init()
    frame_rate = 120
    screen_width = 576
    screen_height = 1024
    BIRDFLAP = pygame.USEREVENT + 1
    pygame.time.set_timer(BIRDFLAP, 200)
    SPAWN_PIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWN_PIPE, 1200)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height))
    bg = pygame.image.load('assets/images/background-day.png').convert_alpha()
    bg = pygame.transform.scale2x(bg)
    game = Game(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.save.save_data()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game.game_is_playing:
                    game.bird.sprite.update_movement()
                    game.sounds_manager.play(Sounds.FLAP)
                if event.key == pygame.K_SPACE and not game.game_is_playing:
                    game.remake_game()
            if event.type == SPAWN_PIPE:
                game.spawn_pipes()
            if event.type == BIRDFLAP:
                game.bird.sprite.on_event_bird_flap()
        screen.blit(bg, (0, 0))
        if game.game_is_playing:
            game.run()
        else:
            game.update_screen_on_over_game()
        game.update_floor_position()
        pygame.display.update()
        clock.tick(frame_rate)


if __name__ == '__main__':
    main()
