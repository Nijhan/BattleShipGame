wizard= "Wizard"
elf= "Elf"
human= "Human"

#Hp characters
wizard_hp = 70
elf_hp = 100
human_hp = 150

#Damage characters
wizard_damage = 150
elf_damage = 100
human_damage = 20

#Addd gragon starts
dragon_hp = 300
dragon_damage = 50


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




#task4

# Create copies of HP so originals stay unchanged
current_dragon_hp = dragon_hp
current_my_hp = my_hp
while True:
    #player attacks the dragon
    current_dragon_hp = my_damage
    print(f"The {character} attacks and deals {my_damage} damage to the Dragon.")
    print(f"The Dragon's HP is now {current_dragon_hp}.")

    #check if dragon is defeated
    if current_dragon_hp <= 0:
        print("The Dragon has lost the battle! You win!\n")
        break
    #dragon attacks the player
    current_my_hp = dragon_damage
    print(f"The Dragon attacks and deals {dragon_damage} damage to the {character}.")
    print(f"The {character}'s HP is now {current_my_hp}.")


    #check if player is defeated
    if current_my_hp <= 0:
        print(f"The {character} has lost the battle! You lose!\n")
        break


