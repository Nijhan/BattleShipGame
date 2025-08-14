# Task 4: Battle Simulation

current_dragon_hp = dragon_hp
current_my_hp = my_hp

while True:
    # Player attacks the dragon
    current_dragon_hp -= my_damage
    print(f"The {character} attacks and deals {my_damage} damage to the Dragon.")
    print(f"The Dragon's HP is now {current_dragon_hp}.")

    if current_dragon_hp <= 0:
        print("The Dragon has lost the battle! You win!")
        break

    # Dragon attacks the player
    current_my_hp -= dragon_damage
    print(f"The Dragon attacks and deals {dragon_damage} damage to the {character}.")
    print(f"The {character}'s HP is now {current_my_hp}.")

    if current_my_hp <= 0:
        print(f"The {character} has lost the battle! You lose!")
        break
