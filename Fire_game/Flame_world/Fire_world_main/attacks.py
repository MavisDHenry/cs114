from random import random
from Fire_game.Flame_world.Fire_world_main import constants


class AttackWeapon(object):
    def __init__(self):
        self._base_damage = constants.MAX_DAMAGE
        self._dpl = constants.DAMAGE_PER_LEVEL

    def do_damage(self, level: int) -> int:
        max_damage = self._base_damage + (level * self._dpl)
        return random(self._base_damage, max_damage)


class Sword(AttackWeapon):
    def __init__(self):
        AttackWeapon.__init__(self)


class Attack(object):
    def __init__(self):
        self.Sword = Sword()

    def attack(self, level: int) -> int:
        return self.Sword.do_damage(level)
