import urllib.request

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def image_downloader(keyword):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)

    driver.maximize_window()
    driver.get('https://www.google.co.kr/imghp?hl=ko&ogbl')
    time.sleep(2)

    search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search.click()
    search.send_keys(keyword)
    search.send_keys(Keys.ENTER)
    time.sleep(2.3)

    i = 0
    while i < 40:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        i += 1

    try:
        the_bo_gi = driver.find_element(By.CSS_SELECTOR, '#islmp > div > div > div > div > div.gBPM8 > div.qvfT1 > div.YstHxe > input')
        the_bo_gi.click()

    except:
        continue

        i = 0
        while i < 30:
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
            i += 1

    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    images = soup.find_all('div', class_='bRMDJf islir')
    k = 1
    for img in images:
        img_url = img.find('img').get('src')
        try:
            urllib.request.urlretrieve(img_url, 'C:/images/' + keyword + '/' + str(k) + '.jpg')
            k += 1
            time.sleep(0.5)
        except:
            continue

        if k == 1000:
            print('end')
            break


keywords = ['leg curl machine',
            'leg extension machine',
            'bench press bench',
            'lat pull down machine',
            'seated row machine',
            'shoulder press machine',
            'leg press machine',
            'chest press machine',
            'rowing machine',
            'stepmill']

for keyword in keywords:
    image_downloader(keyword)
