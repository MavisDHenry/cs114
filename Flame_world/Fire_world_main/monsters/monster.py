from random import randint
from Flame_world.Fire_world_main import constants
from Flame_world.Fire_world_main import statements
from Flame_world.Fire_world_main.interact import exit_game
from Flame_world.Fire_world_main.interact import get_player_input
from Flame_world.Fire_world_main.interact import player_print
from Flame_world.Fire_world_main.player import Player
from typing import Callable


class Monster(object):
    def __init__(self):
        self._action_next = ''
        self._health = 0
        self._health_max = 0
        self._name = 'Monster'
        self._game_loop = None

    def _dead_monster_check(self, player: Player) -> None:
        if self._health <= 0:
            player_print("You have defeated {0}".format(self._name))
            player.level_gain()
            self._game_loop(self._action_next, player)
        else:
            self._do_attack(player)

    def _dead_player_check(self, player: Player) -> None:
        if player.is_dead():
            exit_game("You have died to {0}".format(self._name))
        self._player_choice(player)

    def _do_attack(self, player: Player) -> None:
        level = player.level_cur()
        level_damage = constants.MONSTER_DAMAGE_PER_LEVEL * level
        attack_min = constants.MONSTER_MIN_DAMAGE + level_damage
        attack_max = constants.MONSTER_MAX_DAMAGE + level_damage
        cur_damage = randint(attack_min, attack_max)
        player_print("{0} attacks dealing {1} damage".format(self._name,
                                                             cur_damage))
        player.damage(cur_damage)
        player.print_health()
        self._dead_player_check(player)

    def _do_player_attack(self, player: Player) -> None:
        level = player.level_cur()
        level_damage = constants.PLAYER_DAMAGE_PER_LEVEL * level
        attack_max = constants.PLAYER_MIN_DAMAGE + level_damage
        cur_damage = randint(constants.PLAYER_MIN_DAMAGE, attack_max)
        self._health -= cur_damage
        attack_format = "You attacked {0} dealing {1} damage"
        health_format = "{0}'s health: {1}/{2}"
        player_print(attack_format.format(self._name, cur_damage))
        player_print(health_format.format(self._name, self._health,
                                          self._health_max))
        self._dead_monster_check(player)

    def _set_health(self, player: Player) -> None:
        over_base = (player.level_cur()-1) * constants.MONSTER_HEALTH_PER_LEVEL
        self._health = constants.MONSTER_BASE_HEALTH + over_base
        self._health_max = self._health

    def _player_choice(self, player: Player) -> None:
        p_act = get_player_input(statements.fight_or_heal_question,
                                 statements.fight_or_heal_answers)
        if p_act.lower() == 'fight':
            self._do_player_attack(player)
        elif p_act.lower() == 'heal':
            self._player_heal_battle(player)
        elif p_act.lower() == 'retreat':
            player_print(statements.retreat)
            self._player_retreat(player)

    def _player_heal_battle(self, player: Player) -> None:
        player.heal()
        player.print_health()
        self._do_attack(player)

    def _player_heal_retreat(self, player: Player) -> None:
        player.heal()
        player.print_health()
        self._player_retreat(player)

    def _player_retreat(self, player: Player) -> None:
        p_act = get_player_input(statements.retreat_question,
                                 statements.retreat_answers)
        if p_act.lower() == 'heal':
            self._player_heal_retreat(player)
        else:
            self._do_player_attack(player)

    def set_game_loop(self, game_loop: Callable) -> None:
        self._game_loop = game_loop

    def start_fight(self, player: Player) -> None:
        self._set_health(player)
        self._do_attack(player)
