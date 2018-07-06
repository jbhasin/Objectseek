from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Python37\TestProj1\ProjectPython1\driver\chromedriver.exe")
driver.set_page_load_timeout("10")

driver.get("http://www.haldiram.com/")
driver.find_element_by_xpath("//a[text()='Click here to order online']").send_keys(Keys.RETURN)
driver.find_element_by_xpath("//a[@class='level-top over']/span[1]").click()


#driver.find_element_by_xpath("//a[@id='our_range']").click()
#driver.find_element_by_xpath("//li[@class='subCatExp sub-cat1']/a[@class='cat-name' and 1]").click()
#driver.find_element_by_xpath("//ul[@class='sub-ranges dropdown-menu subcat']/li[3]/a[@class='cat-pro ' and 1]").click()
#driver.find_element_by_xpath("//div[1]/a[2]/div[@class='product-details' and 1]/p[1]/span[2]").click()

#driver.find_element_by_xpath("//a[text()='Click here to order online']").send_keys(Keys.RETURN)
#driver.find_element_by_xpath("//input[@type='text'][@name='q']").click()

#driver.find_element_by_xpath("//*[@name='search']").click()
#driver.find_element_by_xpath("//*[@name='search']").send_keys("Rasgulla")
#driver.find_element_by_xpath("//*[@name='search']").send_keys(Keys.RETURN)





