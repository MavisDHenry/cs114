from Fire_world_main.monsters import monster


class FireWalker(monster.Monster):
    def __init__(self):
        monster.Monster.__init__(self)
        self._action_next = 'flame_fork'
        self._name = 'Fire Walker'
