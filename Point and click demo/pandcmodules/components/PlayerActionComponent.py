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
        logger = LoggerUtil()
        logger.info("PlayerActionComponent")