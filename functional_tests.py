"""File: functional_tests_py
https://www.obeythetestinggoat.com/book/chapter_01.html
https://www.guru99.com/selenium-python.html
""" 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Goat example continued
# browser = driver.Firefox(desired_capabilities=capabilities)
browser = webdriver.Firefox(firefox_binary='/home/morten/firefox/firefox')
#browser = webdriver.Firefox(firefox_binary='/home/morten/firefox/firefox-bin')
browser.get('http://127.0.0.1:8000')

assert 'Django' in browser.title