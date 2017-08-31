from Flame_world.Fire_world_infinite import constants
from Flame_world.Fire_world_infinite.interact import player_print


class Player(object):
    def __init__(self):
        self._max_health = 0
        self._cur_health = 0
        self._cur_level = 0
        self._is_dead = False

    def _check_death(self):
        if self._cur_health < 0:
            self._cur_health = 0
            self._is_dead = True

    def player_new(self):
        self._cur_health = constants.INIT_HEALTH
        self._max_health = constants.INIT_HEALTH
        self._cur_level = constants.INIT_LEVEL

    def player_restore(self, health: int, level: int) -> None:
        self._cur_health = health
        self._cur_level = level
        self._check_death()

    def damage(self, damage_amount: int) -> None:
        self._cur_health -= damage_amount
        self._check_death()

    def heal(self) -> None:
        if self._cur_health > 0:
            h_diff = self._max_health - self._cur_health
            h_add = int(h_diff / 2)
            self._cur_health += h_add
        else:
            self._check_death()

    def is_dead(self) -> bool:
        return self._is_dead

    def level_cur(self) -> int:
        return self._cur_level

    def level_gain(self, extra_levels: int=0) -> None:
        self._cur_level += 1
        if extra_levels > 0:
            self._cur_level += extra_levels
        hpl = (self._cur_level-1) * constants.HEALTH_PER_LEVEL
        self._cur_health = constants.INIT_HEALTH + hpl
        self._max_health = self._cur_health
        if self._cur_health > self._max_health:
            self._cur_health = self._max_health
        player_print("Congratulations! You have gained a level.")
        player_print("You are now level {0}".format(self._cur_level))
        self.print_health()

    def level_remove(self) -> None:
        self._cur_level -= 1
        if self._cur_level < 1:
            self._cur_level = 1

    def print_health(self) -> None:
        player_print("Your current health is {0}/{1}".format(self._cur_health,
                                                             self._max_health))
