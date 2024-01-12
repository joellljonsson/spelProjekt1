import random
import os

#########################
### Navigatinossystem ###
#########################


# Vilket rum man befinner sig i
position = "a2"

# Variabler som håller koll på vilket rum man har varit i, 0 = inte varit i rummet, 1 = varit eller befinner sig i rummet
a1E = 0
a2E = 0
a3E = 0
a4E = 0
a5E = 0
a1V = 0
a3V = 0
a4V = 0
a5V = 0
b2E = 0
b3b4E = 0
bcd5E = 0
cd1E = 0
c2E = 0
cd3cd4E = 0
d2E = 0
b2V = 0
b3b4V = 0
bcd5V = 0
bcd5V2 = 0
bcd5V3 = 0
cdV1 = 0
cdV2 = 0
c2V = 0
cd3cd4V = 0
cd3cd4V2 = 0
d2E = 0
d2V = 0

# funktion för att avsluta spelet
def avslutaSpel():
    # print som ger dig 2 val
    print("Är du säker på att du vill avsluta?")
    print("'bekräfta' eller 'avbryt'")
    # input där du svarar på frågan ovan
    while True:
        svar = input("...")
        # 2 listor med fel- och rättstavelser
        olikaSvarB = ["bekräfta", "bäkrefta", "b", "bekräftga", "bekrägta", "berkäfta"]
        olikaSvarA = ["avnryt", "avbryt", "abvryt", "avbrty", "avbrty", "a"]
        if svar.lower() in olikaSvarB:
            # om svar är bekräfta så avslutas spelet
            exit("Spelet avsutas...")
        elif svar.lower() in olikaSvarA:
            # om svar är avbryt så fortätter spelet
            os.system("clear")
            break
        else:
            # om svaret inte finns på någon lista
            print("Svara med 'bekräfta för att avsluta spelet\nEller skriv 'avbryt' för att fortsätta spela")
        os.system("clear")

