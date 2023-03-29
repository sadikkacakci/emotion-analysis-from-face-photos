import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os.path
from os import path
import random


def humanTypes():
    emotion = int(input(
        "1-Angry\n2-Disgust\n3-Fear\n4-\Happiness\n5-Sadness\n6-Surprise\nChoose:"))
    return emotion


def createFolder(category):
    direction = "images/"
    if path.exists(direction) == False:
        os.mkdir(direction)
        print(direction, "klasör başarıyla oluşturuldu.")
    direction = direction + category
    if path.exists(direction) == False:
        os.mkdir(direction)
        print(direction, "klasör başarıyla oluşturuldu.")
    return direction


def getUrl(sentence):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    # options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com.tr/imghp?hl=tr&authuser=0&ogbl")
    time.sleep(2)
    searchInput = driver.find_element_by_name("q")
    searchInput.send_keys(sentence)
    time.sleep(2)
    searchInput.send_keys(Keys.ENTER)
    url = driver.current_url
    driver.quit()
    return url

def downloadImages(url,category):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    for value in soup.find_all("img"):
        try:
            data = requests.get(value.get("src"), stream=True)
            path = createFolder(category) 
            with open(path + f"/img{random.randrange(0,10000)}.png", "wb") as file:
                for chunk in data.iter_content(chunk_size=4096):
                    file.write(chunk)
        except Exception as err:
            pass