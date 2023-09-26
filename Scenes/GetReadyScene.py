import pygame
from Scene import Scene
from Scenes.ExplodeScene import ExplodeScene

class GetReadyScene(Scene):

    font = pygame.font.SysFont("Arial", 30, italic=False, bold=True)
    text = font.render("Press SPACE to start", True, 'yellow')

    def tick(self, frame: int, screen: pygame.Surface, events):

        screen.blit(self.text, ((screen.get_width()-self.text.get_width())/2, (screen.get_height()-self.text.get_height())/2))

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == 32:
                from Scenes.ExplodeScene import ExplodeScene
                return ExplodeScene()

        return self
