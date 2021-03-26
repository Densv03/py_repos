import pyautogui as pg
from time import sleep
print(pg.position())
print('Введите номер телефона: ',sep='')
number=input()
number1=number+' 60'
timer=60
while True:
    pg.moveTo(700,543,0.5)
    pg.click()
    pg.moveTo(946,641,0.5)
    pg.click()
    pg.moveTo(723,601,0.5)
    pg.click()
    pg.typewrite(number)
    pg.press('enter')
    sleep(1)
    pg.moveTo(731,647,0.5)
    pg.click()
    pg.moveTo(723,601,0.5)
    pg.click()
    pg.typewrite(number1)
    pg.press('enter')
    sleep(timer)