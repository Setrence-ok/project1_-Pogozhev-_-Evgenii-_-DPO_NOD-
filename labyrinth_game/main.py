#!/usr/bin/env python3

from .utils import describe_current_room
from .player_actions import show_inventory


def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    game_state = {
        'player_inventory': [],  # Инвентарь игрока
        'current_room': 'entrance',  # Текущая комната
        'game_over': False,  # Значения окончания игры
        'steps_taken': 0  # Количество шагов
    }
    describe_current_room(game_state)
    show_inventory(game_state)
    while True:



