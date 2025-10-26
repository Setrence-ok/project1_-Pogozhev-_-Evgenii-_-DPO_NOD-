# labyrinth_game/utils.py

from .constants import rooms


def describe_current_room(game_state):
    room = game_state.get('current_room')
    print(f"== {room.upper()} ==")
    for k, v in rooms[room].items():
            print(f"{v}")

