import pygame
from pyplatformerengine.utilities.LoggerUtil import LoggerUtil

"""
    controller for the main character's inputs.
"""
class PlayerActionComponent:
    endGame = False
    
    """
        Runs the update to the logic component.
    """
    def determineAction(self, entity):
        #entity.deltaX = 50
        #entity.deltaY = 50
        logger = LoggerUtil()
        logger.info("PlayerActionComponent")