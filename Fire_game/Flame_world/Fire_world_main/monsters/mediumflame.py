from Fire_game.Flame_world.Fire_world_main.monsters import monster


class MediumFlame(monster.Monster):
    def __init__(self):
        monster.Monster.__init__(self)
        self._action_next = 'hallway_continue'
        self._name = 'Medium Flame'
