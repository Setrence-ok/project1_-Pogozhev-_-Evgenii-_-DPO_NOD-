# labyrinth_game/utils.py
import math

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
    if room == 'treasure_room':
        attempt_open_treasure(game_state)
    else:
        if rooms[room]['puzzle'] is not None and len(rooms[room]['puzzle']) > 1:
            print(rooms[room]['puzzle'][0])
            answer = input("Ваш ответ: ")
            if answer == rooms[room]['puzzle'][1] or answer.lower() == rooms[room]['puzzle'][2]:
                print("Поздравляю! Ответ верный! Награда добавлена в инвентарь.")
                rooms[room]['puzzle'] = None
                match game_state['current_room']:
                    case 'hall':
                        game_state['player_inventory'].append("shield")
                    case 'trap_room':
                        game_state['player_inventory'].append("trap")
                    case 'library':
                        game_state['player_inventory'].append("test_tube")
                    case 'outpatient':
                        game_state['player_inventory'].append("bandage")
                    case 'shop':
                        game_state['player_inventory'].append("knife")
            else:
                if room == 'trap_room':
                    print("Ответ неверный!")
                    trigger_trap(game_state)
                else:
                    print("Неверно. Попробуйте снова.")
        else:
            print("Загадок здесь нет.")


def attempt_open_treasure(game_state):
    room = game_state['current_room']
    if "treasure_key" in game_state['player_inventory']:
        print("Вы применяете ключ и замок щёлкает. Сундук открыт!")
        rooms[room]["items"].remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
    else:
        print("Сундук заперт. ... Ввести код? (да/нет)")
        answer = input("Введите ваш ответ: ")
        if answer.lower() == "да":
            print("Дверь защищена кодом. Введите код "
                  "(подсказка: это число пятикратного шага, 2*5= ? )")
            puzzle_answer = input("Введите ваш ответ: ")
            if puzzle_answer == rooms[room]['puzzle'][1]:
                print("Вы ввели верный код и замок щёлкает. Сундук открыт!")
                rooms[room]["items"].remove("treasure_chest")
                print("В сундуке сокровище! Вы победили!")
                game_state['game_over'] = True
            else:
                print("К сожалению ответ не верный!")
        else:
            print("Вы отступаете от сундука.")


def pseudo_random(seed, modulo):
    one = 12.9898
    two = 43758.5453
    value = math.sin(seed * one)
    value = value * two
    value = value - math.floor(value)
    value = value * modulo
    return int(value)


def trigger_trap(game_state):
    print("Ловушка активирована! Пол стал дрожать...")
    if len(game_state['player_inventory']) > 0:
        los_item = game_state['player_inventory'].pop(pseudo_random(game_state['steps_taken'],
                                                                    len(game_state['player_inventory'])))
        print(f"Вы потеряли: {los_item}")
    else:
        damage = pseudo_random(game_state['steps_taken'], 9)
        if damage > 5:
            print("Вы получили избыточный урон!")
            game_state['game_over'] = True
        else:
            print("Поздравляю! Вы уцелели")


def random_event(game_state):
    room = game_state['current_room']
    event = pseudo_random(game_state['steps_taken'], 11)
    if 0 <= event < 3:
        script = pseudo_random(game_state['steps_taken'], 3)
        match script:
            case 0:
                print("Вы нашли в комнате предмет: 'coin'")
                rooms[room]['items'].append("coin")
            case 1:
                print("Вы слышите пугающий шорох!")
                if "sword" in game_state['player_inventory']:
                    print("Вы отпунули существо предметом 'sword'")
                else:
                    print("К сожалению вам нечем отпугнуть существо")
            case 2:
                if game_state['current_room'] == "trap_room":
                    if "torch" not in game_state['player_inventory']:
                        print("Вы в опасности!")
                        trigger_trap(game_state)



def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")