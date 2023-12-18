import random

# Vilket rum man befinner sig i
position = "a2"
a1E = 0
a2E = 0
a3E = 0
a4E = 0
a5E = 0
b2E = 0
b3b4E = 0
bcd5E = 0
cd1E = 0
c2E = 0
cd3cd4E = 0
d2E = 0

a1V = 0
a3V = 0
a4V = 0
a5V = 0
b2V = 0
b3b4V = 0
bcd5V = 0
bcd5V2 = 0
bcd5V3 = 0

cd1V = 0
c2V = 0
cd3cd4V = 0



# funktion för rum a1
def a1():
    global position
    global a1E
    if a1E == 0:
        a1E = 1
    print(a1E, a2E, a3E, a4E)
    print(f"Nu är du i {position}")
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
            aRowKarta()
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum a2
def a2():
    global position
    print(f"Nu är du i {position}")
    print(a1E, a2E, a3E, a4E)
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
            aRowKarta()
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum a3
def a3():
    global position
    global a3E
    if a3E == 0:
        a3E = 1
    print(f"Nu är du i {position}")
    print(a1E, a2E, a3E, a4E)
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
            aRowKarta()            
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum a4
def a4():
    global position
    global a4E
    if a4E == 0:
        a4E = 1
    print(f"Nu är du i {position}")
    print(a1E, a2E, a3E, a4E)
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
            aRowKarta()
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum a5
def a5():
    global position
    global a5E
    if a5E == 0:
        a5E = 1
    print(f"Nu är du i {position}")
    print(a1E, a2E, a3E, a4E)
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
            aRowKarta()
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum b2
def b2():
    global position
    global b2E
    if b2E == 0:
        b2E = 1
    print(f"Nu är du i {position}")
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
            aRowKarta()   
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum b3b4
def b3b4():
    global position
    global b3b4E
    if b3b4E == 0:
        b3b4E = 1
    print(f"Nu är du i {position}")
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
            position = "a2"
            a2()
        elif flytta.lower() == "karta":
            aRowKarta()   
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum bcd5
def bcd5():
    global position
    global bcd5E
    if bcd5E == 0:
        bcd5E = 1
    print(f"Nu är du i {position}")
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
            aRowKarta()   
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum cd1
def cd1():
    global position
    global cd1E
    if cd1E == 0:
        cd1E = 1
    print(f"Nu är du i {position}")
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
            aRowKarta()  
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum c2
def c2():
    global position
    global c2E
    if c2E == 0:
        c2E = 1
    print(f"Nu är du i {position}")
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
            aRowKarta()  
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum cd3cd4
def cd3cd4():
    global position
    global cd3cd4E
    if cd3cd4E == 0:
        cd3cd4E = 1
    print(f"Nu är du i {position}")
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
            aRowKarta()  
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")
# funktion för rum d2
def d2():
    global position
    global d2E
    if d2E == 0:
        d2E = 1
    print(f"Nu är du i {position}")
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
            aRowKarta()  
        else:
            print("använd w a s d\n'w' för upp\n'a' för vänster\n's' för ner\n'd' för höger")


a1Hittad = """@@@@@@@@@@@@@@@@@@@@@@@@@@
@@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@
@@|                     ¯¯
@@|                       
@@|                     __
@@|_____________________|@
@@@@@@@@@@@@@@@@@@@@@@@@@@""".split("\n")
    
a1Tom = """                          
                          
                          
                          
                          
                          
                          """.split("\n")

a2Hittad = """@@@@@@@@@@|    |@@@@@@@@@@
@|¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯¯|@
¯¯                      ¯¯
           [ ]            
__                      __
@|______________________|@
@@@@@@@@@@@@@@@@@@@@@@@@@@""".split("\n")

a3Hittad = """@@@@@@@@@@|    |@@@@@@@@@
@|¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯|@
¯¯                     |@
           [ ]         |@
__                     |@
@|_____________________|@
@@@@@@@@@@@@@@@@@@@@@@@@@""".split("\n")
    
a3Tom = """                         
                         
                         
                         
                         
                         
                         """.split("\n")

a4Hittad = """@@@@@@@@@@@@@@@@@@@@@@@@@@
@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@
@|                      ¯¯
@|         [ ]            
@|                      __
@|______________________|@
@@@@@@@@@@@@@@@@@@@@@@@@@@""".split("\n")

a4Tom = """                          
                          
                          
                          
                          
                          
                          """.split("\n")

a5Hittad = """@@@@@@@@@@|    |@@@@@@@@@@
@|¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯|@@
¯¯                     |@@
           [ ]         |@@
__                     |@@
@|_____________________|@@
@@@@@@@@@@@@@@@@@@@@@@@@@@""".split("\n")

a5Tom = """                          
                          
                          
                          
                          
                          
                          """.split("\n")

