# Written by project contributors

import time
import random

random.seed()


# ----------------------------- Define Biomes -----------------------------
def define_biomes():
    # ---------------- forest ----------------
    forest_enemies = {
        'Goblin': Enemy('Goblin', 15, [2, 5]),
        'Shroom': Enemy('Shroom', 25, [5, 8])
    }
    forest_treasures = {
        'Bread Seed': Item('Bread Seed', 'seed', (0, 1), True),
        'Apple Seed': Item('Apple Seed', 'seed', (2, 5), True),
        'Crossbow': Item('Crossbow', 'weapon', 15, False),
        'Damage Potion': Item('Damage Potion', 'potion', ('damage', 10), True),
        'Heal Potion': Item('Heal Potion', 'potion', ('heal', 20), True),
        'Mystery Potion': Item('Mystery Potion', 'potion', ('reward', 0), True),
    }
    forest = Biome('Forest', 3, 3, forest_enemies, forest_treasures, 0.3, 0.65)

    # ---------------- desert ----------------
    desert_enemies = {
        'Scorpion': Enemy('Scorpion', 20, [4, 7]),
        'Worm': Enemy('Worm', 35, [6, 10])
    }
    desert_treasures = {
        'Apple Seed': Item('Apple Seed', 'seed', (3, 4), True),
        'Spear': Item('Spear', 'weapon', 18, False),
        'Damage Potion': Item('Damage Potion', 'potion', ('damage', 12), True),
        'Heal Potion': Item('Heal Potion', 'potion', ('heal', 25), True),
    }
    desert = Biome('Desert', 4, 4, desert_enemies, desert_treasures, 0.35, 0.60)

    # ---------------- tundra ----------------
    tundra_enemies = {
        'Wolf': Enemy('Wolf', 25, [5, 9]),
        'Ice Monster': Enemy('Frozen Giant', 45, [8, 12])
    }
    tundra_treasures = {
        'Berry Seed': Item('Berry Seed', 'seed', (2, 6), True),
        'Icicle': Item('Ice Blade', 'weapon', 5, False),
        'Damage Potion': Item('Damage Potion', 'potion', ('damage', 15), True),
        'Heal Potion': Item('Heal Potion', 'potion', ('heal', 30), True),
    }
    tundra = Biome('Tundra', 5, 5, tundra_enemies, tundra_treasures, 0.40, 0.55)

    # ---------------- swamp ----------------
    swamp_enemies = {
        'Slime': Enemy('Slime', 18, [3, 6]),
        'Swamp Monster': Enemy('Swamp Monster', 40, [7, 11])
    }
    swamp_treasures = {
        'Mushroom Seed': Item('Mushroom Seed', 'seed', (1, 3), True),
        'Swamp Sword': Item('Swamp Sword', 'weapon', 20, False),
        'Damage Potion': Item('Damage Potion', 'potion', ('damage', 14), True),
        'Heal Potion': Item('Heal Potion', 'potion', ('heal', 22), True),
    }
    swamp = Biome('Swamp', 4, 5, swamp_enemies, swamp_treasures, 0.38, 0.60)

    # ---------------- volcano ----------------
    volcano_enemies = {
        'Fire Monster': Enemy('Fire Monster', 30, [7, 10]),
        'Lava Beast': Enemy('Lava Beast', 55, [10, 15])
    }
    volcano_treasures = {
        'Bread Seed': Item('Bread Seed', 'seed', (4, 8), True),
        'Flame Sword': Item('Flame Sword', 'weapon', 28, False),
        'Damage Potion': Item('Damage Potion', 'potion', ('damage', 20), True),
        'Heal Potion': Item('Heal Potion', 'potion', ('heal', 35), True),
    }
    volcano = Biome('Volcano', 6, 6, volcano_enemies, volcano_treasures, 0.45, 0.50)

    return [forest, desert, tundra, swamp, volcano]


# ----------------------------- Time Functions -----------------------------

def updated_time(starting_time):
    return time.monotonic() - starting_time


def is_day(current_time, day_length, night_length):
    if current_time % (day_length + night_length) < day_length:
        return True
    return False


