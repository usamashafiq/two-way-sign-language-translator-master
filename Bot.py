import traceback

import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from _csv import reader
import urllib.parse

# input the salary xlsx file path
location_data = input("Enter the xlsx message file path : ")
df = pd.read_excel(location_data)

# input the numbers file path csv
location_number = input("Enter the csv number file path: ")

# sort the data in xlsx file

data = df.values.tolist()
flat_list = []
for sublist in data:
    for item in sublist:
        flat_list.append(item)

new_lst = []
for i in flat_list:
    new_lst.append(i.replace("\n", ""))
print(new_lst)
#
# # initiate some variables
driver = None
Link = "https://web.whatsapp.com/"
wait = None


# function for whatapp web page open in browser
def whatsapp_login():
    global wait, driver, Link
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\HafizUsama\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    # options.add_argument('--profile-directory=Default')
    driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)

    wait = WebDriverWait(driver, 10)
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB IF DISPLAYED")
    driver.get(Link)
    driver.maximize_window()
    print("QR CODE SCANNED")


try:
    whatsapp_login()
    i = 0
    # open cvs file
    number = open(location_number, 'r')

    for phone in number:
        print(i + 1)
        print(phone)
        params = {'phone': str(phone), 'text': str(new_lst[i])}
        end = urllib.parse.urlencode(params)
        final_url = Link + 'send?' + end
        list1 = final_url
        print(list1)
        # open the web page
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.COMMAND + 't')
        # driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.COMMAND + 't')
        driver.get(str(list1))
        WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, '//div[@title = "Menu"]')))
        sleep(5)
        driver.find_element(by=By.XPATH,
                            value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        sleep(2)
        # close the web page
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.COMMAND + 'w')
        # driver.refresh()
        sleep(5)
        print("Message sent successfully.")
        i = i + 1
        # break

except Exception as e:
    print(e)
    traceback.print_exc()
    print("please check your file path or internet connection")
