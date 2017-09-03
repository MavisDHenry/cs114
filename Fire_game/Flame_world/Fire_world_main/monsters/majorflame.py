from Flame_world.Fire_world_main.monsters import monster


class MajorFlame(monster.Monster):
    def __init__(self):
        monster.Monster.__init__(self)
        self._action_next = 'hallway02'
        self._name = 'Major Flame'