# funktion för rum a1
def a1():
    os.system("clear")
    global position
    global a1E
    if a1E == 0:
        a1E = 1    
    print(f"Nu är du i {position}")
    karta()
    while True:
        flytta = input()
        if flytta.lower() == "w":
            print("error")
        elif flytta.lower() == "a":
            print("error")
        elif flytta.lower() == "d":
            position = "a2"
            a2()
        elif flytta.lower() == "s":
            print("error")
        elif flytta.lower() == "karta":
            karta()
        elif flytta.lower() == "exit":
            avslutaSpel()            
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum a2
def a2():
    os.system("clear")
    global position
    print(f"Nu är du i {position}")
    karta()
    while True:
        flytta = input()
        if flytta.lower() == "w":
            position = "b2"
            b2()
        elif flytta.lower() == "a":
            position = "a1"
            a1()
        elif flytta.lower() == "d":
            position = "a3"
            a3()
        elif flytta.lower() == "s":
            print("error")
        elif flytta.lower() == "karta":
            karta()
        elif flytta.lower() == "exit":
            avslutaSpel()
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum a3
def a3():
    os.system("clear")
    global position
    global a3E
    if a3E == 0:
        a3E = 1
    print(f"Nu är du i {position}")
    karta()
    while True:
        flytta = input()
        if flytta.lower() == "w":
            position = "b3b4"
            b3b4()
        elif flytta.lower() == "a":
            position = "a2"
            a2()
        elif flytta.lower() == "d":
            print("error")
        elif flytta.lower() == "s":
            print("error")
        elif flytta.lower() == "karta":
            karta()  
        elif flytta.lower() == "exit":
            avslutaSpel()                      
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum a4
def a4():
    os.system("clear")
    global position
    global a4E
    if a4E == 0:
        a4E = 1
    print(f"Nu är du i {position}")
    karta()
    while True:
        flytta = input()
        if flytta.lower() == "w":
            print("error")
        elif flytta.lower() == "a":
            print("error")
        elif flytta.lower() == "d":
            position = "a5"
            a5()
        elif flytta.lower() == "s":
            print("error")
        elif flytta.lower() == "karta":
            karta()
        elif flytta.lower() == "exit":
            avslutaSpel()
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum a5
def a5():
    os.system("clear")
    global position
    global a5E
    if a5E == 0:
        a5E = 1
    print(f"Nu är du i {position}")
    karta()
    while True:
        flytta = input()
        if flytta.lower() == "w":
            position = "bcd5"
            bcd5()
        elif flytta.lower() == "a":
            position = "a4"
            a4()
        elif flytta.lower() == "d":
            print("error")
        elif flytta.lower() == "s":
            print("error")
        elif flytta.lower() == "karta":
            karta()
        elif flytta.lower() == "exit":
            avslutaSpel()
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum b2
def b2():
    os.system("clear")
    global position
    global b2E
    if b2E == 0:
        b2E = 1
    print(f"Nu är du i {position}")
    karta()
    while True:
        flytta = input()
        if flytta.lower() == "w":
            print("error")
        elif flytta.lower() == "a":
            print("error")
        elif flytta.lower() == "d":
            print("error")
        elif flytta.lower() == "s":
            position = "a2"
            a2()
        elif flytta.lower() == "karta":
            karta()  
        elif flytta.lower() == "exit":
            avslutaSpel() 
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum b3b4
def b3b4():
    os.system("clear")
    global position
    global b3b4E
    if b3b4E == 0:
        b3b4E = 1
    print(f"Nu är du i {position}")
    karta()
    while True:
        flytta = input()
        if flytta.lower() == "w":
            position = "cd3cd4"
            cd3cd4()
        elif flytta.lower() == "a":
            print("error")
        elif flytta.lower() == "d":
            print("error")
        elif flytta.lower() == "s":
            position = "a3"
            a3()
        elif flytta.lower() == "karta":
            karta()   
        elif flytta.lower() == "exit":
            avslutaSpel()
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum bcd5
def bcd5():
    os.system("clear")
    global position
    global bcd5E
    if bcd5E == 0:
        bcd5E = 1
    print(f"Nu är du i {position}")
    karta()
    while True:
        flytta = input()
        if flytta.lower() == "w":
            print("error")
        elif flytta.lower() == "a":
            position = "cd3cd4"
            cd3cd4()
        elif flytta.lower() == "d":
            print("error")
        elif flytta.lower() == "s":
            position = "a5"
            a5()
        elif flytta.lower() == "karta":
            karta()   
        elif flytta.lower() == "exit":
            avslutaSpel()
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum cd1
def cd1():
    os.system("clear")
    global position
    global cd1E
    if cd1E == 0:
        cd1E = 1
    print(f"Nu är du i {position}")
    karta()
    while True:
        flytta = input()
        if flytta.lower() == "w":
            print("error")
        elif flytta.lower() == "a":
            print("error")
        elif flytta.lower() == "d":
            position = "c2"
            c2()
        elif flytta.lower() == "s":
            print("error")
        elif flytta.lower() == "karta":
            karta()  
        elif flytta.lower() == "exit":
            avslutaSpel()
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum c2
def c2():
    os.system("clear")
    global position
    global c2E
    if c2E == 0:
        c2E = 1
    print(f"Nu är du i {position}")
    karta()
    while True:
        flytta = input()
        if flytta.lower() == "w":
            position = "d2"
            d2()
        elif flytta.lower() == "a":
            position = "cd1"
            cd1()
        elif flytta.lower() == "d":
            position = "cd3cd4"
            cd3cd4()
        elif flytta.lower() == "s":
            print("error")
        elif flytta.lower() == "karta":
            karta() 
        elif flytta.lower() == "exit":
            avslutaSpel() 
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum cd3cd4
def cd3cd4():
    os.system("clear")
    global position
    global cd3cd4E
    if cd3cd4E == 0:
        cd3cd4E = 1
    print(f"Nu är du i {position}")
    karta()
    while True:
        flytta = input()
        if flytta.lower() == "w":
            print("error")
        elif flytta.lower() == "a":
            position = "c2"
            c2()
        elif flytta.lower() == "d":
            position = "bdc5"
            bcd5()
        elif flytta.lower() == "s":
            position = "b3b4"
            b3b4()
        elif flytta.lower() == "karta":
            karta()  
        elif flytta.lower() == "exit":
            avslutaSpel()
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum d2
def d2():
    os.system("clear")
    global position
    global d2E
    if d2E == 0:
        d2E = 1
    print(f"Nu är du i {position}")
    karta()
    while True:
        flytta = input()
        if flytta.lower() == "w":
            print("error")
        elif flytta.lower() == "a":
            print("error")
        elif flytta.lower() == "d":
            print("error")
        elif flytta.lower() == "s":
            position = "c2"
            c2()
        elif flytta.lower() == "karta":
            karta()  
        elif flytta.lower() == "exit":
            avslutaSpel()
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")

