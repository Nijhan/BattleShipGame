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







#task4
character = wizard         
my_hp = wizard_hp
my_damage = wizard_damage

# Create copies of HP so originals stay unchanged
current_dragon_hp = dragon_hp
current_my_hp = my_hp

character = wizard         
my_hp = wizard_hp
my_damage = wizard_damage

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

    