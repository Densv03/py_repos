from selenium import webdriver
from time import sleep
import pyautogui as pg
from threading import Thread

phoneNumber = "687962598"
#number = str(number)
countryCode = "+380"
#countryCode = str(countryCode)
fullnumber = str(countryCode) + str(phoneNumber)
def facebook(fullNumber):
    for i in range(2):
        browser = webdriver.Chrome("chromedriver.exe")
        browser.get("https://www.facebook.com/login/identify/?str=recover")
        number = browser.find_element_by_xpath('//*[@id="identify_email"]')
        did_submit = browser.find_element_by_name('did_submit')
        number.send_keys(fullNumber)
        did_submit.click()
        sleep(3)
        submit = browser.find_element_by_xpath('//*[@id="initiate_interstitial"]/div[3]/div/div[1]/button')
        submit.click()
        sleep(5)
def sweet_tv (num):
    for i in range(2):
        browser = webdriver.Chrome("chromedriver.exe")
        browser.get("https://sweet.tv/ru")
        sleep(1)
        logIn = browser.find_element_by_xpath('//*[@id="tabs"]/div/div/div[2]/div/div[3]')
        logIn.click()
        sleep(1)
        input = browser.find_element_by_xpath('//*[@id="m--login"]/div/div/div[2]/div[1]/div[1]/form/div[1]/input')
        input.click()
        input.send_keys(str(num))
        sleep(1)
        sendSMS = browser.find_element_by_xpath('//*[@id="m--login"]/div/div/div[2]/div[1]/div[1]/form/button')
        sendSMS.click()
        sleep(1)
        againSend = browser.find_element_by_xpath('//*[@id="inputSMS"]/div[2]/button')
        againSend.click()

th1=Thread(target=sweet_tv(phoneNumber))
th1.start()

th1.join()
facebook(fullnumber)
print('Stopped')