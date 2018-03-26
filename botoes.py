# coding: utf-8
from gpiozero import Button
import ap310
import time

if __name__ == "__main__":
    token = ap310.login()
    vermelho = Button(2)
    verde = Button(3)
    while True:
        if vermelho.is_pressed and verde.is_pressed:
            print('Ambos')
            r = ap310.changeLed(token, "yellow", "blink")
            ap310.apply(token)
            time.sleep(5)
        elif vermelho.is_pressed:
            print('Vermelho')
            r = ap310.changeLed(token, "red", "pulse")
            ap310.apply(token)
            time.sleep(3)
        elif verde.is_pressed:
            print('Verde')
            r = ap310.changeLed(token, "green", "on")
            ap310.apply(token)
