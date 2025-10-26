# labyrinth_game/player_actions.py

def show_inventory(game_state):
    if len(game_state['player_inventory']) == 0:
        print("Инвентарь пуст")
    else:
        print("Содержимое инвентаря: " + (", ").join(game_state['player_inventory']))
