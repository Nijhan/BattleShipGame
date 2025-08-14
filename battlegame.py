# Task 3: Assign Player Stats Based on Choice

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
