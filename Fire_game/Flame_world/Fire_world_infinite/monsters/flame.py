from Fire_game.Flame_world.Fire_world_infinite.monsters import monster


class Flame(monster.Monster):
    def __init__(self):
        monster.Monster.__init__(self)
        self._action_next = 'after_flame_fork'
        self._name = 'Flame'