# Display på karta för om rummet är hittat
a1Hittad = """@@@@@@@@@@@@@@@@@@@@@@@@@@
@@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@
@@|                     ¯¯
@@|                       
@@|                     __
@@|_____________________|@
@@@@@@@@@@@@@@@@@@@@@@@@@@""".split("\n")
# Display på kartan för om rummet INTE är hittat
a1Tom = """                          
                          
                          
                          
                          
                          
                          """.split("\n")
# Display på karta för om rummet är hittat
a2Hittad = """@@@@@@@@@@|    |@@@@@@@@@@
@|¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯¯|@
¯¯                      ¯¯
           [ ]            
__                      __
@|______________________|@
@@@@@@@@@@@@@@@@@@@@@@@@@@""".split("\n")
# Display på karta för om rummet är hittat
a3Hittad = """@@@@@@@@@@|    |@@@@@@@@@
@|¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯|@
¯¯                     |@
           [ ]         |@
__                     |@
@|_____________________|@
@@@@@@@@@@@@@@@@@@@@@@@@@""".split("\n")
# Display på kartan för om rummet INTE är hittat
a3Tom = """                         
                         
                         
                         
                         
                         
                         """.split("\n")
# Display på karta för om rummet är hittat
a4Hittad = """@@@@@@@@@@@@@@@@@@@@@@@@@@
@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@
@|                      ¯¯
@|         [ ]            
@|                      __
@|______________________|@
@@@@@@@@@@@@@@@@@@@@@@@@@@""".split("\n")
# Display på kartan för om rummet INTE är hittat
a4Tom = """                          
                          
                          
                          
                          
                          
                          """.split("\n")
# Display på karta för om rummet är hittat
a5Hittad = """@@@@@@@@@@|    |@@@@@@@@@@
@|¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯|@@
¯¯                     |@@
           [ ]         |@@
__                     |@@
@|_____________________|@@
@@@@@@@@@@@@@@@@@@@@@@@@@@""".split("\n")
# Display på kartan för om rummet INTE är hittat
a5Tom = """                          
                          
                          
                          
                          
                          
                          """.split("\n")
# Display på kartan för om rummet INTE är hittat
b1Tom = """                         
                         
                         
                         
                         
                         """.split("\n")
# Display på karta för om rummet är hittat
b1Hittad = """@@@@@@@@@@@@@@@@@@@@@@@@@
                         
                         
                         
                         
                         """.split("\n")
# Display på karta för om rummet är hittat
b2Hittad = """@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@
@@|                      |@
@@|         [ ]          |@
@@|                      |@
@@|________      ________|@""".split("\n")
# Display på kartan för om rummet INTE är hittat
b2Tom = """                           
                           
                           
                           
                           
                           """.split("\n")
# Display på karta för om rummet är hittat
b3b4Hittad = """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|    |@@@@@@@@@@
@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯¯|@
@|                                               |@
@|                     [ ]                       |@
@|                                               |@
@|________      _________________________________|@""".split("\n")
# Display på kartan för om rummet INTE är hittat
b3b4Tom = """                                                   
                                                   
                                                   
                                                   
                                                   
                                                   """.split("\n")
