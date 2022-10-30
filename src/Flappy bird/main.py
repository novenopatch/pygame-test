import pygame, sys, random


def draw_floor(screen: pygame.Surface, floor: pygame.Surface, floor_x_position: int):
    screen.blit(floor, (floor_x_position, screen.get_height() - 100))
    screen.blit(floor, (floor_x_position + screen.get_width(), screen.get_height() - 100))


def create_pipe(pipe_surface: pygame.Surface, pipe_height: list[int]) -> tuple:
    pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700, pipe_pos - 300))
    return bottom_pipe, top_pipe


def move_pipes(pipes: list[pygame.Rect]) -> list[pygame.Rect]:
    for pipe in pipes:
        pipe.centerx -= 5
    visibles_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return visibles_pipes


def draw_pipes(pipes: list[pygame.Rect], pipe_surface: pygame.Surface, screen: pygame.Surface):
    for pipe in pipes:
        if pipe.bottom >= screen.get_height():
            screen.blit(pipe_surface, pipe)
        else:
            flip_pip = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pip, pipe)


def check_collision(pipes: list[pygame.Surface], bird_rect: pygame.Rect, sound: pygame.mixer.Sound) -> bool:
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            sound.play()
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        return False
    return True


def center_bird_rect(bird: pygame.Surface, screen: pygame.Surface) -> pygame.Rect:
    return bird.get_rect(center=((screen.get_width() - 76) / 5, screen.get_height() / 2))


def rotate_bird(bird: pygame.Surface, bird_movement: int):
    return pygame.transform.rotozoom(bird, -bird_movement * 3, 1)


def bird_animation(bird_index: int, bird_frames: list[pygame.Surface], last_bird_rect: pygame.Rect,
                   screen: pygame.Surface):
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=((screen.get_width() - 76) / 5, last_bird_rect.centery))
    return new_bird, new_bird_rect


def score_display(game_state: bool, game_font: pygame.font.Font, screen: pygame.Surface, score: int,
                  high_score: int = None):
    if game_state:
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 100))
        screen.blit(score_surface, score_rect)
    elif not game_state and high_score != None:
        score_surface = game_font.render(f'Score = {str(int(score))} ', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score = {str(int(high_score))} ', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(288, 850))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score: int, high_score: int) -> tuple:
    score += 0.01
    if score > high_score:
        high_score = score
    return score, high_score


def pipes_score_check(pipes: list[pygame.Surface], score: int, sound: pygame.mixer.Sound):
    for pipe in pipes:
        if 95 < pipe.get_rect().centerx < 105:
            score += 1
            sound.play()


def main():
    pygame.init()
    screen_width = 576
    screen_height = 1024
    clock = pygame.time.Clock()
    game_font = pygame.font.Font("assets/font/Pixeled.ttf", 20)

    frame_rate = 120
    gravity = 0.25
    bird_movement = 0
    game_active = True
    score = 0
    high_score = 0
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
    bird_frames = [bird_downflap, bird_midflap, bird_upflap]
    bird_index = 0
    bird = bird_frames[bird_index]
    bird_rect = center_bird_rect(bird, screen)
    BIRDFLAP = pygame.USEREVENT + 1
    pygame.time.set_timer(BIRDFLAP, 200)
    # bird = pygame.image.load('assets/images/bluebird-midflap.png').convert_alpha()
    # bird = pygame.transform.scale2x(bird)
    # bird_rect = center_bird_rect(bird,screen)

    pipe = pygame.image.load('assets/images/pipe-green.png').convert_alpha()
    pipe = pygame.transform.scale2x(pipe)

    pipe_list = []
    SPAWN_PIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWN_PIPE, 1200)
    pipe_height = [400, 600, 800]
    game_over = pygame.transform.scale2x(pygame.image.load('assets/images/message.png').convert_alpha())
    game_over_rect = game_over.get_rect(center=(screen_width / 2, screen_height / 2))
    flap_sound = pygame.mixer.Sound('assets/audio/wing.wav')
    death_sound = pygame.mixer.Sound('assets/audio/hit.wav')
    score_sound = pygame.mixer.Sound('assets/audio/point.wav')
    score_sound_countdown = 200
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement -= 7
                    flap_sound.play()
                if event.key == pygame.K_SPACE and not game_active:
                    bird_movement = 0
                    game_active = True
                    pipe_list.clear()
                    bird_rect = center_bird_rect(bird, screen)
                    score = 0

            if event.type == SPAWN_PIPE:
                pipe_list.extend(create_pipe(pipe, pipe_height))
            if event.type == BIRDFLAP:
                if bird_index < 2:
                    bird_index += 1
                else:
                    bird_index = 0
                bird, bird_rect = bird_animation(bird_index, bird_frames, bird_rect, screen)

        screen.blit(bg, (0, 0))
        if game_active:
            bird_movement += gravity
            rotated_bird = rotate_bird(bird, bird_movement)
            bird_rect.centery += bird_movement
            screen.blit(rotated_bird, bird_rect)
            game_active = check_collision(pipe_list, bird_rect, death_sound)

            pipe_list = move_pipes(pipe_list)
            draw_pipes(pipe_list, pipe, screen)
            score_display(game_active, game_font, screen, score)
            score, high_score = update_score(score, high_score)
            score_sound_countdown -= 1
            if score_sound_countdown <= 0:
                score_sound_countdown = 200
                score_sound.play()

            floor_x_position -= 1
            draw_floor(screen, floor, floor_x_position)
        else:
            screen.blit(game_over, game_over_rect)
            score_display(game_active, game_font, screen, score, high_score)
        if floor_x_position <= -screen_width:
            floor_x_position = 0

        pygame.display.update()
        clock.tick(frame_rate)


if __name__ == '__main__':
    main()
    print(pygame.version, pygame.get_sdl_version())
