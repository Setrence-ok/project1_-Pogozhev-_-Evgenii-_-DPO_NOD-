#!/usr/bin/env python3

from .utils import describe_current_room, solve_puzzle, show_help
from .player_actions import show_inventory, get_input, move_player, take_item, use_item
from .constants import game_state


def process_command(state, command):
    command_elements = command.split()
    match command_elements[0]:
        case "help":
            show_help()
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



