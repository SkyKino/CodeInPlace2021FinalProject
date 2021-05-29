"""
Final Project: Anna Zhao

I wanted to do something similar to a turn-based RPG game where the enemies are random from easy, medium, boss, and rare. 
Attacks are random and the type of enemy encountered is random. The more wins, the higher chances of getting a difficult enemy
Hero can use items to heal their health and have a chance of finding them and will heal the player at a random amount between 25 and 100
I just want a game full of luck :)


"""
import random 

POTIONS = 1
STAMINA = 1
PLAYER_HP = 100

def main():
    # First asks the user if they want to know about some details for first playthough
    # Then asks for the user to input a name for the hero
    # The Player HP is default at 100
    # Every floor, a enemy spawns until defeated or the player is defeated
    Intro()
    NAME = input("Enter a name for the Hero: ")
    print()


    print("Welcome " + NAME +"!")
    print()
    global Floor_Number
    Floor_Number = 1
    print("You are currently on floor " + str(Floor_Number))
    print("")
    
    while PLAYER_HP > 0:
        Enemy_Spawn()
        print("-------------------------------------------")
        Player_Action()
    print("You reached floor", Floor_Number)
    print("Thank you for playing!")

def Intro():
    # Gives a brief overview of the game
    Start = input("Welcome to a quick RPG (Role-playing Game), type 1 if you want to read the extra details or ENTER to start the game ")
    if Start == str(1):
        print("Here are some important things to note: ")
        print("    - You start off with 1 potion and 1 stamina charge" )
        print("    - After each battle, there is a 30% chance of getting a new potion and 20% chance of getting stamina after every enemy turn (MAX OF 3)")
        print("    - Stamina is to use the special attack (option 2)")
        print("    - Please enjoy and also thank you Code in Place 2021")
    print("-------------------------------------------")

def Player_Action():
    # The player decides on the action they would like to take
    # 1 and 2 are attacks while 3 is recovery
    # The player will always move first

    global Floor_Number
    global PLAYER_HP
    print("Type 1 for Attack (10 to 20 damage) ")
    print("Type 2 for Special Attack (10 to 50 damage) ")
    print("Type 3 to use a potion (Recover 25 to 100 HP) ")
    Action = int(input("Your action: "))
    while Action > 3:
        print("Not a valid number, try again")
        print("-------------------------------------------")
        Action = int(input("Your action: "))

    if Action == 1: 
        global Attack_Damage
        global Enemy_HP
        global POTIONS
        Attack_Damage = random.randint(10,20)
        print("-------------------------------------------")
        print("You dealt " + str(Attack_Damage) + " damage!")
        Enemy_HP_Left = Enemy_HP - Attack_Damage
        if Enemy_HP_Left <= 0:
            print("The enemy is defeated!")
            print("")
            Floor_Number += 1
            print("You are now on floor:", Floor_Number)
            Pot_Pick = random.randint(1,11)
            if POTIONS != 3:
                if Pot_Pick >= 8:
                    POTIONS += 1
                    print("You picked up a potions! You now have", POTIONS, "left.")
            print("-------------------------------------------")
        else:
            Enemy_HP = Enemy_HP_Left
            print("The enemy has", Enemy_HP_Left, "HP left")
            print("-------------------------------------------")
            Enemy_Action()

        # Stamina is needed to use charge attack
    if Action == 2: 
        global STAMINA
        if STAMINA > 0:
            Attack_Damage = random.randint(10,50)
            STAMINA -= 1
            print("-------------------------------------------")
            print("You dealt " + str(Attack_Damage) + " damage!")
            print("You can use special:", STAMINA, "time(s) left")
            Enemy_HP_Left = Enemy_HP - Attack_Damage
            if Enemy_HP_Left <= 0:
                print("The enemy is defeated!")
                print("")
                Floor_Number += 1
                print("You are now on floor:", Floor_Number)
                Pot_Pick = random.randint(1,11)
                if POTIONS != 3:
                    if Pot_Pick >= 8:
                        POTIONS += 1
                        print("You picked up a potions! You now have", POTIONS, "left.")
                print("-------------------------------------------")
            else:
                Enemy_HP = Enemy_HP_Left
                print("The enemy has", Enemy_HP_Left, "hp left")
                print("-------------------------------------------")
                Enemy_Action()
        else:
            print("-------------------------------------------")
            print("Not enough stamina")
            print()
            Player_Action()


    if Action == 3:
        if POTIONS > 0:
            Heal = random.randint(25,101)
            PLAYER_HP = PLAYER_HP + Heal
            Potions_Left = POTIONS - 1
            print("-------------------------------------------")
            print("You used a potion! It healed you for "+ str(Heal) +" HP! You currently have " + str(Potions_Left) + " left and " + str(PLAYER_HP) +" HP")
            print()
            POTIONS -= 1
            Enemy_Action()
        else:
            print("-------------------------------------------")
            print("You do not have any potions left")
            print()
            Player_Action()