# Display på karta för om rummet är hittat
bcd5HittadTop = """@@@@@@@@@@@@@@@@@@@@@@@@@@
@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@@
@|                     |@@
@|                     |@@
@|                     |@@""".split("\n")
# Display på karta för om rummet är hittat
bcd5HittadMit = """@|                     |@@
@|                     |@@
¯¯                     |@@
           [ ]         |@@
__                     |@@
@|                     |@@""".split("\n")
# Display på karta för om rummet är hittat
bcd5HittadBotten = """@|                     |@@
@|                     |@@
@|                     |@@
@|                     |@@
@|                     |@@
@|________      _______|@@
@@@@@@@@@@|    |@@@@@@@@@@""".split("\n")
# Display på kartan för om rummet INTE är hittat
bcd5TomTop = """                          
                          
                          
                          
                          """.split("\n")
# Display på kartan för om rummet INTE är hittat
bcd5TomMit = """                          
                          
                          
                          
                          
                          """
# Display på kartan för om rummet INTE är hittat
bcd5TomBotten = """                          
                          
                          
                          
                          
                          
                          """.split("\n")
# Display på karta för om rummet är hittat
cd3cd4HittadBotten = """@|                                               |@
@|                     [ ]                       |@
¯¯                                               ¯¯
                                                   
__                                               __
@|_________________________________      ________|@""".split("\n")
# Display på karta för om rummet är hittat
cd3cd4HittadTop = """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@
@|                                               |@
@|                                               |@
@|                                               |@""".split("\n")
# Display på kartan för om rummet INTE är hittat
cd3cd4TomBotten = """                                                   
                                                   
                                                   
                                                   
                                                   """.split("\n")
# Display på kartan för om rummet INTE är hittat
cd3cd4TomTop = """                                                   
                                                   
                                                   
                                                   
                                                   
                                                   """.split("\n")
# Display på karta för om rummet är hittat
cd1HittadBotten = """@@|                     |@
@@|         [ ]         |@
@@|                     ¯¯
@@|                       
@@|                     __
@@|_____________________|@""".split("\n")
# Display på karta för om rummet är hittat
cd1HittadTop = """@@@@@@@@@@@@@@@@@@@@@@@@@@
@@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@
@@|                     |@
@@|                     |@
@@|                     |@""".split("\n")
# Display på kartan för om rummet INTE är hittat
cd1TomBotten = """                          
                          
                          
                          
                          
                          
                          """.split("\n")
# Display på kartan för om rummet INTE är hittat
cd1TomTop = """                          
                          
                          
                          
                          """.split("\n")
# Display på karta för om rummet är hittat
c2Hittad = """@@@@@@@@@@|    |@@@@@@@@@@
@|¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯¯|@
¯¯                      ¯¯
           [ ]            
__                      __
@|______________________|@""".split("\n")
# Display på kartan för om rummet INTE är hittat
c2Tom = """                          
                          
                          
                          
                          
                          """.split("\n")
# Display på karta för om rummet är hittat
d2Hittad = """@@@@@@@@@@@@@@@@@@@@@@@@@@
@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@
@|                      |@
@|         [ ]          |@
@|________      ________|@""".split("\n")
# Display på kartan för om rummet INTE är hittat
d2Tom = """                          
                          
                          
                          
                          """.split("\n")

