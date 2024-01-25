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
    hp_mc = 80
    mana_mc = 150
    attack_mc_light = 6
    attack_mc_heavy = 9
    turn_mc = 0 
    
    hp_g = 100
    # mana_g = 150
    attack_g_light = 6
    attack_g_heavy = 8
    turn_g = 0

    while True:
        turn_mc = turn_mc + 1
        print(f"\nRunda {turn_mc} - Tur för MC")

        attack_choice = input("Välj din attack - Lätt (L) eller Tung (T): ").upper()

        if attack_choice == "T" and mana_mc >= attack_mc_heavy * 1.5:
            mc_attack = attack_mc_heavy
            mana_mc = mana_mc - (attack_mc_heavy * 1.5)
            print(f"MC använder Tung Attack med {attack_mc_heavy} skada. Mana: {mana_mc}")
        elif attack_choice == "L":
            mc_attack = attack_mc_light 
            mana_mc = mana_mc - (attack_mc_light * 1.5)
            print(f"MC använder Lätt Attack med {attack_mc_light} skada. Mana: {mana_mc}")
        else:
            print("Ogiltigt val. Du har gett fel input eller du har inte tillräcklig mana kvar. Turen för MC hoppas över.")
            continue
        
        garmit_received = mc_attack
        hp_g = hp_g - garmit_received
        print(f"Garmit's HP: {hp_g}")

        if hp_g <= 0:
            print("Garmit är besegrad! MC vinner!")
            break
        elif hp_mc <= 0 or mana_mc <= 0:
            # print("du tog texten här")
            break
        
        turn_g = turn_g + 1
        print(f"\nRunda {turn_g} - Tur för Garmit")

        if hp_mc <= 20:
            garmit_attack = attack_g_heavy
            print(f"Garmit använder Tung Attack med {attack_g_heavy} skada.")
        else:
            garmit_attack = attack_g_light
            print(f"Garmit använder Lätt Attack med {attack_g_light} skada.")

        hp_mc -= garmit_attack
        print(f"MC's HP: {hp_mc}")

        if hp_mc <= 0:
            print("MC är besegrad! Garmit vinner!")
            break
def girefiantVSmc():
    hp_mc = 80
    mana_mc = 150
    attack_mc_light = 6
    attack_mc_heavy = 9
    turn_mc = 0 
    
    hp_gf = 100
    attack_gf_light = 6
    attack_gf_heavy = 8
    turn_gf = 0

    while True:
        turn_mc = turn_mc + 1
        print("\nRunda", turn_mc, "- Tur för MC")

        attack_choice = input("Välj din attack - Lätt (L) eller Tung (T): ").upper()

        if attack_choice == "T" and mana_mc >= attack_mc_heavy * 1.5:
            mc_attack2 = attack_mc_heavy
            mana_mc = mana_mc - (attack_mc_heavy * 1.5)
            print("MC använder Tung Attack med", attack_mc_heavy, "skada. Mana:", mana_mc)
        elif attack_choice == "L":
            mc_attack = attack_mc_light 
            mana_mc = mana_mc - (attack_mc_light * 1.5)
            print("MC använder Lätt Attack med", attack_mc_light, "skada. Mana:", mana_mc)
        else:
            print("Ogiltigt val. Du har gett fel input eller du har inte tillräcklig mana kvar. Turen för MC hoppas över.")
            continue
        
        if hp_gf <= 0:
            print("Gire Fiant är besegrad! MC vinner!")
            break
        elif hp_mc <= 0:
            break
        
        turn_gf = turn_gf + 1
        print("\nRunda", turn_gf, "- Tur för Gire Fiant")

        if hp_mc <= 20:
            gf_attack = attack_gf_heavy
            hp_mc = hp_mc - gf_attack
            print("MC's HP:", hp_mc)
        else:
            gf_attack = attack_gf_light
            hp_mc = hp_mc - gf_attack
            print("MC's HP:", hp_mc)

        if hp_mc <= 0:
            print("MC är besegrad! Gire Fiant vinner!")
            break

garmitVSmc()

# forsenadPrint("Välkommen1\n")
# start()
# plot()


