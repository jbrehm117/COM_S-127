# Joseph Brehm       10.10.22
# Assignment 4 - Dungeon Crawler

import random
import time
import sys

print("[Dungeon Crawler] by Joseph Brehm")
print("[Com S 127, Section D]")
print("_____________________________________________")
print()

# Global Varibles
MAX_GOLD = 15
MIN_GOLD = 5
gold = 0
MAX_HEALTH = 100
health = 100
damage = 10
armor = 0
potionsAvailable = 1

# Stores data for visited rooms
isVisited = [False, False, False, False, False,
             False, False, False, False, False, False
             ]


def treasureChest(type):
    global health
    global damage
    global armor
    global potionsAvailable
    global MAX_HEALTH
    if type == 0:
        print("**You have found a sword!! Your damage has increased by 15...**")
        print()
        damage += 15
    elif type == 1:
        print("**You have found a shield!! Your armor has increased by 1...**")
        print()
        armor += 1
    elif type == 2:
        print("**You have found a potion!! You've added a potion to your bag...**")
        print()
        potionsAvailable += 1
    elif type == 3:
        print("A mystical presence fills your body...")
        print()
        MAX_HEALTH += 10
        health = MAX_HEALTH
    time.sleep(1.5)


def displayStats():
    global health
    global damage
    global armor
    global gold
    global potionsAvailable
    if potionsAvailable <= 0:
        print(
            "-----[Player]-----\nGold: {0}\nHealth: {1}\nArmor: {2}\nDamage: {3}\n------------------".format(gold, health, armor, damage))
    elif potionsAvailable > 0:
        print(
            "-----[Player]-----\nGold: {0}\nHealth: {1}\nArmor: {2}\nDamage: {3}\nPotions: {4}\n------------------".format(gold, health, armor, damage, potionsAvailable))


def combat(encounterChance, runChance, mHealth, mDamage, mArmor, monsterType, goldReward):
    global health
    global damage
    global armor
    global potionsAvailable
    global gold
    battleOver = False
    monster = {
        'Health': mHealth,
        'Armor': mArmor,
        'Attack': mDamage
    }
    if encounterChance > random.randint(0, 9):
        while battleOver == False:
            battle = input(
                "A monster is sleeping in the corner of the room... what will you do | [F]ight [R]un: ")
            battle = battle.upper()
            while battleOver == False:
                if battle == 'F':
                    print()
                    print(
                        "The {0} has awoken... it looks fearsome, prepare to fight!!".format(monsterType))
                    print()
                    time.sleep(1.5)
                    currentTurn = random.randint(0, 1)
                    while health > 0 and monster['Health'] > 0:
                        print("----[Monster]----")
                        for key, value in monster.items():
                            print(key + ':', value)
                        print("-----------------")
                        print()
                        displayStats()
                        print()
                        if currentTurn == 0:
                            healAmount = 25
                            print("Player's turn")
                            print("------------------")
                            attack = input(
                                '[A]ttack({0})    [H]eal({1}): '.format(damage, healAmount))
                            attack = attack.upper()
                            if attack == "A":
                                criticalChance = random.randint(0, 9)
                                if criticalChance > 7:
                                    monster["Health"] -= ((damage * 1.5) /
                                                          (monster["Armor"]+1))
                                    print(
                                        "Critical hit!! You have done", ((damage * 1.5) / (monster["Armor"]+1)), "damage to the monster...")
                                else:
                                    monster["Health"] -= (damage /
                                                          (monster["Armor"]+1))
                                    print(
                                        "You have done", (damage / (monster["Armor"]+1)), "damage to the monster...")
                                currentTurn += 1
                                currentTurn %= 2
                                time.sleep(1.5)
                            elif attack == "H":
                                if potionsAvailable > 0:
                                    if MAX_HEALTH > health:
                                        potionsAvailable -= 1
                                        if health <= (MAX_HEALTH - 25):
                                            health += 25
                                            print(
                                                "You have used 1 potion and healed for 25 health")
                                            print()
                                        elif health > (health - 25):
                                            healAmount = (MAX_HEALTH - health)
                                            health += healAmount
                                            print(
                                                "You have used 1 potion and healed for {0} because you cannot exceed your maximum health".format(healAmount))
                                            print()
                                    else:
                                        print(
                                            "You cannot heal because you already are at maximum health")
                                else:
                                    print(
                                        "You cannot heal because you don't have enough potions")
                                    print()
                                time.sleep(1.5)
                            else:
                                print("ERROR: PLEASE INPUT A VALID CHARACTER")
                        elif currentTurn == 1:
                            print("Monsters Turn")
                            print("------------------")
                            retaliateChance = random.randint(0, 1)
                            if retaliateChance == 0:
                                health -= (monster["Attack"] / (armor + 1))
                                print("The monster fights back and deals {} damage".format(
                                    monster["Attack"] / (armor + 1)))
                                print()
                                currentTurn += 1
                                currentTurn %= 2
                            elif retaliateChance == 1:
                                print("The monster has missed...")
                                print()
                                currentTurn += 1
                                currentTurn %= 2
                            time.sleep(1.5)
                    else:
                        if health <= 0:
                            battleOver = True
                            print("You have died in the dungeon... you dropped",
                                  gold, "gold on the floor.")
                            print()
                            sys.exit()
                        elif monster['Health'] <= 0:
                            battleOver = True
                            print()
                            print(
                                "**Congraduations you have defeated the monster!**")
                            print("The monster dropped", goldReward,
                                  "gold on the floor...")
                            gold += goldReward
                            print()
                            break
                        break
                elif battle == 'R':
                    if runChance > random.randint(0, 9):
                        print("You managed to sneak past the enemy...", end='\n\n')
                        battleOver = True
                    else:
                        print(
                            "You tried to run away, but the monster heard your footsteps... you have to fight!", end="\n\n")
                        battle = 'F'
                else:
                    print("ERROR: PLEASE INPUT A VALID CHARACTER")
    else:
        print("There seems to be a presense in this room...")
        print()


