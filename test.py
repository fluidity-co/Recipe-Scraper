from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.food2fork.com/")

"""
for i in range(10):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(10)
"""

links = [x for x in driver.find_elements_by_class_name("recipe-link")]
driver.execute_script('''window.open("{}","_blank");'''.format(links[0].get_attribute("href")))

links[4].send_keys(Keys.CONTROL + "t")

print(links)
