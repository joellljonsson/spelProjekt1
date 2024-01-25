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
    attack_mc_lätt = 6
    attack_mc_tung = 9
    turn_mc = 0 
    
    hp_g = 100
    attack_g_light = 6
    attack_g_heavy = 8
    turn_g = 0

    while True:
        turn_mc = turn_mc + 1
        print(f"\nRunda {turn_mc} - Tur för MC")

        attack_val = input("Välj din attack - Lätt (L) eller Tung (T): ").upper()

        if attack_val == "T" and mana_mc >= attack_mc_tung * 1.5:
            mc_attack = attack_mc_tung
            mana_mc = mana_mc - (attack_mc_tung * 1.5)
            print(f"MC använder Tung Attack med {attack_mc_tung} skada. Mana: {mana_mc}")
        elif attack_val == "L":
            mc_attack = attack_mc_lätt 
            mana_mc = mana_mc - (attack_mc_lätt * 1.5)
            print(f"MC använder Lätt Attack med {attack_mc_lätt} skada. Mana: {mana_mc}")
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

        hp_mc = hp_mc - garmit_attack
        print(f"MC's HP: {hp_mc}")

        if hp_mc <= 0:
            print("MC är besegrad! Garmit vinner!")
            break

def girefiantVSmc():
    hp_mc = 80
    mana_mc = 150
    attack_mc_lätt = 6
    attack_mc_tung = 9
    tur_mc = 0 
    
    hp_gf = 100
    tur_gf = 0
    
    hälsa_flaska = 20
    mana_flaska = 30

    använt_hpflask = False
    använt_manaflask = False

    while True:
        tur_mc = tur_mc + 1
        print(f"\nRunda {tur_mc} - Tur för MC")

        val = input("\nVälj din handling - Attack (A), Använd hälsoflask (H), Använd manaflask (M): ").upper()

        if val == "A":
            attack_choice = input("\nVälj din attack - Lätt (L) eller Tung (T): ").upper()
            if attack_choice == "T" and mana_mc >= attack_mc_tung * 1.5:
                mc_attack = attack_mc_tung
                mana_mc = mana_mc - int(attack_mc_tung * 1.5)
                print(f"\nMC använder Tung Attack med {attack_mc_tung} skada. Mana: {mana_mc}")
            elif attack_choice == "L":
                mc_attack = attack_mc_lätt 
                mana_mc = mana_mc - int(attack_mc_lätt * 1.5)
                print(f"\nMC använder Lätt Attack med {attack_mc_lätt} skada. Mana: {mana_mc}")
            else:
                print("\nOgiltigt val. Du har gett fel input eller du har inte tillräcklig mana kvar.")
                continue

        elif val == "H":
            if not använt_hpflask:
                hp_mc = hp_mc + hälsa_flaska
                print(f"\nDu använde en hälsoflask och ökade din HP med {hälsa_flaska}. Din HP är nu {hp_mc}.")
                använt_hpflask = True
            else:
                print("\nDu har redan använt en hälsoflask denna strid.")
            continue

        elif val == "M":
            if not använt_manaflask:
                mana_mc = mana_mc + mana_flaska
                print(f"\nDu använde en manaflask och ökade din mana med {mana_flaska}. Din mana är nu {mana_mc}.")
                använt_manaflask = True
            else:
                print("\nDu har redan använt en manaflask denna strid.")
            continue

        else:
            print("\nOgiltigt val. Du har gett fel input. Turen för MC hoppas över.")
            continue
        
        if hp_gf <= 0:
            print("\nGire Fiant är besegrad! MC vinner!")
            break
        elif hp_mc <= 0 or mana_mc <= 0:
            break
        
        tur_gf = tur_gf + 1
        print(f"\nRunda {tur_gf} - Tur för Gire Fiant")

        if hp_mc <= 20:
            gf_attack = random.randint(7, 9)
            hp_mc = hp_mc - gf_attack
            print(f"\nGire Fiant använder  med {gf_attack} skada.")
        else:
            gf_attack = random.randint(6, 8)
            hp_mc = hp_mc - gf_attack
            print(f"\nGire Fiant använder Attack med {gf_attack} skada.")

        print(f"\nMC's HP: {hp_mc}")
        print(f"Gire Fiant's HP: {hp_gf}")

        hp_gf = hp_gf - mc_attack

        if hp_mc <= 0:
            print("\nMC är besegrad! Gire Fiant vinner!")
            break


