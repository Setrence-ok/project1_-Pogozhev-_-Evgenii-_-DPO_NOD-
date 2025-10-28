#!/usr/bin/env python3

from .constants import commands, game_state
from .player_actions import get_input, move_player, show_inventory, take_item, use_item
from .utils import attempt_open_treasure, describe_current_room, show_help, solve_puzzle


def process_command(state, command):
    """
      Поцедурная функция, преализующая вызов остальных функций в
      зависимости от команды игрока
      """
    command_elements = command.split()
    room = state['current_room']
    direction = ['west', 'south', 'east', 'north']
    if len(command_elements) == 1 and command_elements[0] in direction:
        move_player(state, command_elements[0])
    else:
        match command_elements[0]:
            case "help":
                show_help(commands)
            case "look":
                describe_current_room(state)
            case "use":
                use_item(state, command_elements[1])
            case "go":
                move_player(state, command_elements[1])
            case "take":
                take_item(state, command_elements[1])
            case "inventory":
                show_inventory(state)
            case "solve":
                if room == 'treasure_room':
                    attempt_open_treasure(state)
                else:
                    solve_puzzle(state)
            case "quit":
                print("Игра окончена")
                state['game_over'] = True
            case "exit":
                print("Игра окончена")
                state['game_over'] = True


def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)

    while not game_state['game_over']:
        process_command(game_state, get_input(prompt="> "))