def Enemy_Action():
    # After a player's turn, the enemy will attack
    # Stronger attacks when increase in floors
    global PLAYER_HP
    global Floor_Number
    global STAMINA
    if Floor_Number < 10:
        Enemy_Damage = random.randint(5,16)
        PLAYER_HP -= Enemy_Damage
        print("The enemy did", Enemy_Damage, "damage and you have", PLAYER_HP, "HP left")
        print("")
        if PLAYER_HP <= 0:
            print("Game Over")
        else:
            Number = random.randint(1,11)
            if Number >= 9:
                if STAMINA != 3:
                    STAMINA += 1
                    print("You gained stamina back! You can now use special attack", STAMINA, "time(s)")
                    print("-------------------------------------------")
            Player_Action()


    if Floor_Number >= 10 and Floor_Number < 20:
        Enemy_Damage = random.randint(10,26)
        PLAYER_HP -= Enemy_Damage
        print("The enemy did", Enemy_Damage, "damage and you have", PLAYER_HP, "HP left")
        print("")
        if PLAYER_HP <= 0:
            print("Game Over")
        else:
            Number = random.randint(1,11)
            if Number >= 9:
                if STAMINA != 3:
                    STAMINA += 1
                    print("You gained stamina back! You can now use special attack", STAMINA, "time(s)")
                    print("-------------------------------------------")
            Player_Action()


    if Floor_Number >= 20:
        Enemy_Damage = random.randint(15,51)
        PLAYER_HP -= Enemy_Damage
        print("The enemy did", Enemy_Damage, "damage and you have", PLAYER_HP, "HP left")
        print("")
        if PLAYER_HP <= 0:
            print("Game Over")
        else:
            Number = random.randint(1,11)
            if Number >= 9:
                if STAMINA != 3:
                    STAMINA += 1
                    print("You gained stamina back! You can now use special attack", STAMINA, "time(s)")
                    print("-------------------------------------------")
            Player_Action()



def Enemy_Spawn():
    # Starting off, it would spawn easy enemies and then increases in difficulty afterwards
    global Floor_Number
    if Floor_Number < 5:
        Random_Number = random.randint(1,21)
        if Random_Number < 19:
            Enemy_Select_Easy()
        else:
            Enemy_Select_Rare()
            

    if Floor_Number >= 5 and Floor_Number < 10:
        Random_Number = random.randint(1,21)
        if Random_Number < 15:
            Enemy_Select_Easy()
        elif Random_Number >= 15 and Random_Number < 18:
            Enemy_Select_Med()
        else:
            Enemy_Select_Rare()

    if Floor_Number >= 10:
        Random_Number = random.randint(1,21)
        if Random_Number < 10:
            Enemy_Select_Easy()
        elif Random_Number >= 10 and Random_Number < 15:
            Enemy_Select_Med()
        elif Random_Number >= 15 and Random_Number < 18:
            Enemy_Select_Boss()
        else:
            Enemy_Select_Rare()

def Enemy_Select_Easy():
    Easy_Enemy_List = ["Blue Slime", "Yellow Slime", "Red Slime", "Green Slime"]
    Random_Enemy = Easy_Enemy_List[random.randint(0,3)]
    global Enemy_HP
    Enemy_HP = random.randint(15,35)
    print("A " + Random_Enemy + " appears! It has " + str(Enemy_HP) + " HP!")
    return Enemy_HP and Random_Enemy

def Enemy_Select_Med():
    Med_Enemy_List = ["Big Blue Slime", "Big Yellow Slime", "Big Red Slime", "Big Green Slime"]
    Random_Enemy = Med_Enemy_List[random.randint(0,3)]
    global Enemy_HP
    Enemy_HP = random.randint(36,50)
    print("A " + Random_Enemy + " appears! It has " + str(Enemy_HP) + " HP!")
    return Enemy_HP and Random_Enemy

def Enemy_Select_Boss():
    Boss_Enemy_List = ["Slime King", "Slime Army", "Slime Queen", "Derpy Slime Slime"]
    Random_Enemy = Boss_Enemy_List[random.randint(0,3)]
    global Enemy_HP
    Enemy_HP = random.randint(51,100)
    print("A boss " + Random_Enemy + " appears! It has " + str(Enemy_HP) + " HP!")
    return Enemy_HP and Random_Enemy

def Enemy_Select_Rare():
    Rare_Enemy_List = ["Mimic", "Ghost Slime", "Pinkie", "Rainbow Slime"]
    Random_Enemy = Rare_Enemy_List[random.randint(0,3)]
    global Enemy_HP
    Enemy_HP = random.randint(10,100)
    print("A rare " + Random_Enemy + " appears! It has " + str(Enemy_HP) + " HP!")
    return Enemy_HP and Random_Enemy

if __name__ == "__main__":
    main()