def date(current_time, day_length, night_length):
    return int(current_time // (day_length + night_length))


starting_time = time.monotonic()
current_time = time.monotonic() - starting_time


# ----------------------------- Character class -----------------------------
class Character:
    def __init__(self, name, health, damage, energy, modifiers, inventory,
                 location='Home', farm=None):
        self._name = name
        self._health = health
        self._damage = damage
        self._modifiers = modifiers
        self._energy = energy
        self._inventory = inventory
        self._location = location
        if farm is None:
            self._farm = []
        else:
            self._farm = farm

    def __str__(self):
        return ('Character: ' + self._name + '; Health: ' + str(self._health) +
                '; Damage: ' + str(self._damage) + '; Energy: ' + str(self._energy)
                + '; modifiers: ' + str(self._modifiers) + '; inventory: ' +
                str(self._inventory))

    def __repr__(self):
        return ('Character: ' + self._name + '\n' + 'Health: ' + str(self._health) +
                '\n' + 'Damage: ' + str(self._damage) + '\n' + 'Energy: ' +
                str(self._energy) + '\n' + 'modifiers: ' + str(self._modifiers) +
                '\n' + 'inventory: ' + str(self._inventory))

    def display_inventory(self):
        print('Here is your inventory:')
        if len(self._inventory) == 0:
            print('Oh! Your inventory is empty')
        else:
            for item in self._inventory:
                print(self._inventory[item][0]._name + ' x' +
                      str(self._inventory[item][1]))
        print()

    def add_to_inventory(self, item, item_amount):
        inventory = []
        inventory_type = []
        inventory_keys = []
        for inventory_item in self._inventory:
            inventory.append(self._inventory[inventory_item][0])
            inventory_type.append((self._inventory[inventory_item][0])._item_type)
            inventory_keys.append(inventory_item)

        if item._item_type == 'weapon':
            for item_index in range(len(inventory_type)):
                if inventory_type[item_index] == 'weapon':
                    print('You already have a weapon in your inventory')
                    user_choice = input('Would you like to discard your current ' +
                                        (inventory[item_index])._name +
                                        ' in order to take another item (Y/N): ')
                    while user_choice != 'Y' and user_choice != 'N':
                        user_choice = input('Please provide a valid answer (Y/N): ')
                    if user_choice == 'N':
                        return
                    del self._inventory[inventory_keys[item_index]]

        existing_item = False
        if item._stackable:
            for item_key in self._inventory:
                if self._inventory[item_key][0]._name == item._name:
                    self._inventory[item_key][1] += item_amount
                    existing_item = True

        if not existing_item:
            new_key = max(self._inventory.keys(), default=-1) + 1
            self._inventory[new_key] = [item, item_amount]

    def current_weapon(self):
        for item in self._inventory:
            if (self._inventory[item][0])._item_type == 'weapon':
                return self._inventory[item][0]
        return None


# ----------------------------- Biome class -----------------------------
class Biome:
    def __init__(self, name, rows, columns, biome_enemies,
                 biome_treasures, probability_enemy, probability_treasure):
        self._name = name
        self._rows = rows
        self._columns = columns
        self._size = rows * columns
        self._enemies = biome_enemies
        self._treasure = biome_treasures
        self._probability_treasure = probability_treasure
        self._probability_enemy = probability_enemy

    def __str__(self):
        return ('Biome:' + self._name + '\n' + str(self._rows) + '\n' +
                str(self._columns) + '\n' + str(self._size) + '\n' +
                str(self._enemies) + '\n' + str(self._treasure))

    def __repr__(self):
        return ('Biome:' + self._name + '\n' + str(self._rows) + '\n' +
                str(self._columns) + '\n' + str(self._size) + '\n' +
                str(self._enemies) + '\n' + str(self._treasure))


# ----------------------------- Item Class -----------------------------
class Item:
    def __init__(self, name, item_type, function, stackable):
        self._name = name
        self._item_type = item_type
        self._function = function
        self._stackable = stackable

        if self._item_type == 'seed':
            self._growth_time = function[0]

        if self._item_type == 'food':
            self._health = function[0]
            self._energy = function[1]

        if self._item_type == 'potion':
            self._potion_type = function[0]
            self._potion_value = function[1]


# ----------------------------- Enemy class -----------------------------
class Enemy:
    def __init__(self, name, starting_health, damage_range):
        self._name = name
        self.health = starting_health
        self._health = starting_health
        self._damage_range = damage_range


# ----------------------------- Save / Load Functions -----------------------------

def create_all_items():
    all_items = {
        'Sword': Item('Sword', 'weapon', 10, False),
        'Bread Seed': Item('Bread Seed', 'seed', (0, 1), True),
        'Apple Seed': Item('Apple Seed', 'seed', (2, 5), True),
        'Berry Seed': Item('Berry Seed', 'seed', (2, 6), True),
        'Mushroom Seed': Item('Mushroom Seed', 'seed', (1, 3), True),
        'Watering Can': Item('Watering Can', 'object', None, False),
        'Damage Potion': Item('Damage Potion', 'potion', ('damage', 10), True),
        'Heal Potion': Item('Heal Potion', 'potion', ('heal', 20), True),
        'Mystery Potion': Item('Mystery Potion', 'potion', ('reward', 0), True),
        'Crossbow': Item('Crossbow', 'weapon', 15, False),
        'Spear': Item('Spear', 'weapon', 18, False),
        'Ice Blade': Item('Ice Blade', 'weapon', 5, False),
        'Swamp Sword': Item('Swamp Sword', 'weapon', 20, False),
        'Flame Sword': Item('Flame Sword', 'weapon', 28, False),
    }

    return all_items


def create_starting_inventory(all_items):
    starting_inventory = {
        0: [all_items['Sword'], 1],
        1: [all_items['Bread Seed'], 3],
        2: [all_items['Watering Can'], 1],
        3: [all_items['Damage Potion'], 2],
        4: [all_items['Heal Potion'], 2],
        5: [all_items['Mystery Potion'], 1],
    }

    return starting_inventory


def convert_farm_value(value):
    if value == 'True':
        return True
    elif value == 'False':
        return False
    elif value == 'None':
        return None

    try:
        return int(value)
    except ValueError:
        return value


def save_game(player):
    out_file_name = 'data/player_data.txt'

    with open(out_file_name, 'w') as out_file:
        out_file.write(str(player._name) + '\n')
        out_file.write(str(player._health) + '\n')
        out_file.write(str(player._damage) + '\n')
        out_file.write(str(player._energy) + '\n')
        out_file.write(str(player._location) + '\n')

        for modifier in player._modifiers:
            out_file.write(str(modifier) + ',')
        out_file.write('\n')

        for item_key in player._inventory:
            item = player._inventory[item_key][0]
            amount = player._inventory[item_key][1]
            out_file.write(item._name + ',' + str(amount) + '\n')

    print('[Game Saved]')


def load_game(all_items):
    in_file_name = 'data/player_data.txt'

    with open(in_file_name, 'r') as in_file:
        lines = in_file.readlines()

    name = lines[0].strip()
    health = int(lines[1].strip())
    damage = int(lines[2].strip())
    energy = int(lines[3].strip())
    location = lines[4].strip()

    modifiers_line = lines[5].strip()
    modifiers = []
    if modifiers_line != '':
        modifiers_parts = modifiers_line.split(',')
        for modifier in modifiers_parts:
            if modifier != '':
                modifiers.append(modifier)

    inventory = {}
    inventory_key = 0

    for line_index in range(6, len(lines)):
        line = lines[line_index].strip()

        if line != '':
            item_data = line.split(',')
            item_name = item_data[0]
            item_amount = int(item_data[1])

            if item_name in all_items:
                inventory[inventory_key] = [all_items[item_name], item_amount]
                inventory_key += 1

    return Character(name, health, damage, energy, modifiers, inventory, location)


def save_farming(player):
    out_file_name = 'data/farm_data.txt'

    with open(out_file_name, 'w') as out_file:
        for plot in player._farm:
            for value in plot:
                out_file.write(str(value) + ',')
            out_file.write('\n')

    print('[Farming Saved]')


def load_farming():
    in_file_name = 'data/farm_data.txt'
    farm = []

    try:
        with open(in_file_name, 'r') as in_file:
            lines = in_file.readlines()
    except FileNotFoundError:
        return farm

    for line in lines:
        line = line.strip()

        if line != '':
            plot_data = line.split(',')
            plot = []
            for value in plot_data:
                if value != '':
                    plot.append(convert_farm_value(value))
            farm.append(plot)

    return farm


def create_new_player(all_items):
    starting_inventory = create_starting_inventory(all_items)
    return Character('Elf', 120, 10, 100, [], starting_inventory, 'Home', [])


# ----------------------------- Combat Functions -----------------------------
def generate_enemy(biome):
    enemy = random.choice(list(biome._enemies.values()))
    enemy._health = enemy.health
    return enemy


def play_combat(player, enemy, biome):
    starting_health = player._health
    print("You've entered combat against " + enemy._name)

    weapon = player.current_weapon()
    if weapon is None:
        print("You have no weapon! You can't fight.")
        return 'enemy'

    print('Your current weapon is the ' + weapon._name +
          ', which does ' + str(weapon._function) + ' damage.')

    while enemy._health > 0 and player._health > 0:
        print('\n--- Your HP: ' + str(player._health) +
              ' | ' + enemy._name + ' HP: ' + str(enemy._health) + ' ---')
        user_choice = input("Press Enter to attack or 'i' to use item: ")

        if user_choice == 'i':
            player.display_inventory()
            user_choice = input('Please enter the name of the item you' +
                                ' would like to use: ')
            inventory = []
            for item in player._inventory:
                inventory.append((player._inventory[item][0])._name)

            if user_choice in inventory:
                for used_item in list(player._inventory.keys()):
                    if user_choice == (player._inventory[used_item][0])._name:
                        if (player._inventory[used_item][0])._item_type == 'food':
                            player._health += (player._inventory[used_item][0])._health
                            player._energy += (player._inventory[used_item][0])._energy
                            player._inventory[used_item][1] -= 1
                            if player._inventory[used_item][1] == 0:
                                del player._inventory[used_item]

                            enemy_damage = random.randint(enemy._damage_range[0],
                                                          enemy._damage_range[1])
                            player._health -= enemy_damage
                            if player._health < 0:
                                player._health = 0
                            print(enemy._name + ' dealt ' + str(enemy_damage) +
                                  ' damage. You have ' + str(player._health) + ' HP left.')
                            break

                        elif (player._inventory[used_item][0])._item_type == 'potion':
                            used_potion = player._inventory[used_item][0]

                            if used_potion._potion_type == 'damage':
                                enemy._health -= used_potion._potion_value
                                if enemy._health < 0:
                                    enemy._health = 0
                                print('You threw ' + used_potion._name + ' at ' +
                                      enemy._name + ' for ' +
                                      str(used_potion._potion_value) + ' damage! ' +
                                      enemy._name + ' has ' +
                                      str(enemy._health) + ' HP left.')

                            elif used_potion._potion_type == 'heal':
                                player._health += used_potion._potion_value
                                print('You drank ' + used_potion._name +
                                      ' and restored ' +
                                      str(used_potion._potion_value) +
                                      ' HP. HP is now ' +
                                      str(player._health) + '.')

                            elif used_potion._potion_type == 'reward':
                                treasure = generate_treasure(biome)
                                print('The ' + used_potion._name +
                                      ' shimmers and produces a ' +
                                      treasure._name + '!')
                                player.add_to_inventory(treasure, 1)

                            player._inventory[used_item][1] -= 1
                            if player._inventory[used_item][1] == 0:
                                del player._inventory[used_item]

                            if enemy._health > 0:
                                enemy_damage = random.randint(enemy._damage_range[0],
                                                              enemy._damage_range[1])
                                player._health -= enemy_damage
                                if player._health < 0:
                                    player._health = 0
                                print(enemy._name + ' dealt ' + str(enemy_damage) +
                                      ' damage. You have ' +
                                      str(player._health) + ' HP left.')
                            break

                        else:
                            print('You cannot use that item in this combat')
                            break
            else:
                print('You do not have that item to use!')

        elif user_choice == '':
            enemy._health -= weapon._function
            if enemy._health < 0:
                enemy._health = 0
            print('You dealt ' + str(weapon._function) + ' damage. ' +
                  enemy._name + ' has ' + str(enemy._health) + ' HP left.')

            if enemy._health <= 0:
                break

            enemy_damage = random.randint(enemy._damage_range[0],
                                          enemy._damage_range[1])
            player._health -= enemy_damage
            if player._health < 0:
                player._health = 0
            print(enemy._name + ' dealt ' + str(enemy_damage) +
                  ' damage. You have ' + str(player._health) + ' HP left.')
        else:
            print('Please provide a valid response')

    if enemy._health <= 0 and player._health > 0:
        return 'player'
    elif player._health <= 0 and enemy._health <= 0:
        return 'tie'
    else:
        return 'enemy'


def combat(biome, player):
    enemy = generate_enemy(biome)
    result = play_combat(player, enemy, biome)
    if result == 'player':
        print('The player won!')
        reward(biome, player)
    elif result == 'enemy':
        print('The enemy won.')
    else:
        print('Both the player and the enemy died in this combat.')


# ----------------------------- Movement and Treasure Functions -----------------------------
def get_home_movement():
    return input('Where would you like to go? (up/down/left/right/quit): ')


def get_biome_movement(player, energy_per_move):
    print('\n------------------------------')
    print('  HP: ' + str(player._health)
          + '  |  Energy: ' + str(player._energy) + ' (each movement costs '
          + str(energy_per_move) + ')')
    player.display_inventory()
    return input('Where would you like to go? (up/down/left/right/home/quit): ')


def generate_location(biome):
    if random.random() < biome._probability_enemy:
        return 'combat'
    elif random.random() < biome._probability_treasure:
        return 'reward'
    else:
        return 'empty'


def generate_treasure(biome):
    return random.choice(list(biome._treasure.values()))


def reward(biome, player):
    treasure = generate_treasure(biome)
    print('You received a ' + treasure._name + '!')
    player.add_to_inventory(treasure, 1)


# ----------------------------- Map Generation -----------------------------

directions = ['up', 'down', 'left', 'right']


def generate_current_map(all_biomes):
    current_map = {}
    used_biomes = []
    for direction in directions:
        biome = random.choice(all_biomes)
        while biome in used_biomes:
            biome = random.choice(all_biomes)
        used_biomes.append(biome)
        current_map[direction] = biome
    return current_map


def show_map(current_map):
    print()
    print('=========== Current Map ===========')
    print('          ' + current_map['up']._name)
    print()
    print(current_map['left']._name
          + '     Home     '
          + current_map['right']._name)
    print()
    print('          ' + current_map['down']._name)
    print('==================================')
    print()


def choose_biome_from_map(current_map):
    show_map(current_map)
    player_choice = get_home_movement()

    if player_choice == 'quit':
        return 'quit'

    while player_choice not in directions:
        print('Invalid direction. Try again.')
        player_choice = get_home_movement()

        if player_choice == 'quit':
            return 'quit'

    return current_map[player_choice]


def explore_biome(biome, player, energy_per_move):
    print('\n==============================')
    print('You entered the ' + biome._name + '!')
    print('==============================')
    player._location = biome._name
    player_choice = get_biome_movement(player, energy_per_move)

    if player_choice == 'quit':
        return 'quit'

    while player_choice != 'home':
        if player_choice not in directions:
            print('Invalid direction. Try again.')
        else:
            player._energy -= energy_per_move
            if player._energy <= 0:
                player._energy = 0
                print('\nYou ran out of energy!')
                print('You are teleported home.')
                player._location = 'Home'
                return True

            print('\n==============================')
            location = generate_location(biome)
            if location == 'combat':
                combat(biome, player)
            elif location == 'reward':
                print('You found a treasure chest!')
                reward(biome, player)
            else:
                print('Nothing here...')
            print('==============================')

            if player._health <= 0:
                print('You died! Game over.')
                return False

        player_choice = get_biome_movement(player, energy_per_move)

        if player_choice == 'quit':
            return 'quit'

    print('You go back home.')
    player._location = 'Home'
    return True


# ------------------------------ Main function ------------------------------
def main():
    all_items = create_all_items()

    load_choice = input('Load previous game? (Y/N): ')

    while load_choice != 'Y' and load_choice != 'N':
        load_choice = input('Please provide a valid answer (Y/N): ')

    if load_choice == 'Y':
        player = load_game(all_items)
        player._farm = load_farming()
        print('[Save file loaded.]')
    else:
        player = create_new_player(all_items)
        player._farm = []
        print('[New game started.]')

    all_biomes = define_biomes()
    energy_per_move = 5

    print('==============================')
    print(' Welcome to the Survival Game!')
    print('==============================')

    game_over = False

    while not game_over:
        current_map = generate_current_map(all_biomes)
        print('\n------------------------------')
        print('HP: ' + str(player._health) +
              ' | Energy: ' + str(player._energy) +
              ' (movement cost: ' + str(energy_per_move) + ')')
        print('------------------------------')
        player.display_inventory()

        biome = choose_biome_from_map(current_map)

        if biome == 'quit':
            save_game(player)
            save_farming(player)
            print('Game saved. You quit the game.')
            game_over = True
        else:
            still_alive = explore_biome(biome, player, energy_per_move)

            save_game(player)
            save_farming(player)

            if still_alive == 'quit':
                print('Game saved. You quit the game.')
                game_over = True
            elif not still_alive:
                game_over = True
            else:
                print('\nYou return home.')
                print('The world changes and a new map appears.')

        print()

    print('\nGame Over.')


if __name__ == "__main__":
    main()
