from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

with open("message.txt", "r", encoding= "utf-8") as messages:
    message_list = []
    text = messages.read()
    message_list = text.split("\n")

#print(message_list)

def send_message():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get("https://web.whatsapp.com/")
    time.sleep(30)
    input("QR kodu okutup, herhangi bir tuşa basınız!!!")
    message_area = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
    time.sleep(15)
    
    while True:
        flag = False
        message_area.click()
        wp_source = driver.page_source
        soup = bs(wp_source, "lxml")
        search = soup.find_all("div", attrs= {"class" : ["zzgSd", "_3e6xi"]})
        try:
            online = search[0].span.text
            print(online)

            if (online in ["Çevrimiçi", "Online", "Siz"]) and flag== False:
                print("online")
                msg_To_Send = message_list[random.randint(0, len(message_list)-1)]
                message_area.send_keys(msg_To_Send)
                message_area.send_keys(Keys.ENTER)
                flag = True


            elif online not in ["Çevrimiçi", "Online", "Siz"]:
                print("The person is not online")
                flag = False

        except:
            print("The person is not online")
            flag = False

        time.sleep(5)

send_message()