def room_0():
    if isVisited[0] == False:
        print("You have entered the dungeon...")
        isVisited[0] = True
    else:
        print("You've already visited this room...")


def room_1():
    if isVisited[1] == False:
        global gold
        randomGold = gold
        gold += random.randint(MIN_GOLD, MAX_GOLD)
        print(
            "There's {} gold on the floor and you pick it up.".format(gold-randomGold))
        print()
        isVisited[1] = True
    else:
        print("You've already visited this room...")


def room_2():
    if isVisited[2] == False:
        print("You've discovered a shop!!")
        print("--------------------------")
        print()
        isVisited[2] = True
    else:
        pass
    global gold
    global health
    global damage
    global armor
    global potionsAvailable
    global MAX_HEALTH
    while True:
        purchase = input(
            "There are items available for purchase, will you buy anything? [Y]es [N]o: ")
        print()
        purchase = purchase.upper()
        if purchase == 'Y':
            while True:
                items_to_purchase = input(
                    "What will you purchase? | [H]ealth (15g)   [A]rmor (12g)    [D]amage (20g)    [P]otions (25g) | [E]xit shop: ")
                items_to_purchase = items_to_purchase.upper()
                if items_to_purchase == 'H':
                    if gold >= 15:
                        gold -= 15
                        health += 10
                        MAX_HEALTH += 10
                        print("You have purchased 10 health!")
                    else:
                        print("You don't have enough gold")
                elif items_to_purchase == 'A':
                    if gold >= 12:
                        gold -= 12
                        armor += 1
                        print("You have purchased 1 armor!")
                    else:
                        print("You don't have enough gold")
                elif items_to_purchase == 'D':
                    if gold >= 20:
                        gold -= 20
                        damage += 5
                        print("You have purchased 5 damage!")
                    else:
                        print("You don't have enough gold")
                elif items_to_purchase == 'E':
                    print("Goodbye, hope to see you again")
                    print()
                    break
                elif items_to_purchase == 'P':
                    if gold >= 25:
                        gold -= 25
                        potionsAvailable += 1
                        print("You have purchased 1 potion!")
                    else:
                        print("You don't have enough gold")
                else:
                    print("ERROR: PLEASE INPUT A VALID CHARACTER")
                print()
        elif purchase == 'N':
            break
        else:
            print("ERROR: PLEASE INPUT A VALID CHARACTER")
            continue
    print("You've decided not to purchase anything...")