def kartaFull():
    print(f"""
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@@
    @@|                     |@@|                      |@@|                                               |@@|                     |@@
    @@|                     |@@|         [ ]          |@@|                                               |@@|                     |@@
    @@|                     |@@|________      ________|@@|                                               |@@|                     |@@
    @@|                     |@@@@@@@@@@@|    |@@@@@@@@@@@|                                               |@@|                     |@@
    @@|         [ ]         |@@|¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯¯|@@|                     [ ]                       |@@|                     |@@
    @@|                     ¯¯¯¯                      ¯¯¯¯                                               ¯¯¯¯                     |@@
    @@|                                  [ ]                                                                          [ ]         |@@
    @@|                     ____                      ____                                               ____                     |@@
    @@|_____________________|@@|______________________|@@|_________________________________      ________|@@|                     |@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|    |@@@@@@@@@@@|                     |@@
                             @@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯¯|@@|                     |@@
                             @@|                      |@@|                                               |@@|                     |@@
                             @@|         [ ]          |@@|                     [ ]                       |@@|                     |@@
                             @@|                      |@@|                                               |@@|                     |@@
                             @@|________      ________|@@|________      _________________________________|@@|________      _______|@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|    |@@@@@@@@@@@@@@@@@@@@|    |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|    |@@@@@@@@@@
    @@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@@|¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯¯|@@|¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯|@@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@@|¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯|@@
    @@|                     ¯¯¯¯                      ¯¯¯¯                     |@@|                      ¯¯¯¯                     |@@
    @@|                                  [ ]                       [ ]         |@@|         [ ]                       [ ]         |@@
    @@|                     ____                      ____                     |@@|                      ____                     |@@
    @@|_____________________|@@|______________________|@@|_____________________|@@|______________________|@@|_____________________|@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")


# funktion för att visa kartan
def karta():
    # varaibler för rummen
    global a1E
    global a3E
    global a4E
    global a5E 
    global a1V
    global a3V
    global a4V
    global a5V 

    # om man har varit inne i a1 -
    if a1E != 0:
        # så blir variabeln a1v en display av rum a1
        a1V = a1Hittad
    else:
        # om inte så visas rum a1 inte
        a1V = a1Tom
    if a3E != 0:
        a3V = a3Hittad
    else:
        a3V = a3Tom
    if a4E != 0:
        a4V = a4Hittad
    else:
        a4V = a4Tom
    if a5E != 0:
        a5V = a5Hittad
    else:
        a5V = a5Tom



    global b2E
    global b3b4E
    global bcd5E
    global b2V
    global b3b4V
    global bcd5V
    global bcd5V2

    if b2E != 0:
        b2V = b2Hittad
    else:
        b2V = b2Tom

    if b3b4E != 0:
        b3b4V = b3b4Hittad
    else:
        b3b4V = b3b4Tom

    if bcd5E != 0:
        bcd5V = bcd5HittadBotten
    else:
        bcd5V = bcd5TomBotten

    global cd1E
    global c2E
    global cd3cd4E
    global cdV1
    global cdV2
    global c2V
    global cd3cd4V
    global bcd5V3

    if cd1E != 0:
        cd1V = cd1HittadBotten
        cdV2 = cd1HittadTop
        b1V = b1Hittad
    else:
        cd1V = cd1TomBotten
        cdV2 = cd1TomTop
        b1V = b1Tom
    if c2E != 0:
        c2V = c2Hittad
    else:
        c2V = c2Tom
    if cd3cd4E != 0:
        cd3cd4V = cd3cd4HittadBotten
        cd3cd4V2 = cd3cd4HittadTop
    else:
        cd3cd4V = cd3cd4TomBotten
        cd3cd4V2 = cd3cd4TomTop
    if bcd5E != 0:
        bcd5V = bcd5HittadBotten
        bcd5V2 = bcd5HittadMit
        bcd5V3 = bcd5HittadTop
    else:
        bcd5V = bcd5TomBotten
        bcd5V2 = bcd5TomMit
        bcd5V3 = bcd5TomTop

    global d2E
    global d2V

    if d2E != 0:
        d2V = d2Hittad
    else:
        d2V = d2Tom

    # cred till någon snubbe i ett forum som jag inte vet vart det är någonstans...
    for row in zip(cdV2, d2V, cd3cd4V2, bcd5V3):
        print(row[0] + "" + row[1] + "" + row[2] + "" + row[3])

    for row in zip(cd1V, c2V, cd3cd4V, bcd5V2):
        print(row[0] + "" + row[1] + "" + row[2] + "" + row[3])

    for row in zip(b1V, b2V, b3b4V, bcd5V):
        print(row[0] + "" + row[1] + "" + row[2] + "" + row[3])

    for row in zip(a1V, a2Hittad, a3V, a4V, a5V):
        print(row[0] + "" + row[1] + "" + row[2] + "" + row[3] + "" + row[4])

#####################
### Combat system ###
#####################
        
# player stats
hp = 100
stamina = 100






a2()