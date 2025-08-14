
#Task 2: Prompt Player Choice
character_choice=input("choose your character")
print("1)Wizard")
print("2) Elf")
print("3) Human")
print("You chose option:", character_choice)

# Task 3: Player Choice

# Character stats
wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

# Loop until a valid choice is made
while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")

    choice = input("Choose your character (1, 2, or 3): ")

    if choice == "1":
        character = "Wizard"
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif choice == "2":
        character = "Elf"
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif choice == "3":
        character = "Human"
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("That is not a valid choice, try again.")

# Show player choice
print("You have chosen the", character)
print("HP:", my_hp)
print("Damage:", my_damage)



