# labyrinth_game/player_actions.py

from .constants import rooms
from .utils import describe_current_room


def show_inventory(game_state):
    if len(game_state['player_inventory']) == 0:
        print("Инвентарь пуст")
    else:
        print("Содержимое инвентаря: " + (", ").join(game_state['player_inventory']))


def get_input(prompt="> "):
    try:
        user_input = input(prompt)  # Запрашиваем ввод от пользователя
        return user_input  # Возвращаем введённое значение
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def move_player(game_state, direction):
    room = game_state.get('current_room')
    exits = rooms[room]['exits']
    for direct in exits:
        if direction == direct:
            game_state['current_room'] = rooms[room]['exits'][direction]
            game_state['steps_taken'] += 1
            describe_current_room(game_state)
        else:
            print("Нельзя пойти в этом направлении.")

def take_item(game_state, item_name):
    room = game_state.get('current_room')
    item_name = item_name.lower()
    if item_name in rooms[room]['items']:
        game_state['player_inventory'].append(item_name)
        rooms[room]['items'].remove(item_name)
        print("Вы подняли: " + item_name)
    else:
        print("Такого предмета здесь нет.")



