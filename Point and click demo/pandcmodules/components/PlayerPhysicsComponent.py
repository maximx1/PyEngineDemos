"""
    A basic physics component for moving a character around.
"""
class PlayerPhysicsComponent:
    
    goalX = 0
    goalY = 0
    
    """
        Initializes the object.
    """
    def __init__(self, terminalVelocity, collisionDetectionComponent):
        self.terminalVelocity = terminalVelocity
        self.collisionDetectionComponent = collisionDetectionComponent
    
    """
        Runs the update to the logic component.
    """
    def update(self, entity):
        self.updateLocation(entity)
    
    """
        Updates the logic location of the entity.
    """
    def updateLocation(self, entity):
        """
            1. Calculate angle between the two points
            2. Convert the left-right velocity to an diagonal speed
        """
        entity.rect.x = self.goalX
        entity.rect.y = self.goalY