import pygame
import math
from pyplatformerengine.utilities.LoggerUtil import LoggerUtil

"""
    controller for the main character's inputs.
"""
class PlayerActionComponent:
    endGame = False
    goalX = 0
    goalY = 0
    isToMove = False
    
    """
        Runs the update to the logic component.
    """
    def determineAction(self, entity):
        entity.deltaX = 0
        entity.deltaY = 0
        if self.isToMove:
            angle = self.calculateAngle(self.goalX, entity.rect.x, self.goalY, entity.rect.y)
            deltaX, deltaY = self.determineSpeed(angle, entity.maximumLeftRightVelocity)
            print("X: " + str(deltaX))
            print("Y: " + str(deltaY))
            entity.deltaX = deltaX
            entity.deltaY = deltaY
    
    """
        Calculate the angle between the 2 points.
    """
    def calculateAngle(self, x1, x2, y1, y2):
        return math.atan((x2 - x1) / (y2 - y1)) * 180 / math.pi
    
    """
        Determine the x and the y speeds.
    """
    def determineSpeed(self, angle, maxSpeed):
        x = maxSpeed * math.sin(angle)
        y = maxSpeed * math.cos(angle)
        return int(x), int(y)