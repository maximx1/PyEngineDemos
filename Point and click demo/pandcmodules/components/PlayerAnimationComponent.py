from pyplatformerengine.utilities.ImageUtils import ImageUtils
from pyplatformerengine.utilities.LoggerUtil import LoggerUtil

"""
    Default animation component for a platformer character.
"""
class PlayerAnimationComponent:
    
    """
        Initializes the object.
    """
    def __init__(self, animationProperties):
        self.props = animationProperties
    
    """
        Prepares the entity with its initial graphic.
    """
    def initializeCharacter(self, entity, startX, startY):
        entity.image = entity.spriteStages["standing"]
        #imageUtils = ImageUtils(entity.spriteStages["standing"])
        #entity.image = imageUtils.scale(self.props["width"], self.props["height"]).getImage()
        entity.rect = entity.image.get_rect()
        entity.rect.x = startX
        entity.rect.y = startY
        
    """
        Runs the update to the logic component.
    """
    def draw(self, entity):
        entity.image = entity.spriteStages["standing"]
        #image = entity.spriteStages["standing"]
        #imageUtils = ImageUtils(image)
        #entity.image = imageUtils.scale(self.props["width"], self.props["height"]).getImage()
        originalX = entity.rect.x
        originalY = entity.rect.y
        entity.rect = entity.image.get_rect()
        entity.rect.x = originalX
        entity.rect.y = originalY
        loggerUtil = LoggerUtil()
        loggerUtil.info("CharacterLocation: (" + str(entity.rect.x) + ", " + str(entity.rect.y) + ")")