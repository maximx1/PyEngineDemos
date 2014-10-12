import pygame
from pyplatformerengine.utilities.ConsoleManager import ConsoleManager

"""
    controller for the main character's inputs.
"""
class MouseActionComponent:
    
    """
        Runs the update to the logic component.
    """
    def determineAction(self, entity):
        consoleManager = ConsoleManager()
        playerEntity = None
        for ent in consoleManager.getInScopeEntities():
            if ent._id == "2":
                playerEntity = ent
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playerEntity.actionComponent.endGame = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    playerEntity.actionComponent.endGame = True
            elif event.type == pygame.MOUSEMOTION:
                mouseX, mouseY = event.pos
                entity.deltaX = mouseX
                entity.deltaY = mouseY
        mouse1, _, mouse3 = pygame.mouse.get_pressed()
        if mouse3:
            playerEntity.physicsComponent.goalX = entity.deltaX
            playerEntity.physicsComponent.goalY = entity.deltaY