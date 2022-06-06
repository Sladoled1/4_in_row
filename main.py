import sys
import math
import numpy as np
import pygame
import fu

#ргб кольри
black=(0,0,0)
red=(253,70,89)
green=(100, 166, 74)
blue=(0,0,255)
# змінні які використ для ств масиву
stovp = 7
radky = 6

pole = fu.create_pole()
game_over = False
hid=0
# зміння масштабування
pygame.init()
kvadrat=100
radius = int(kvadrat/2 -5) #радіус намальованих кіл
width = stovp * kvadrat  # ширина поля
height = (radky+1) * kvadrat# висота поля
size = (width,height)# розмір поля
screen = pygame.display.set_mode(size)

fu.draw_pypole(pole)# виклик малювання посаткового поля
pygame.display.update()#оновлення поля форми
myfont = pygame.font.SysFont("monospace",55)#шрифт

def anymat(pole,row,hid):# функція, яка створює анімацію падіння
    d=0
    k = 5
    z = row - 1
    if(hid ==0):
        d=1
    if(hid ==1):
        d=2
    while k != z:
            pole[k][col] = d
            fu.draw_pypole(pole)
            pygame.time.wait(100)
            pole[k][col] = 0
            fu.draw_pypole(pole)
            k = k - 1

while not game_over:
    for event in pygame.event.get():
        # подія яка дозволяє вийти з гри натисканням на хрестик
        if event.type ==pygame.QUIT:
            sys.exit()
        # подія руху мишки
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,black,(0,0,width,kvadrat))
            posx=event.pos[0]
            pos2=posx//100
            if hid == 0:
                pygame.draw.circle(screen,red,(pos2*int(kvadrat)+50, int(kvadrat/2)),radius)
            else:
                pygame.draw.circle(screen, green, (pos2*int(kvadrat)+50, int(kvadrat / 2)), radius)
        pygame.display.update()

        # подія натискання клавіші мишки
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black, (0, 0, width, kvadrat))
            # Хід 1 гравця
            if hid==0:
                # Визначення за допомогою позиції миші вибір стовбця для ходу
                posx = event.pos[0]
                col= int(math.floor(posx/kvadrat))
                # Перевірка чи можливий хід
                if pole[radky - 1][col] != 0:
                    hid += 1  # зміна ходу
                    hid = hid % 2
                else:
                    # Визначення в яку точку попаде хід, анімація падіння та запис ходу у масив
                    row = fu.Kudu_Monaradok(pole, col)
                    anymat(pole,row,hid)
                    fu.drop_down(pole,row,col,1)
                    #Перевірки на виграш та нічию
                    if fu.win(pole,1):
                        label= myfont.render("Гравець 1 переміг",1,red)
                        screen.blit(label,(40,10))
                        game_over = True
                    if fu.nichiya(pole):
                        label = myfont.render("Нічия", 1, blue)
                        screen.blit(label, (40, 10))
                        game_over = True
            # Хід 2 гравця
            else:
                # Визначення за допомогою позиції миші вибір стовбця для ходу
                posx = event.pos[0]
                col = int(math.floor(posx / kvadrat))
                # Перевірка чи можливий хід
                if pole[radky-1][col] != 0:
                    hid += 1  # зміна ходу
                    hid = hid % 2
                else:
                    # Визначення в яку точку попаде хід, анімація падіння та запис ходу у масив
                        row = fu.Kudu_Monaradok(pole, col)
                        anymat(pole,row,hid)
                        fu.drop_down(pole, row, col, 2)
                    # Перевірки на виграш та нічию
                        if fu.win(pole,2):
                            label = myfont.render("Гравець 2 переміг", 1, green)
                            screen.blit(label, (40, 10))
                            game_over = True
                        if fu.nichiya(pole):
                            label = myfont.render("Нічия", 1, blue)
                            screen.blit(label, (40, 10))
                            game_over = True
            # Після кожного ходу міняємо гравця, який ходить, оновлюємо масив та перемальовуємо поле гри
            fu.print_pole(pole)
            fu.draw_pypole(pole)
            hid+= 1     #зміна ходу
            hid = hid%2

            if game_over == True:
                pygame.time.wait(4000)