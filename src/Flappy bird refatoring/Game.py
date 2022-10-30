import pygame, random
from Bird import Bird
from Floor import Floor
from Pipe import Pipe
from Sounds import SoundManager
from Enumeration import Sounds


class Game():
    def __init__(self, screen: pygame.Surface):
        self.screen: pygame.Surface = screen
        self.screen_width: int = screen.get_width()
        self.screen_height: int = screen.get_height()
        self.game_font: pygame.font.Font = pygame.font.Font("assets/font/Pixeled.ttf", 20)
        self.game_is_playing: bool = False
        self.bird_sprite: Bird = Bird(screen)
        self.bird: pygame.sprite.GroupSingle = pygame.sprite.GroupSingle(self.bird_sprite)
        self.game_over: pygame.Surface = pygame.transform.scale2x(
            pygame.image.load('assets/images/message.png').convert_alpha())
        self.game_over_rect: pygame.Rect = self.game_over.get_rect(
            center=(self.screen_width / 2, self.screen_height / 2))
        self.floor: Floor = Floor(screen)
        self.score: int = 0
        self.high_score: int = 0
        self.pipes_group = pygame.sprite.Group()
        self.pipe: Pipe = Pipe()
        self.pipes: list[pygame.Rect] = []
        self.pipe_height: list[int] = [400, 600, 800]
        self.pipe_spacing: int = 300
        self.pipe_starting_pos_x: int = 700
        self.score_sound_countdown: int = 200
        self.sounds_manager: SoundManager = SoundManager()

    def run(self):
        self.bird.sprite.draw()
        ##game
        self.game_is_playing = self.check_collision()
        self.pipes = self.move_pipes()
        self.draw_pipes()
        self.score_display()
        self.score, self.high_score = self.update_score()
        self.score_sound_countdown -= 1
        if self.score_sound_countdown <= 0:
            self.score_sound_countdown = 200
            self.sounds_manager.play(Sounds.SCORE)
        self.floor.position_x -= 1
        self.floor.draw()

    def update_screen_on_over_game(self):
        self.screen.blit(self.game_over, self.game_over_rect)
        self.score_display()

    def update_floor_position(self):
        if self.floor.position_x <= -self.screen_width:
            self.floor.position_x = 0

    def update_score(self) -> tuple:
        self.score += 0.01
        if self.score > self.high_score:
            self.high_score = self.score
        return self.score, self.high_score

    def score_display(self):
        if self.game_is_playing:
            score_surface = self.game_font.render(str(int(self.score)), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(288, 100))
            self.screen.blit(score_surface, score_rect)
        else:
            score_surface = self.game_font.render(f'Score = {str(int(self.score))} ', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(288, 100))
            self.screen.blit(score_surface, score_rect)

            high_score_surface = self.game_font.render(f'High Score = {str(int(self.high_score))} ', True,
                                                       (255, 255, 255))
            high_score_rect = high_score_surface.get_rect(center=(288, 850))
            self.screen.blit(high_score_surface, high_score_rect)

    def create_pipe(self) -> tuple:
        pipe_pos = random.choice(self.pipe_height)
        bottom_pipe = self.pipe.image.get_rect(midtop=(self.pipe_starting_pos_x, pipe_pos))
        top_pipe = self.pipe.image.get_rect(midbottom=(self.pipe_starting_pos_x, pipe_pos - self.pipe_spacing))
        return bottom_pipe, top_pipe

    def move_pipes(self) -> list[pygame.Rect]:
        for pipe in self.pipes:
            pipe.centerx -= 5
        visibles_pipes = [pipe for pipe in self.pipes if pipe.right > -50]
        return visibles_pipes

    def draw_pipes(self):
        for pipe in self.pipes:
            if pipe.bottom >= self.screen_height:
                self.screen.blit(self.pipe.image, pipe)
            else:
                flip_pip = pygame.transform.flip(self.pipe.image, False, True)
                self.screen.blit(flip_pip, pipe)

    def check_collision(self) -> bool:
        for pipe in self.pipes:
            if self.bird.sprite.rect.colliderect(pipe):
                self.sounds_manager.play(Sounds.DEATH)
                return False
        if self.bird.sprite.rect.top <= -100 or self.bird.sprite.rect.bottom >= 900:
            return False
        return True

    def remake_game(self):
        self.bird.sprite.bird_movement = 0
        self.game_is_playing = True
        self.pipes.clear()
        self.bird.sprite.rect = self.bird.sprite.center_bird_rect()
        # self.bird.sprite.rect = self.bird.sprite.c
        self.score = 0

    def spawn_pipes(self):
        self.pipes.extend(self.create_pipe())
