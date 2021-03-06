# Copyright (C) 2014 Marvin Poul <ponder@creshal.de>
import pygame
import math
from ecs.exceptions import NonexistentComponentTypeForEntity

from copanzers.systems import LogSystem
from copanzers.components import *


class RenderSystem (LogSystem):

    def __init__(self, surface, *args, **kw):
        """
        surface -- pygame.Surface, surface to draw to
        """
        self.surface = surface
        LogSystem.__init__(self, *args, **kw)

    def update(self, _):

        surf = self.surface
        surf.fill((255, 255, 255))

        eman = self.entity_manager
        renders = list(eman.pairs_for_type(Renderable))
        renders.sort(key=lambda x: x[1].layer)
        for e, renderable in renders:

            pos = eman.component_for_entity(e, Position)
            try:
                rot = eman.component_for_entity(e, Movement).angle
                if rot != 0:
                    texture = pygame.transform.rotate(
                        renderable.texture, math.degrees(-rot)
                    )
                else:
                    texture = renderable.texture
            except NonexistentComponentTypeForEntity:
                texture = renderable.texture

            text_rect = texture.get_rect()
            text_rect.center = pos.x, pos.y
            surf.blit(texture, text_rect)
