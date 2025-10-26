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
