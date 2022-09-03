
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from _csv import reader
import urllib.parse

driver = None
Link = "https://web.whatsapp.com/"
wait = None


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


whatsapp_login()
phone = ["923167629731","923027274944"]
msg = "HEy"
for list in phone:
    params = {'phone': str(list), 'text': str(msg)}
    end = urllib.parse.urlencode(params)
    final_url = Link + 'send?' + end
    list1 = final_url
    print(list1)
    driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.COMMAND + 't')
    driver.get(str(list1))
    WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, '//div[@title = "Menu"]')))
    sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
    sleep(3)
    driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.COMMAND + 'w')
    # driver.refresh()
    sleep(5)
    print("Message sent successfully.")
#
location = input("Enter the CSV file path : ")

# _____________________________________________________________________
# ******************TYPE THE ANY MESSAGE HERE**************************
# msg = "Here write that msg that you want to send tha client or any other"
#
# try:
#
#     with open(location, 'r') as csv_file:
#         csv_reader = reader(csv_file)
#     whatsapp_login()
#
#     while True:
#         try:
#             print("Start Message sending")
#
#             list = []
#             for row in csv_reader:
#                 list = row
#                 for list in list:
#                     sleep(1)
#
#
#         except:
#             print("something wrong")
#
#
# except:
#     print("check webpage ")
