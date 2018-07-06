# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.facebook.com/')
emailElem = browser.find_element_by_css_selector('input#email')
emailElem.send_keys('priya@gmail.com')
passwordElem = browser.find_element_by_css_selector('input#pass')
passwordElem.send_keys('12345')
passwordElem.submit()