import random
import time
import sys


def skriv_långsamt(text, fördröjning=0.1):
    for tecken in text:
        print(tecken, end='', flush=True)
        time.sleep(fördröjning)



def rajgon():
    skriv_långsamt("Ser ut som du har träffat FINAL BOSS!, RAJGOn")
    print(''' 
                                        ⢀⣠⣤⣴⣶⣶⠿⠿⠿⠿⠿⠿⢶⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⢀⣴⣾⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣷⣦⡀⠀⠀⠀
                                ⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⡀⠀
                                ⢠⣿⠋⠀ I AM RAJGON, THE FINAL     ⠙⣿⡄
                                ⣾⡏⠀⠀⠀⠀⠀⠀⠀   BOSS                ⢸⣷
                                ⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿
                                ⠸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠇
                                ⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀
                                ⠀⠀⠀⠙⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠿⠋⠀⠀⠀
                                ⠀⠀⠀⢰⣿⠀⠀⠀⠀⠀⢀⣶⣦⣤⣤⣤⣤⣴⣶⣶⠿⠿⠛⠉⠀⠀⠀⠀⠀⠀
                                ⠀⠀⣠⣿⠃⠀⢀⣠⣤⣾⠟⠋⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⢿⣷⡾⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                      ____...                                  
             .-"--"""".__    `.                                
            |            `    |                                                                                          
  (         `._....------.._.:          
   )         .()''        ``().                                
  '          () .=='  `===  `-.         
   . )       (         g)                                
    )         )     /        J          
   (          |.   /      . (                                  
   $$         (.  (_'.   , )|`                                 
   ||         |\`-....--'/  ' \                                
  /||.         \\ | | | /  /   \.                                                      
 //||(\         \`-===-'  '     \o.                            
.//7' |)         `. --   / (     OObaaaad888b.                 
(<<. / |     .a888b`.__.'d\     OO888888888888a.               
 \  Y' |    .8888888aaaa88POOOOOO888888888888888.              
  \  \ |   .888888888888888888888888888888888888b              
   |   |  .d88888P88888888888888888888888b8888888.             
   b.--d .d88888P8888888888888888a:f888888|888888b             
   88888b 888888|8888888888888888888888888\8888888
''')