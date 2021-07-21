import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

# Variables initialization
input_publ = [
   'vtoroe.dyhanye',
    'maldives.trip',
    'blackjacktravel',
    'adat.travel',
    'sheintours',
    'ehala_kz',
    'andorra.group.tours',
    'ski.group.tours',
    'kislorod.trip',
    'tuda_syuda_trip',







]
input_follow = 1
count_of_foll = 1500
counter_sleep = 4
counter_scrolling = 600
counter_processed = 0



browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.instagram.com/accounts/login/')
try:
    login = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
except TimeoutException:
    browser.quit()
    sys.exit()
password = browser.find_element_by_name('password')


login.send_keys('dima_luzanovsky')
password.send_keys("586945MishaMisha")
password.send_keys(Keys.ENTER)


for input_publs in input_publ:
    print(input_publs)

    time.sleep(40)
    browser.get('https://www.instagram.com/' + input_publs)
    time.sleep(4)
    followers_label = browser.find_elements_by_class_name('-nal3')
    followers_label[int(input_follow)].click()
    time.sleep(3)
    try:
        followers_label = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'isgrP'))
        )
    except TimeoutException:
        browser.quit()



    for _ in range(int(count_of_foll/9)):
        browser.execute_script("elem = document.getElementsByClassName('isgrP')[0]; elem.scroll(0,{0})".format(counter_scrolling))
        time.sleep(.7)
        counter_scrolling += 600
    array_nicks = browser.find_elements_by_class_name('d7ByH')
    print(array_nicks)
    file = open('file.txt', 'a')
    for nick in array_nicks:
        file.write(nick.text + '\n')
    file.close()
    time.sleep(20)

browser.quit()