from Fire_game.Flame_world.Fire_world_main.monsters import bossmonster


class FireWarden(bossmonster.BossMonster):
    def __init__(self):
        bossmonster.BossMonster.__init__(self)
        self._action_next = 'fire_fork_left_return02'
        self._name = 'Fire Warden'