def raygonVSmc():
    hp_mc = 100
    mana_mc = 150
    attack_mc_lätt = 8
    attack_mc_tung = 12
    tur_mc = 0 
    
    hp_raygon = 150
    tur_raygon = 0
    
    hpflask = 30
    manaflask = 40
    super_attack = 30

    använd_hpflaska = False
    använd_manaflaska = False
    använt_super = False

    while True:
        tur_mc += 1
        print(f"\nRunda {tur_mc} - MC:s Tur")

        val = input("\nVälj din val - Attack (A), Använd hälsodryck (H), Använd manaflaska (M), Använd kraftpotion (K): ").upper()

        if val == "A":
            attack_val = input("\nVälj din attack - Lätt (L) eller Tung (T): ").upper()
            if attack_val == "T" and mana_mc >= attack_mc_tung * 1.5:
                mc_attack = random.randint(attack_mc_tung, attack_mc_tung+2)
                mana_mc -= int(attack_mc_tung * 1.5)
                print(f"\nMC använder Tung Attack med {mc_attack} skada. Mana: {mana_mc}")
            elif attack_val == "L":
                mc_attack = random.randint(attack_mc_lätt, attack_mc_lätt+1)
                mana_mc -= int(attack_mc_lätt * 1.5)
                print(f"\nMC använder Lätt Attack med {mc_attack} skada. Mana: {mana_mc}")
            else:
                print("\nOgiltigt val. Antingen angav du fel input eller så har du inte tillräckligt med mana.")
                continue

        elif val == "H":
            if not använd_hpflaska:
                hp_mc += hpflask
                print(f"\nDu använde en hälsodryck och ökade din HP med {hpflask}. Din HP är nu {hp_mc}.")
                använd_hpflaska = True
            else:
                print("\nDu har redan använt en hälsodryck under denna strid.")
            continue

        elif val == "M":
            if not använd_manaflaska:
                mana_mc += manaflask
                print(f"\nDu använde en manaflaska och ökade din mana med {manaflask}. Din mana är nu {mana_mc}.")
                använd_manaflaska = True
            else:
                print("\nDu har redan använt en manaflaska under denna strid.")
            continue

        elif val == "K":
            if not använt_super:
                hp_raygon -= super_attack
                print(f"\nDu använde en kraftpotion och gjorde {super_attack} skada på Raygon. Raygons HP är nu {hp_raygon}.")
                använt_super = True
            else:
                print("\nDu har redan använt kraftpotion under denna strid.")
            continue

        else:
            print("\nOgiltigt val. Var god välj ett giltigt alternativ.")
            continue
        
        if hp_raygon <= 0:
            print("\nRaygon är besegrad! MC vinner!")
            break
        elif hp_mc <= 0 or mana_mc <= 0:
            print("\nMC är besegrad! Raygon vinner!")
            break
        
        tur_raygon += 1
        print(f"\nRunda {tur_raygon} - Raygons Tur")

        boss_attack = random.randint(10, 14)
        hp_mc -= boss_attack

        print(f"\nRaygon attackerar och gör {boss_attack} skada.")
        print(f"\nMC:s HP: {hp_mc}")
        print(f"Raygons HP: {hp_raygon}")

        if hp_mc <= 0:
            print("\nMC är besegrad! Raygon vinner!")
            break
        
        hp_raygon -= mc_attack

        if hp_raygon <= 0:
            print("\nRaygon är besegrad! MC vinner!")
            break
