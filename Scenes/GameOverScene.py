import pygame
from Scene import Scene

class GameOverScene(Scene):

    font = pygame.font.SysFont("Arial", 60, italic=False, bold=True)
    text = font.render("GAME OVER", True, 'white')

    def tick(self, frame: int, screen: pygame.Surface, events):

        screen.blit(self.text, ((screen.get_width()-self.text.get_width())/2, (screen.get_height()-self.text.get_height())/2))

        if frame > 100:
            from Scenes.GetReadyScene import GetReadyScene
            return GetReadyScene()

        return self
    