def room_11():
    global gold
    if isVisited[3] == False:
        combat(9, 5, 60, 10, 0, "slime", 15)
        randomGold = gold
        gold += random.randint(MIN_GOLD, MAX_GOLD)
        print(
            "There's {} gold on the floor and you pick it up.".format(gold-randomGold))
        print()
        isVisited[3] = True
    else:
        print("You've already visited this room...")
        combat(1, 5, 60, 10, 0, "slime", 15)


def room_neg9():
    global gold
    if isVisited[4] == False:
        combat(2, 5, 60, 10, 0, "slime", 15)
        randomTreasure = random.randint(0, 3)
        treasureChest(randomTreasure)
        randomGold = gold
        gold += random.randint(MIN_GOLD, MAX_GOLD)
        print(
            "There's {} gold on the floor and you pick it up.".format(gold-randomGold))
        print()
        isVisited[4] = True
    else:
        print("You've already visited this room...")
        combat(1, 5, 60, 10, 0, "slime", 15)


def room_neg8():
    global gold
    if isVisited[5] == False:
        combat(0, 5, 100, 15, 1, "knight", 20)
        randomGold = gold
        gold += random.randint(MIN_GOLD, MAX_GOLD)
        print(
            "There's {} gold on the floor and you pick it up.".format(gold-randomGold))
        print()
        isVisited[5] = True
    else:
        print("You've already visited this room...")
        combat(1, 5, 100, 15, 1, "knight", 20)


def room_12():
    global gold
    if isVisited[6] == False:
        combat(2, 5, 120, 20, 1, "big slime", 25)
        randomTreasure = random.randint(0, 3)
        treasureChest(randomTreasure)
        randomGold = gold
        gold += random.randint(MIN_GOLD, MAX_GOLD)
        print(
            "There's {} gold on the floor and you pick it up.".format(gold-randomGold))
        print()
        isVisited[6] = True
    else:
        print("You've already visited this room...")
        combat(4, 5, 120, 20, 1, "big slime", 25)


def room_13():
    global gold
    if isVisited[7] == False:
        combat(0, 5, 120, 20, 1, "big slime", 25)
        randomGold = gold
        gold += random.randint(MIN_GOLD, MAX_GOLD)
        print(
            "There's {} gold on the floor and you pick it up.".format(gold-randomGold))
        print()
        isVisited[7] = True
    else:
        print("You've already visited this room...")
        combat(2, 5, 120, 20, 1, "big slime", 25)


def room_14():
    global gold
    if isVisited[8] == False:
        combat(0, 5, 150, 20, 1.5, "fearsome knight", 30)
        randomTreasure = random.randint(0, 3)
        treasureChest(randomTreasure)
        randomGold = gold
        gold += random.randint(MIN_GOLD, MAX_GOLD)
        print(
            "There's {} gold on the floor and you pick it up.".format(gold-randomGold))
        print()
        isVisited[8] = True
    else:
        print("You've already visited this room...")
        combat(4, 5, 150, 20, 1.5, "fearsome knight", 30)


def room_4():
    global gold
    if isVisited[9] == False:
        combat(9, 5, 180, 30, 2, "dungeon janitor", 50)
        randomGold = gold
        gold += random.randint(MIN_GOLD, MAX_GOLD)
        print(
            "There's {} gold on the floor and you pick it up.".format(gold-randomGold))
        print()
        isVisited[9] = True
    else:
        print("You've already visited this room...")
        combat(2, 5, 180, 30, 2, "dungeon janitor", 50)


def room_5():
    global gold
    if isVisited[10] == False:
        combat(9, 5, 200, 30, 2.5, "dungeon boss", 1000)
        print()
        isVisited[10] = True
    else:
        print("You've already visited this room...")
        combat(9, 5, 200, 30, 2.5, "dungeon boss", 1000)


def controls():
    direction = input("[N]orth  [S]outh  [E]ast  [W]est: ")
    direction = direction.upper()  # Not case sensitive
    return direction


