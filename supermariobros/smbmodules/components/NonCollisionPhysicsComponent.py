    
from pygame.rect import Rect
from pyplatformerengine.physics.CollisionDetectionFactory import CollisionDetectionFactory

"""
    A basic background physics
"""
class NonCollisionPhysicsComponent:
    
    """
        Initializes the object.
    """
    def __init__(self, _id, desc):
        self._id = _id
        self.desc = desc
    
    """
        Sets up the object.
    """
    def setUp(self, actor, entity):
        entity.rect = Rect(actor.stateDict["startPositionX"], actor.stateDict["startPositionY"], 1, 1)
    
    """
        Runs the update to the logic component.
    """
    def update(self, actor, entity):
        self.updateLocation(entity)
    
    """
        Updates the logic location of the entity.
    """
    def updateLocation(self, entity):
        entity.rect.x += entity.deltaX
        entity.rect.y += entity.deltaY