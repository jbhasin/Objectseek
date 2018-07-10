from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Python37\TestProj1\ProjectPython1\driver\chromedriver.exe")
driver.set_page_load_timeout("40")

driver.get("http://www.haldiram.com/")
driver.find_element_by_xpath("//a[@class='hed-ordr-onln']").click()
driver.find_element_by_xpath("//span[@class='login-text']").click()
driver.find_element_by_id("[@id='email']").click()


#driver.find_element_by_css_selector("input#email").click()


#driver.find_element_by_xpath("//input[@id='email' and @title='Email Address']").click()

#driver.find_element_by_xpath("//input[@id='email' and @title='Email Address']").send_keys("jt9@gmail.com")
#driver.find_element_by_css_selector("input#pass").send_keys("jt9@gmail.com")
#driver.find_element_by_xpath("//input[@id='email']").send_keys(Keys.RETURN)
#driver.find_element_by_css_selector("form#ajaxkit-login-form-validate button").send_keys(Keys.RETURN)