b1Tom = """                         
                         
                         
                         
                         
                         """.split("\n")

b1Hittad = """@@@@@@@@@@@@@@@@@@@@@@@@@
                         
                         
                         
                         
                         """

b2Hittad = """@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@
@@|                      |@
@@|         [ ]          |@
@@|                      |@
@@|________      ________|@""".split("\n")

b2Tom = """                           
                           
                           
                           
                           
                           """.split("\n")

b3b4Hittad = """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|    |@@@@@@@@@@
@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯¯|@
@|                                               |@
@|                     [ ]                       |@
@|                                               |@
@|________      _________________________________|@""".split("\n")

b3b4Tom = """                                                   
                                                   
                                                   
                                                   
                                                   
                                                   """.split("\n")

bcd5HittadTop = """@@@@@@@@@@@@@@@@@@@@@@@@@@
@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@@
@|                     |@@
@|                     |@@
@|                     |@@""".split("\n")

bcd5HittadMit = """@|                     |@@
@|                     |@@
¯¯                     |@@
           [ ]         |@@
__                     |@@
@|                     |@@""".split("\n")

bcd5HittadBotten = """@|                     |@@
@|                     |@@
@|                     |@@
@|                     |@@
@|                     |@@
@|________      _______|@@
@@@@@@@@@@|    |@@@@@@@@@@""".split("\n")

bcd5TomTop = """                          
                          
                          
                          
                          """.split("\n")

bcd5TomMit = """                          
                          
                          
                          
                          
                          """

bcd5TomBotten = """                          
                          
                          
                          
                          
                          
                          """.split("\n")


cd3cd4HittadBotten = """@|                                               |@
@|                     [ ]                       |@
¯¯                                               ¯¯
                                                   
__                                               __
@|_________________________________      ________|@""".split("\n")

cd3cd4HittadTop = """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@
@|                                               |@
@|                                               |@
@|                                               |@""".split("\n")

cd3cd4TomBotten = """                                                   
                                                   
                                                   
                                                   
                                                   """.split("\n")

cd3cd4TomTop = """                                                   
                                                   
                                                   
                                                   
                                                   
                                                   """.split("\n")

cd1HittadBotten = """@@|                     |@
@@|         [ ]         |@
@@|                     ¯¯
@@|                       
@@|                     __
@@|_____________________|@""".split("\n")

cd1HittadTop = """@@@@@@@@@@@@@@@@@@@@@@@@@@
@@|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|@
@@|                     |@
@@|                     |@
@@|                     |@""".split("\n")

cd1TomBotten = """                          
                          
                          
                          
                          
                          
                          """.split("\n")

cd1TomTop = """                          
                          
                          
                          
                          """.split("\n")

c2Hittad = """@@@@@@@@@@|    |@@@@@@@@@@
@|¯¯¯¯¯¯¯¯      ¯¯¯¯¯¯¯¯|@
¯¯                      ¯¯
           [ ]            
__                      __
@|______________________|@""".split("\n")

c2Tom = """                          
                          
                          
                          
                          
                          """.split("\n")

def karta():
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


def aRowKarta():
    global a1E
    global a3E
    global a4E
    global a5E 
    global a1V
    global a3V
    global a4V
    global a5V 

    if a1E != 0:
        a1V = a1Hittad
    else:
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
    global bcd5v2

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
    global cd1V
    global c2V
    global cd3cd4V
    global bcd5V3

    if cd1E != 0:
        cd1V = cd1HittadBotten
        b1V = b1Hittad
    else:
        cd1V = cd1TomBotten
        b1V = b1Tom
    if c2E != 0:
        c2V = c2Hittad
    else:
        c2V = c2Tom
    if cd3cd4E != 0:
        cd3cd4V = cd3cd4HittadBotten
    else:
        cd3cd4V = cd3cd4TomBotten
    if bcd5E != 0:
        bcd5V = bcd5HittadBotten
        bcd5V2 = bcd5HittadMit
        bcd5V3 = bcd5HittadTop
    else:
        bcd5V = bcd5TomBotten
        bcd5V2 = bcd5TomMit
        bcd5V3 = bcd5TomTop

    for row in zip(cd1V, c2V, cd3cd4V, bcd5V2):
        print(row[0] + "" + row[1] + "" + row[2] + "" + row[3])

    for row in zip(b1V, b2V, b3b4V, bcd5V):
        print(row[0] + "" + row[1] + "" + row[2] + "" + row[3])

    for row in zip(a1V, a2Hittad, a3V, a4V, a5V):
        print(row[0] + "" + row[1] + "" + row[2] + "" + row[3] + "" + row[4])
    




a2()

# for row in zip(a1Hittad, a2Hittad):
#     print(row[0] + "" + row[1])

# a1Tom()
# a2()