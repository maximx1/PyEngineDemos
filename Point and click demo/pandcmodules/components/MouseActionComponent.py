import pygame

"""
    controller for the main character's inputs.
"""
class MouseActionComponent:
    endGame = False
    
    """
        Runs the update to the logic component.
    """
    def determineAction(self, entity):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.endGame = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.endGame = True
            elif event.type == pygame.MOUSEMOTION:
                mouseX, mouseY = event.pos
                entity.deltaX = mouseX
                entity.deltaY = mouseY