def main():
    gameOver = False
    direction = None
    roomNum = 0
    while True:
        main_menu = input("[P]lay     [I]nstructions     [Q]uit: ")
        main_menu = main_menu.upper()  # Not case sensitive

        if main_menu == 'P':
            while health > 0:
                while gameOver == False:
                    # Handles location of player
                    if roomNum == 0:
                        print()
                        room_0()
                        displayStats()
                        print()
                        print("Where will you go?")
                        direction = controls()
                        break
                    elif roomNum == 1:
                        print()
                        room_1()
                        displayStats()
                        print()
                        print("Where will you go?")
                        direction = controls()
                        break
                    elif roomNum == 2:
                        print()
                        room_2()
                        displayStats()
                        print()
                        print("Where will you go?")
                        direction = controls()
                        break
                    elif roomNum == 11:
                        print()
                        room_11()
                        displayStats()
                        print()
                        print("Where will you go?")
                        direction = controls()
                        break
                    elif roomNum == -9:
                        print()
                        room_neg9()
                        displayStats()
                        print()
                        print("Where will you go?")
                        direction = controls()
                        break
                    elif roomNum == -8:
                        print()
                        room_neg8()
                        displayStats()
                        print()
                        print("Where will you go?")
                        direction = controls()
                        break
                    elif roomNum == 12:
                        print()
                        room_12()
                        displayStats()
                        print()
                        print("Where will you go?")
                        direction = controls()
                        break
                    elif roomNum == 13:
                        print()
                        room_13()
                        displayStats()
                        print()
                        print("Where will you go?")
                        direction = controls()
                        break
                    elif roomNum == 14:
                        print()
                        room_14()
                        displayStats()
                        print()
                        print("Where will you go?")
                        direction = controls()
                        break
                    elif roomNum == 4:
                        print()
                        room_4()
                        displayStats()
                        print()
                        print("Where will you go?")
                        direction = controls()
                        break
                    elif roomNum == 5:
                        print()
                        room_5()
                        displayStats()
                        print()
                        print(
                            "Congraduations!! You have escaped the dungeon with", gold, "gold!! Thank you for playing, and see you next time...")
                        gameOver = True
                        sys.exit()
                    else:
                        # Handles if user inputs a direction that puts them out of range
                        print("OUCH!! You ran into a wall!!")
                        if direction == "S":
                            roomNum -= 1
                        elif direction == "N":
                            roomNum += 1
                        elif direction == "E":
                            roomNum -= 10
                        elif direction == "W":
                            roomNum += 10
                # Handles room movement
                if direction == "S":
                    roomNum += 1
                elif direction == "N":
                    roomNum -= 1
                elif direction == "E":
                    roomNum += 10
                elif direction == "W":
                    roomNum -= 10
                else:
                    print("ERROR: PLEASE INPUT A VALID CHARACTER")
        elif main_menu == "I":
            print("Instructions\n------------------------------------")
            print()
            print("[CONTROLS]")
            print("Use [N][S][E][W] to control the direction of your character.")
            print()
            print("[ROOM MECHANICS]")
            print("Monsters spawn in some rooms the first time you visit them,\nhowever, most rooms will spawn a monster randomly on the next")
            print("visit...")
            print(
                "*Note* a random amount of gold is rewarded for the discover of a new room")
            print()
            print("[BATTLE MECHANICS]")
            print("You have two choices when you enounter a monster...\n1) You can fight the monster\n2) You can attempt to run from the monster\n\nWhen in combat, you are also given two choices...")
            print("1) You can fight the monster\n2) You can heal using a potion\n*Note* healing from a potion doesn't take up your turn")
            print("*Note* after defeating a monster, you are rewarded with\nan amount of gold cooresponding to the monster type")
            print()
            print("[HOW TO WIN]")
            print("To win the game, you must find and defeat the dungeon boss")
            print("The rest is up to you...good luck adventurer...")
            print()
        elif main_menu == "Q":
            print("Sorry to see you go...")
            sys.exit()
        # Handles if user inputs a character that isn't P, I, or Q
        else:
            print("ERROR: PLEASE INPUT A VALID CHARACTER")


if __name__ == "__main__":
    main()
