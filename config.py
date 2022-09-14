from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver import ActionChains

from selenium import webdriver


vk_driver = webdriver.Chrome('chromedriver.exe')
vk_target_driver = webdriver.Chrome('chromedriver.exe')

vk_target_driver2 = webdriver.Chrome('chromedriver.exe')
vk_driver2 = webdriver.Chrome('chromedriver.exe')

actionChains = ActionChains(vk_target_driver)
actionChains2 = ActionChains(vk_target_driver2)
