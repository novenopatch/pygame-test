import pygame, sys,random


def draw_floor(screen: pygame.Surface, floor: pygame.Surface, floor_x_position: int):
    screen.blit(floor, (floor_x_position, screen.get_height() - 100))
    screen.blit(floor, (floor_x_position + screen.get_width(), screen.get_height() - 100))


def create_pipe(pipe_surface: pygame.Surface, screen: pygame.Surface,pipe_height:list):
    pipe_pos = random.choice(pipe_height)
    new_pipe = pipe_surface.get_rect(midtop=(int(screen.get_width() -100), pipe_pos))
    return new_pipe


def move_pipes(pipes: list[pygame.Rect]):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
def draw_pipes(pipes: list[pygame.Rect],pipe_surface:pygame.Surface,screen: pygame.Surface):
    for pipe in pipes:
        screen.blit(pipe_surface,pipe)

def main():
    pygame.init()
    screen_width = 480
    screen_height = 820
    clock = pygame.time.Clock()

    frame_rate = 120
    gravity = 0.10
    bird_movement = 0
    screen = pygame.display.set_mode((screen_width, screen_height))
    bg = pygame.image.load('assets/images/background-day.png').convert_alpha()
    bg = pygame.transform.scale(bg, (screen_width, screen_height))

    floor = pygame.image.load('assets/images/base.png').convert_alpha()
    floor = pygame.transform.scale(floor, (screen_width, floor.get_height()))
    floor_x_position = 0
    bird = pygame.image.load('assets/images/bluebird-midflap.png').convert()
    bird = pygame.transform.scale2x(bird)
    bird_rect = bird.get_rect(center=(int(480 / 4), int(screen_height / 2)))

    pipe = pygame.image.load('assets/images/pipe-green.png').convert()
    pipe = pygame.transform.scale2x(pipe)

    pipe_list = []
    SPAWN_PIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWN_PIPE, 1200)
    pipe_height = [300,500,600]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_movement = 0
                    bird_movement -= 4
            if event.type == SPAWN_PIPE:
                pipe_list.append(create_pipe(pipe, screen,pipe_height))

        screen.blit(bg, (0, 0))
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird, bird_rect)

        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list,pipe,screen )
        floor_x_position -= 1
        draw_floor(screen, floor, floor_x_position)
        if floor_x_position <= -screen_width:
            floor_x_position = 0

        pygame.display.update()
        clock.tick(frame_rate)


if __name__ == '__main__':
    main()
    print(pygame.version, pygame.get_sdl_version())
