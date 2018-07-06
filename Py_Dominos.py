from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Python37\TestProj1\ProjectPython1\driver\chromedriver.exe")
driver.get("https://www.dominos.co.in")
driver.set_page_load_timeout("50")

#Add Product to Cart
driver.find_element_by_xpath("//A[@href='https://www.dominos.co.in/menu'][text()='Our menu']").click()
driver.find_element_by_xpath("//A[@href='https://www.dominos.co.in/menu/veg-pizzas'][text()='View All']").click()
driver.find_element_by_xpath("//div[1]/div[@class='row' and 1]/a[@class='btn btn-primary custom-btn' and 1]").click()
time.sleep(5)
driver.find_element_by_xpath("//li[@id='pickUpChkBox']/label[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='custCity']").click()
driver.find_element_by_xpath("//input[@id='custCity']").send_keys("NAGPUR")
driver.find_element_by_xpath("//input[@id='custCity']").send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath("//input[@id='custCity']").send_keys(Keys.RETURN)
time.sleep(3)
driver.find_element_by_xpath("//input[@id='custAddress']").click()
driver.find_element_by_xpath("//input[@id='custAddress']").send_keys("Madhav")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='custAddress']").send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath("//input[@id='custAddress']").send_keys(Keys.RETURN)
time.sleep(3)
driver.find_element_by_xpath("//input[@id='buildOrderBtn']").click()
time.sleep(3)

#Login Code
driver.find_element_by_xpath("//a[@id='login']").click()
time.sleep(5)
driver.find_element_by_xpath("//input[@id='txtMobileNo']").click()
time.sleep(5)
driver.find_element_by_xpath("//input[@id='txtMobileNo']").send_keys("9765102117")
time.sleep(5)
driver.find_element_by_xpath("//input[@id='txtMobileNo']").send_keys(Keys.RETURN)
time.sleep(5)
#driver.find_element_by_xpath("//input[@id='jqi_state0_buttonOk']").click()
#time.sleep(5)
driver.find_element_by_xpath("//input[@id='txtPassword']").click()
time.sleep(5)
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("2784")
time.sleep(5)
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys(Keys.RETURN)
time.sleep(5)
driver.find_element_by_xpath("//input[@id='userlogin']").click()
time.sleep(5)


#MouseOver Action Code
actions =chains(driver)
val1 = driver.find_element_by_xpath("//a[@id='customize_pizza_1']")
actions.move_to_element(val1).perform()
time.sleep(2)
val2 = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='quick_add_1']")))
val2.click()
#MouseOver Action End
#Add Product to Cart End

time.sleep(3)
driver.find_element_by_xpath("//a[@id='checkout']").click()
time.sleep(5)
driver.find_element_by_xpath("//a[@id='crossButtonUpselling']").click()
time.sleep(5)
driver.find_element_by_xpath("//a[@id='crossButtonUpselling']/../../../../../..//input[@id='firstname']").send_keys("FirstName")
driver.find_element_by_xpath("//a[@id='crossButtonUpselling']/../../../../../..//input[@id='lastname']").send_keys("LastName")
driver.find_element_by_xpath("//a[@id='crossButtonUpselling']/../../../../../..//input[@id='email_id']").send_keys("Email@test.com")
driver.find_element_by_xpath("//a[@id='crossButtonUpselling']/../../../../../..//input[@id='mobile']").send_keys("1234567890")
driver.find_element_by_xpath("//input[@id='proceed_to_payment_button']").click()

