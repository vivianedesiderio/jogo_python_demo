from game_core.Const import ENTITY_SPEED
from game_core.Entity import Entity


class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple):
            super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]