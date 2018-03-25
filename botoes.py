# coding: utf-8
from gpiozero import Button
vermelho = Button(2)
verde = Button(3)
while True:
    if vermelho.is_pressed and verde.is_pressed:
        print('Amarelo!')
    elif vermelho.is_pressed:
        print('Vermelho!')
    elif verde.is_pressed:
        print('Verde!')
