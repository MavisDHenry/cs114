from Fire_game.Flame_world.Fire_world_main.monsters import bossmonster


class FlameWarden(bossmonster.BossMonster):
    def __init__(self):
        bossmonster.BossMonster.__init__(self)
        self._action_next = 'fire_fork_left_return'
        self._name = 'Flame Warden'
