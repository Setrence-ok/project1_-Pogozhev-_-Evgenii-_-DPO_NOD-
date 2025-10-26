# labyrinth_game/utils.py

from .constants import rooms


def describe_current_room(game_state):
    room_exit = []
    room = game_state.get('current_room')
    print(f"== {room.upper()} ==")
    print(f"{rooms[room]['description']}")
    for exit_direction, exit_room in rooms[room]['exits'].items():
        room_exit.append(exit_direction)
    if rooms[room]['items']:
        print("Заметные предметы: " + (", ").join(rooms[room]['items']))
    else:
        print("Предметов в комнате нет")
    print("Выходы: " + (", ").join(room_exit))

    if rooms[room]['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).")
    else:
        print("Загадок в комнате нет")


def solve_puzzle(game_state):
    room = game_state['current_room']
    if rooms[room]['puzzle'] is not None and len(rooms[room]['puzzle']) > 1:
        print(rooms[room]['puzzle'][0])
        answer = input("Ваш ответ: ")
        if answer == rooms[room]['puzzle'][1]:
            print("Поздравляю! Ответ верный! Награда добавлена в инвентарь.")
            rooms[room]['puzzle'] = None
            game_state['player_inventory'].append("prize")
        else:
            print("Неверно. Попробуйте снова.")
    else:
        print("Загадок здесь нет.")
