import random
import time
import sys


def skriv_långsamt(text, fördröjning=0.1):
    for tecken in text:
        print(tecken, end='', flush=True)
        time.sleep(fördröjning)


def garmit():
    skriv_långsamt("ser ut som du har träffat den första boss!, garmit!")
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠹⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⢰⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⢆⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⢀⡏⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠸⡆⠀⠀⠢⡄⠘⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠃⠀⠀⣿⠀⡸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠀⢳⠀⠀⠀⠘⢦⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠁⠀⠀⣸⠃⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠈⢷⡀⠹⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⠟⠀⠀⢀⣼⡟⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠹⣄⠈⢧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⢠⠞⢹⠃⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠘⣦⠈⢳⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⡟⠀⠀⠀⣰⠏⢠⡏⠐⠁⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠈⢣⡀⢱⡀⠀⠀⠀
⠀⠀⠀⡴⠃⠀⠀⢀⡼⠃⠀⣼⠁⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠈⣧⠀⢿⡀⠀⠀
⠀⢀⡾⠁⠀⠀⢠⡞⠁⢀⣠⡇⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠈⢧⠈⢧⠀⠀
⢠⡟⠀⠀⠀⣠⠋⢀⡴⠛⢹⠀⠀⢀⣴⣿⣿⣿⣿⠟⣿⣿⣿⣿⡿⠛⢻⣿⣿⣿⠻⣿⣿⣿⣿⣿⣿⣿⣷⣤⣄⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠈⠆⠸⡇⠀
⡞⢠⠀⠀⢸⣧⣾⠟⠁⢠⠏⠀⣠⠞⢿⣿⣿⣿⣿⠀⠒⠿⣿⣏⡀⠀⠀⠈⣿⣿⠀⠉⠻⣿⣿⣿⣿⣿⡿⠿⢮⣙⡳⢶⣄⡀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀
⣧⣜⣀⣬⠿⠋⠁⠀⢠⡏⠀⣴⠃⠀⣾⣿⣿⣿⡇⠀⠀⠀⠈⢿⣔⣄⠀⢀⡇⣯⠀⠀⠀⠈⠻⣿⣿⣿⡃⠀⠀⠉⢿⣿⣬⡟⠶⣌⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇
⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⣰⠃⠀⡀⠙⡿⣿⣿⣤⣀⣀⠀⠀⠀⠙⢷⣄⢸⣧⠀⢠⣀⣀⣀⣀⣈⣻⣿⣿⣶⣤⠀⣸⢿⡟⠀⠀⠘⣧⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⢹
⠀⠀⠀⠀⠀⠀⠀⠈⠿⣄⠈⠀⠀⠹⣄⠇⠸⣿⡉⠛⣻⣿⣷⣶⡀⠀⠙⢾⣿⠀⠙⠻⡿⣿⣿⣿⣿⣿⡯⠹⣿⣠⡯⠞⠀⠀⠀⠀⢸⡀⠙⣧⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⠀⠀⠘⢮⡀⠙⡇⠀⠸⣭⡿⠟⠀⠀⠀⠀⠹⠀⠀⠀⠙⠳⠿⠛⠛⠁⠀⠀⣿⡾⢀⡄⠀⢀⡴⠂⣠⡇⠀⢈⣷⡄⠀⠀⠀⠀⠀⡾
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣆⠀⠀⢀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣷⠯⠝⢛⣩⡴⠞⠉⠀⣠⠞⠀⠹⣄⣀⣀⡠⠞⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣦⠀⠈⠳⣽⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣾⠟⠁⠀⠀⠉⠁⠀⢀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠙⠛⠿⠿⠶⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣶⠿⠛⠛⠉⠀⠀⠀⠀⠀⠀⢀⣔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⣀⣀⣀⣀⣀⣀⣀⣴⢶⡞⡟⠿⣽⢯⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠉⠀⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢱⠟⡴⠛⠉⠀⣾⣿⡇⡄⠈⠻⢷⣄⠀⠀⠀⢀⣤⡶⠛⠉⠀⠀⠀⣇⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠸⣄⠀⠀⠀⣿⢹⡇⣷⠀⠀⢀⣿⠉⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠈⢣⡄⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢀⠈⠳⠶⢾⠇⠈⠙⣿⠒⠚⠛⠉⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡉⠆⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⢰⣿⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠃⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢈⣿⣀⣀⡶⠛⢦⣄⠀⠀⠀⠐⡇⠀⠀⠀⠀⠀⠀⠀⢀⡾⠃⠀⠀⢾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠂⠐⣿⠉⣉⣽⣇⣀⣠⡿⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⣀⣤⣤⣼⣯⣿⠁⠈⠉⠉⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⢸⡟⢦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣹⣇⠀⣀⣠⠾⠿⠀⠀⠀⠀⠀⠀⣤⡇⠈⠉⠉⢳⡶⢾⠃⠀⠀⠀⠀⠀⠀⠀⣾⠁⢀⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠛⠓⠒⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⢐⣡⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢿⠀⠀⠀⢀⣀⣀⡤⠤⠤⠤⣀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣠⠤⠞⠉⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣯⣾⠗⠒⠋⠉⠉⠀⠀⠀⣀⣀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠶⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠤⠤⠤⠤⠤⠖⠒⠒⠚⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
    






