#import modul
import random
import time
import sys

def forsenadPrint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

def is_valid_integer(input_str):
    return input_str.isdigit()

def start():
    while True:
        val = input("Vill du spela Sigma Souls?\n1. Ja\n2. Nej\n")
        if is_valid_integer(val):
            val = int(val)
            if val == 1:
                forsenadPrint("Du har valt att spela Sigma Souls.")
                break
            elif val == 2:
                forsenadPrint("Du har valt t inte spela Sigma Souls.")
                break
            else:
                forsenadPrint("Ogiltigt input, försök igen...\a")
        else:
            forsenadPrint("Felaktig inmatning, försök igen...\a")

def plot():
    while True:
        vapenval = input("Vad är din val då? \n1. Svärd\n2. Yxa\n3. Hammaren\n")
        if is_valid_integer(vapenval):
            vapenval = int(vapenval)
            if 1 <= vapenval <= 3:
                forsenadPrint(f"Du valde {vapenval}.")
                break
            else:
                forsenadPrint("Ogiltigt val, försök igen...\a")
        else:
            forsenadPrint("Felaktig inmatning, försök igen...\a")

def garmitVSmc():
    hp_mc = 50
    mana_mc = 100
    attack_mc_light = 5
    attack_mc_heavy = 8
    turn_mc = 0 
    
    hp_g = 100
    mana_g = 150
    attack_g_light = 6
    attack_g_heavy = 9
    turn_g = 0

    while True:
        turn_mc = turn_mc + 1
        print(f"\nRunda {turn_mc} - Tur för MC")

        attack_choice = input("Välj din attack - Lätt (L) eller Tung (T): ").upper()

        if attack_choice == "T" and mana_mc >= 20:
            mc_attack = attack_mc_heavy
            mana_mc = mana_mc - (attack_mc_heavy * 2)
            print(f"MC använder Tung Attack med {attack_mc_heavy} skada. Mana: {mana_mc}")
        elif attack_choice == "L":
            mc_attack = attack_mc_light 
            mana_mc = mana_mc - (attack_mc_light* 2)
            print(f"MC använder Lätt Attack med {attack_mc_light} skada. Mana: {mana_mc}")
        else:
            print("Ogiltigt val. Turen för MC hoppas över.")
            continue

        garmit_recieved = mc_attack
        hp_g -= garmit_recieved
        print(f"Garmit's HP: {hp_g}")

        if hp_g <= 0:
            print("Garmit är besegrad! MC vinner!")
            break

        turn_g += 1
        print(f"\nRunda {turn_g} - Tur för Garmit")


garmitVSmc()

forsenadPrint("Välkommen1\n")
start()
plot()


