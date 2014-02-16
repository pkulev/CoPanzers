import pygame, math

from .util import Rect

class GameObject:

    def __init__ (self, texture, position, hitbox):
        """
        texture   -- pygame Surface or pygame Color
        position  -- 2 tuple of int, initial position on the screen
        hitbox    -- 2 tuple of int, size of the hitbox of the object
        """

        self.hitbox = Rect ( position, hitbox )

        if isinstance (texture, pygame.Surface):
            self.texture = texture
        elif isinstance (texture, (pygame.Color, tuple)):
            self.texture = pygame.Surface (self.hitbox.size)
            self.texture.fill (texture)
            pygame.draw.rect (self.texture, (0, 0, 0), self.texture.get_rect (), 1)
        else:
            raise TypeError ("Parameter $texture must be a pygame Surface or Color.")

        self.position = list (position)
        # holds misc data about the object
        # class -- what class of objects does it belongs to? Turret/Bullet/Whatever
        # kind  -- what kind of Turret/Bullet/Whatever is it?
        # team  -- objects with the same self.tags["team"] e.g. should normally not attack each other
        # name  -- name for display, should be unique but does not have to be, 
        #          use id(obj) if you need a unique identifier
        self.tags = {"class": None, "kind": None, "team": None, "name": None} 

    def step (self, other_game_objects, relative_time):
        """
        other_game_objects -- list, well, duh, a list of all other 
                                    game objects currently in the game
        relative_time      -- float, modifier to influence to overall 
                                     pace of the game and to accomodate 
                                     between different fps
        """
        self.hitbox.center = self.position

    def draw (self, surface):
        surface.blit (self.texture, (self.position [0] - self.texture.get_width () / 2,
                                    self.position [1] - self.texture.get_height () / 2))

