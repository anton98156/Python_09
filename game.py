# Создайте программу для игры в ""Крестики-нолики"".

import os
import emoji
from progress.bar import Bar
import time

os.system("clear")

def loading():
    bar = Bar('Загрузка', max=3)
    for i in range(3):
        time.sleep(1)
        bar.next()
    bar.finish()

loading()

print("Нумерация позиций от 1 до 9 слева направо. Игроку 1 достались крестики, игроку 2 нолики")
print("Для того чтобы сделать ход, нужно просто выбрать позицию элемента.")
print("Убедитесь, что вводите только корректные значения, согласно правилам игры крестики-нолики")

list_1 = ["-","-","-"]
list_2 = ["-","-","-"]
list_3 = ["-","-","-"]
game_stop = False
    
def check_game():
    print(list_1)
    print(list_2)
    print(list_3)
    global game_stop
    if list_1 == ['x', 'x', 'x'] or list_2 == ['x', 'x', 'x'] or list_3 == ['x', 'x', 'x']:
        game_stop = True
        print(emoji.emojize('Игрок 1 выиграл :thumbs_up:'))
    elif list_1[0] == "x" and list_2[0] == "x" and list_3[0] == "x":
        game_stop = True
        print(emoji.emojize('Игрок 1 выиграл :thumbs_up:'))
    elif list_1[1] == "x" and list_2[1] == "x" and list_3[1] == "x":
        game_stop = True
        print(emoji.emojize('Игрок 1 выиграл :thumbs_up:'))
    elif list_1[2] == "x" and list_2[2] == "x" and list_3[2] == "x":
        game_stop = True
        print(emoji.emojize('Игрок 1 выиграл :thumbs_up:'))
    elif list_1[0] == "x" and list_2[1] == "x" and list_3[2] == "x":
        game_stop = True
        print(emoji.emojize('Игрок 1 выиграл :thumbs_up:'))
    elif list_1[2] == "x" and list_2[1] == "x" and list_3[0] == "x":
        game_stop = True
        print(emoji.emojize('Игрок 1 выиграл :thumbs_up:'))
    elif list_1 == ['0', '0', '0'] or list_2 == ['0', '0', '0'] or list_3 == ['0', '0', '0']:
        game_stop = True
        print(emoji.emojize('Игрок 2 выиграл :thumbs_up:'))
    elif list_1[0] == "0" and list_2[0] == "0" and list_3[0] == "0":
        game_stop = True
        print(emoji.emojize('Игрок 2 выиграл :thumbs_up:'))
    elif list_1[1] == "0" and list_2[1] == "0" and list_3[1] == "0":
        game_stop = True
        print(emoji.emojize('Игрок 2 выиграл :thumbs_up:'))
    elif list_1[2] == "0" and list_2[2] == "0" and list_3[2] == "0":
        game_stop = True
        print(emoji.emojize('Игрок 2 выиграл :thumbs_up:'))
    elif list_1[0] == "0" and list_2[1] == "0" and list_3[2] == "0":
        game_stop = True
        print(emoji.emojize('Игрок 2 выиграл :thumbs_up:'))
    elif list_1[2] == "0" and list_2[1] == "0" and list_3[0] == "0":
        game_stop = True
        print(emoji.emojize('Игрок 2 выиграл :thumbs_up:'))

def player_1_move():
    a = int(input("Ход игрока 1: "))
    if a == 1:
        if list_1[0] == "0":
            print("Это поле уже заполнено")
        else:
            list_1[0] = "x"
    elif a == 2:
        if list_1[1] == "0":
            print("Это поле уже заполнено")
        else:
            list_1[1] = "x"
    elif a == 3:
        if list_1[2] == "0":
            print("Это поле уже заполнено")
        else:
            list_1[2] = "x"
    elif a == 4:
        if list_2[0] == "0":
            print("Это поле уже заполнено")
        else:
            list_2[0] = "x"
    elif a == 5:
        if list_2[1] == "0":
            print("Это поле уже заполнено")
        else:
            list_2[1] = "x"
    elif a == 6:
        if list_2[2] == "0":
            print("Это поле уже заполнено")
        else:
            list_2[2] = "x"
    elif a == 7:
        if list_3[0] == "0":
            print("Это поле уже заполнено")
        else:
            list_3[0] = "x"
    elif a == 8:
        if list_3[1] == "0":
            print("Это поле уже заполнено")
        else:
            list_3[1] = "x"
    elif a == 9:
        if list_3[2] == "0":
            print("Это поле уже заполнено")
        else:
            list_3[2] = "x"
    else:
        print("позиции не существует")

def player_2_move():
    a = int(input("Ход игрока 2: "))
    if a == 1:
        if list_1[0] == "x":
            print("Это поле уже заполнено")
        else:
            list_1[0] = "0"
    elif a == 2:
        if list_1[1] == "x":
            print("Это поле уже заполнено")
        else:
            list_1[1] = "0"
    elif a == 3:
        if list_1[2] == "x":
            print("Это поле уже заполнено")
        else:
            list_1[2] = "0"
    elif a == 4:
        if list_2[0] == "x":
            print("Это поле уже заполнено")
        else:
            list_2[0] = "0"
    elif a == 5:
        if list_2[1] == "x":
            print("Это поле уже заполнено")
        else:
            list_2[1] = "0"
    elif a == 6:
        if list_2[2] == "x":
            print("Это поле уже заполнено")
        else:
            list_2[2] = "0"
    elif a == 7:
        if list_3[0] == "x":
            print("Это поле уже заполнено")
        else:
            list_3[0] = "0"
    elif a == 8:
        if list_3[1] == "x":
            print("Это поле уже заполнено")
        else:
            list_3[1] = "0"
    elif a == 9:
        if list_3[2] == "x":
            print("Это поле уже заполнено")
        else:
            list_3[2] = "0"
    else:
        print("позиции не существует")

print(list_1)
print(list_2)
print(list_3)

def start():
    while not game_stop:
        player_1_move()
        check_game()
        if game_stop == True:
            break
        player_2_move()
        check_game()
        if game_stop == True:
            break

start()

