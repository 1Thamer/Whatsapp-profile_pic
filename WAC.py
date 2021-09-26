from time import sleep
from typing import ByteString
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random, os
import sys
import time


options = Options()
options.binary_location = "C:\\Users\\xopkv\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\Users\xopkv\Downloads\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

for x in range(7):    
 path = r"C:\Users\xopkv\Pictures\Saved Pictures"
 random_filename = random.choice([
     x for x in os.listdir(path)
     if os.path.isfile(os.path.join(path, x))
 ])
 
 sleep(3)
 #filepath = input('Enter your filepath (images/video): ')
 omg = r"C:\Users\xopkv\Pictures\Saved Pictures\image 1.jpg"
 filepath = (omg)
 
 #sleep(5)
 #input('Enter anything after scanning QR code to continue...')
 sleep(2)
 user = driver.find_element_by_xpath('//img[@class="_8hzr9 M0JmA i0jNr"]')
 user.click()

 sleep(2)
 attachment_box = driver.find_element_by_xpath('//div[@class="_3yg5l"]')
 attachment_box.click()

 sleep(2)
 attachment_box = driver.find_element_by_xpath('//div[@aria-label = "Upload photo"]')
 attachment_box.click()

 sleep(3)
 image_box = driver.find_element_by_xpath('//input[@accept="image/gif,image/jpeg,image/jpg,image/png"]')
 image_box.send_keys(filepath)

 sleep(3)
 send_button = driver.find_element_by_xpath('//span[@data-icon="checkmark-large"]')
 send_button.click()

 sleep(2)
 back_button = driver.find_element_by_xpath('//span[@data-icon="back"]')
 back_button.click() 
 sleep(2)

#-----------------------------------------------------------------------------------------------------------------

 omg2 = r"C:\Users\xopkv\Pictures\Saved Pictures\image 2.jpeg"
 filepath2 = (omg2)
 #sleep(5)
 #input('Enter anything after scanning QR code to continue...')
 sleep(3)
 user = driver.find_element_by_xpath('//img[@class="_8hzr9 M0JmA i0jNr"]')
 user.click()

 sleep(3)
 attachment_box = driver.find_element_by_xpath('//div[@class="_3yg5l"]')
 attachment_box.click()

 sleep(3)
 attachment_box = driver.find_element_by_xpath('//div[@aria-label = "Upload photo"]')
 attachment_box.click()
 
 sleep(3)
 image_box = driver.find_element_by_xpath('//input[@accept="image/gif,image/jpeg,image/jpg,image/png"]')
 image_box.send_keys(filepath2)

 sleep(3)
 send_button = driver.find_element_by_xpath('//span[@data-icon="checkmark-large"]')
 send_button.click()

 sleep(3)
 back_button = driver.find_element_by_xpath('//span[@data-icon="back"]')
 back_button.click() 
 sleep(2)
