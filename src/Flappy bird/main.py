import pygame, sys, random


def draw_floor(screen: pygame.Surface, floor: pygame.Surface, floor_x_position: int):
    screen.blit(floor, (floor_x_position, screen.get_height() - 100))
    screen.blit(floor, (floor_x_position + screen.get_width(), screen.get_height() - 100))


def create_pipe(pipe_surface: pygame.Surface, screen: pygame.Surface, pipe_height: list) -> tuple:
    pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700, pipe_pos - 300))
    return bottom_pipe, top_pipe


def move_pipes(pipes: list[pygame.Rect]) -> list[pygame.Rect]:
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes: list[pygame.Rect], pipe_surface: pygame.Surface, screen: pygame.Surface):
    for pipe in pipes:
        if pipe.bottom >= screen.get_height():
            screen.blit(pipe_surface, pipe)
        else:
            flip_pip = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pip, pipe)


def check_colliion(pipes: list[pygame.Surface], bird_rect: pygame.Rect) -> bool:
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        return False
    return True


def center_bird_rect(bird: pygame.Surface, screen: pygame.Surface) -> pygame.Rect:
    return bird.get_rect(center=((screen.get_width() - 76) / 5, screen.get_height() / 2))

def rotate_bird(bird:pygame.Surface,bird_movement:int):
    return pygame.transform.rotozoom(bird,-bird_movement*3,1)
def bird_animation(bird_index:int,bird_frames:list[pygame.Surface],last_bird_rect:pygame.Rect,screen:pygame.Surface):
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=((screen.get_width() - 76) / 5,last_bird_rect.centery))
    return  new_bird,new_bird_rect
def main():
    pygame.init()
    screen_width = 576
    screen_height = 1024
    clock = pygame.time.Clock()

    frame_rate = 120
    gravity = 0.25
    bird_movement = 0
    game_active = True
    screen = pygame.display.set_mode((screen_width, screen_height))
    bg = pygame.image.load('assets/images/background-day.png').convert_alpha()
    # bg = pygame.transform.scale(bg, (screen_width, screen_height))
    bg = pygame.transform.scale2x(bg)

    floor = pygame.image.load('assets/images/base.png').convert_alpha()
    # floor = pygame.transform.scale(floor, (screen_width, floor.get_height()))
    floor = pygame.transform.scale2x(floor)
    floor_x_position = 0

    bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/images/bluebird-downflap.png').convert_alpha())
    bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/images/bluebird-midflap.png').convert_alpha())
    bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/images/bluebird-upflap.png').convert_alpha())
    bird_frames = [bird_downflap,bird_midflap,bird_upflap]
    bird_index = 0
    bird = bird_frames[bird_index]
    bird_rect = center_bird_rect(bird,screen)
    BIRDFLAP = pygame.USEREVENT +1
    pygame.time.set_timer(BIRDFLAP,200)
    #bird = pygame.image.load('assets/images/bluebird-midflap.png').convert_alpha()
    #bird = pygame.transform.scale2x(bird)
    #bird_rect = center_bird_rect(bird,screen)

    pipe = pygame.image.load('assets/images/pipe-green.png').convert_alpha()
    pipe = pygame.transform.scale2x(pipe)

    pipe_list = []
    SPAWN_PIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWN_PIPE, 1200)
    pipe_height = [400, 600, 800]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                bird_movement = 0
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement -= 12
                if event.key == pygame.K_SPACE and not game_active:
                    game_active = True
                    pipe_list.clear()
                    bird_rect = center_bird_rect(bird,screen)

            if event.type == SPAWN_PIPE:
                pipe_list.extend(create_pipe(pipe, screen, pipe_height))
            if event.type == BIRDFLAP:
                if bird_index < 2:
                    bird_index += 1
                else:
                    bird_index = 0
                bird,bird_rect = bird_animation(bird_index,bird_frames,bird_rect,screen)


        screen.blit(bg, (0, 0))
        if game_active:
            bird_movement += gravity
            rotated_bird = rotate_bird(bird,bird_movement)
            bird_rect.centery += bird_movement
            screen.blit(rotated_bird, bird_rect)
            game_active = check_colliion(pipe_list, bird_rect)

            pipe_list = move_pipes(pipe_list)
            draw_pipes(pipe_list, pipe, screen)
            floor_x_position -= 1
            draw_floor(screen, floor, floor_x_position)
        if floor_x_position <= -screen_width:
            floor_x_position = 0

        pygame.display.update()
        clock.tick(frame_rate)


if __name__ == '__main__':
    main()
    print(pygame.version, pygame.get_sdl_version())
