import pygame
from GameObjects.ExplosionParticle import ExplosionParticle
from Scene import Scene

class ExplodeScene(Scene):

    def init(self):

        self.particles = []
        for x in range(1000):
            self.particles.append(ExplosionParticle(512,768/2))


    def tick(self, frame: int, screen: pygame.Surface, events):

        for x in self.particles:
            x.tick()
            x.draw(screen)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == 32:
                from Scenes.GetReadyScene import GetReadyScene
                return GetReadyScene()

        return self
