from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.action_chains import ActionChains
options=Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Chrome(options=options)
driver.get("https://www.google.co.in/webhp?tab=rw&authuser=0")
element=driver.find_element_by_xpath("input[@title='Search']")
element.send_keys('nishiag.218')
element.send_keys(Keys.ENTER)
driver.close()