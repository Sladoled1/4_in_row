import sys
import math
import numpy as np
import pygame

#ргб кольри
black=(0,0,0)
blue=(0,0,255)
red=(253,70,89)
green=(100, 166, 74)
# змінні які використ для ств масиву
stovp = 7
radky = 6


def create_pole(): #функція, яка створює масив
    pole = np.zeros((radky,stovp))#масив значення всіх елементів =0 ,розміром (6,7)-стовбці та рядки
    return pole

def drop_down(pole,row,col,piece):#функція, яка записує в масив хід гравця
    pole[row][col]=piece

def Kudu_Monaradok(pole, Kol):#функція, яка перевіряє куди буде здійснено поточний хід
    for r in range(radky):
        if pole[r][Kol] == 0:
            return r


def print_pole(pole): #фкуія яка перевертає масив
    # фкція бібліотеки numpy , вона перевертає масив (з ніг на голову) необхідна для правидьного заповнення масиву ходами
    np.flip(pole,0)

def nichiya(pole): #функція яка перевіряє нічию
    l=0
    for s in range(7):
        for r in range(6):
            if (pole[r][s]==1 or pole[r][s]==2):
                l=l+1
    if(l==42):
        return True

def win(pole,piece):# функція яка перевіряє виграш
    #Горизонтальна перевірка
    for s in range(stovp-3):
        for r in range(radky):
            if pole[r][s]==piece and pole[r][s+1]==piece and pole[r][s+2]==piece and pole[r][s+3]==piece:
                return True
    # Вертикальна перевірка
    for s in range(stovp):
        for r in range(radky-3):
            if pole[r][s] == piece and pole[r+1][s] == piece and pole[r+2][s] == piece and pole[r+3][s] == piece:
                return True
    # Діагональна зрост перевірка
    for s in range(stovp-3):
        for r in range(radky-3):
            if pole[r][s] == piece and pole[r+1][s+1] == piece and pole[r+2][s+2] == piece and pole[r+3][s+3] == piece:
                return True
    # Діагональна спадна перевірка
    for s in range(stovp-3):
        for r in range(3,radky):
            if pole[r][s] == piece and pole[r-1][s+1] == piece and pole[r-2][s+2] == piece and pole[r-3][s+3] == piece:
                return True


def draw_pypole(pole):#функція, яка малює поле гри відповідно до значень в масиві
    # цикл який малює звичайне поле
    for s in range(stovp):
        for r in range(radky):
            pygame.draw.rect(screen, blue, (s * kvadrat, r * kvadrat + kvadrat, kvadrat, kvadrat))
            pygame.draw.circle(screen,black,(int(s*kvadrat + kvadrat/2) , int(r * kvadrat + kvadrat + kvadrat/2)),radius)
    # цикл який відповіно до значень в масиві відображає ходи на полі
    for s in range(stovp):
        for r in range(radky):
                if pole[r][s]==1:
                    pygame.draw.circle(screen, red,(int(s * kvadrat + kvadrat / 2), height-int(r * kvadrat + kvadrat / 2)), radius)
                elif pole[r][s]==2:
                    pygame.draw.circle(screen, green,(int(s * kvadrat + kvadrat / 2), height-int(r * kvadrat + kvadrat / 2)), radius)
    pygame.display.update()

pole = create_pole()
# масштабування
kvadrat=100
radius = int(kvadrat/2 -5) #радіус намальованих кіл
width = stovp * kvadrat  # ширина поля
height = (radky+1) * kvadrat# висота поля
size = (width,height)#
screen = pygame.display.set_mode(size)

