from pyplatformerengine.engine.Game import Game
import pygame
game = Game("resources/settings/settings.conf")
pygame.display.set_caption("Super Mario Bros")
game.start_game("resources/game_objects/world1-1.json")