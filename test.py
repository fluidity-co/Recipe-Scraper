from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import csv

import unicodedata
driver = webdriver.Chrome()

"""
# Goes to the absolute bottom of the page
print("Scrolling to the bottom of the page")
#number of times the bot should scroll down
n = 3000
for i in range(n):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	print("Scrolled down {}/{} times".format(i+1, n))
	time.sleep(3)

print("Scrolling done")
"""

n = 500

def unicode_to_ascii(txt):
	return unicodedata.normalize("NFKD", txt).encode("ascii", "ignore")



with open("recipes.csv", "w+") as file:
	csvWrite = csv.writer(file, delimiter=",")
	
	for page_index in range(1,n+1):
		driver.get("https://www.food2fork.com/index/" + str(page_index))


		recipe_links = driver.find_elements_by_class_name("recipe-link")
		length = len(recipe_links)
		
		for index, link in enumerate(recipe_links):
			print("On page {}/{} and recipe {}/{}".format(page_index, n+1, index+1, length))
			# Opens new tab 
			driver.execute_script('''window.open("http://www.google.com","_blank");''')
			url = link.get_attribute("href")

			tabs = driver.window_handles
			# Opens the recipe link in the new tab and switches the driver to it
			driver.switch_to.window(tabs[1])
			driver.get(url)
			
			# Finds recipe name
			recipe_name = driver.find_elements_by_class_name("recipe-title")[0].text
			ingredients = [] 

			for ingredient in driver.find_elements_by_tag_name("li")[6:]:
				ingredients.append(unicode_to_ascii(ingredient.text))

			link = driver.find_element(By.XPATH, '//a[@target="_blank"]')

			csvWrite.writerow([unicode_to_ascii(recipe_name), unicode_to_ascii(link.get_attribute("href")),ingredients])
			driver.close()
			driver.switch_to.window(tabs[0])
			time.sleep(5)

file.close()

