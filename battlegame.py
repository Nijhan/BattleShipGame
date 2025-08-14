
# Task 1: Characters, HP, and Damage Setup

# Characters
# --- Task 1: Characters, HP, and Damage ---
wizard = "Wizard"
elf = "Elf"
human = "Human"

# HP
wizard_hp = 70
elf_hp = 100
human_hp = 150

# Damage
wizard_damage = 150
elf_damage = 100
human_damage = 20

# Dragon Stats
dragon_hp = 300
dragon_damage = 50

print("Task 1 complete: Characters and stats have been set up."

# --- Task 2: Prompt Player Choice ---
print("1) Wizard")
print("2) Elf")
print("3) Human")
character_choice = input("Choose your character (1, 2, or 3): ")
print("You chose option:", character_choice)


# --- Task 3: Assign Player Stats Based on Choice ---
if character_choice == "1":
    character = wizard
    my_hp = wizard_hp
    my_damage = wizard_damage
elif character_choice == "2":
    character = elf
    my_hp = elf_hp
    my_damage = elf_damage
elif character_choice == "3":
    character = human
    my_hp = human_hp
    my_damage = human_damage
else:
    print("Invalid choice. Defaulting to Human.")
    character = human
    my_hp = human_hp
    my_damage = human_damage

print(f"You have chosen the {character}")
print(f"HP: {my_hp}")
print(f"Damage: {my_damage}")


# --- Task 4: Battle Simulation ---
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
