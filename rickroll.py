from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

browser=webdriver.Firefox()
browser.get("https://www.youtube.com")
element=browser.find_element('xpath','/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')

element.send_keys("rick roll without ads")
time.sleep(3)
element.send_keys(Keys.RETURN)
time.sleep(3)
link = browser.find_element('xpath','/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div')
link.click()
time.sleep(10)
browser.close()