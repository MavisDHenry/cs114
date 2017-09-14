from Fire_game.Flame_world.Fire_world_main.monsters import bossmonster


class InfernoWalker(bossmonster.BossMonster):
    def __init__(self):
        bossmonster.BossMonster.__init__(self)
        self._action_next = 'inferno_warrior'
        self._name = 'Inferno Walker'

    def _dead_monster_check(self, player: Player) -> None:
        if self._health <= 0:
            player_print("You have defeated {0}".format(self._name))
            player.level_gain(4)
            self._game_loop(self._action_next, player)
        else:
            self._do_attack(player)

    def _set_health(self, player: Player) -> None:
        over_base = (player.level_cur()-1) * \
                    constants.INFERNO_MONSTER_HEALTH_PER_LEVEL
        self._health = constants.INFERNO_MONSTER_BASE_HEALTH + over_base
        self._health_max = self._health