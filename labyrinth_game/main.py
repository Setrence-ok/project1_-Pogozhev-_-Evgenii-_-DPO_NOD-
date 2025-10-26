#!/usr/bin/env python3

from .utils import describe_current_room
from .player_actions import show_inventory, get_input, move_player, take_item, use_item
from .constants import game_state


def process_command(state, command):
    command_elements = command.split()
    match command_elements[0]:
        case "look":
            describe_current_room(game_state)
        case "use":
            use_item(game_state, command_elements[1])
        case "go":
            move_player(game_state, command_elements[1])
        case "take":
            take_item(game_state, command_elements[1])
        case "inventory":
            show_inventory(game_state)
        case "quit":
            print("Игра окончена")
            raise KeyboardInterrupt


def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)

    while True:
        process_command(game_state, get_input(prompt="> "))



