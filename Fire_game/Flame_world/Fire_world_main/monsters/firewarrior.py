from Fire_game.Flame_world.Fire_world_main.monsters import monster


class FireWarrior(monster.Monster):
    def __init__(self):
        monster.Monster.__init__(self)
        self._action_next = 'exit_door'
        self._name = 'Fire Warrior'
