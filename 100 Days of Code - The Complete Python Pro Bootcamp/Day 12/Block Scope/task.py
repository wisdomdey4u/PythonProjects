game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

def increase_enemies():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)