from random import randint
from Flame_world.Fire_world_infinite import constants
from Flame_world.Fire_world_infinite.interact import player_print
from Flame_world.Fire_world_infinite.monsters import monster
from Flame_world.Fire_world_infinite.player import Player


class BossMonster(monster.Monster):
    def __init__(self):
        monster.Monster.__init__(self)
        self._action_next = ''
        self._name = 'BossMonster'

    def _dead_monster_check(self, player: Player) -> None:
        if self._health <= 0:
            player_print("You have defeated {0}".format(self._name))
            player.level_gain(1)
            self._game_loop(self._action_next, player)
        else:
            self._do_attack(player)

    def _do_attack(self, player: Player) -> None:
        level = player.level_cur()
        level_damage = constants.BOSS_MONSTER_DAMAGE_PER_LEVEL * level
        attack_min = constants.BOSS_MONSTER_MIN_DAMAGE + level_damage
        attack_max = constants.BOSS_MONSTER_MAX_DAMAGE + level_damage
        cur_damage = randint(attack_min, attack_max)
        player_print("{0} attacks dealing {1} damage".format(self._name,
                                                             cur_damage))
        player.damage(cur_damage)
        player.print_health()
        self._dead_player_check(player)

    def _set_health(self, player: Player) -> None:
        over_base = (player.level_cur()-1) * \
                    constants.BOSS_MONSTER_HEALTH_PER_LEVEL
        self._health = constants.BOSS_MONSTER_BASE_HEALTH + over_base
        self._health_max = self._health
