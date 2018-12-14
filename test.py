from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import csv

driver = webdriver.Chrome()
driver.get("https://www.food2fork.com/")


# Goes to the absolute bottom of the page
print("Scrolling to the bottom of the page")
#number of times the bot should scroll down
n = 1000 
for i in range(n):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	print("Scrolled down {}/{} times".format(i+1, n))
	time.sleep(3)

print("Scrolling done")
recipes = []
# Goes through each recipe 
print("Going through each recipe")
recipe_links = driver.find_elements_by_class_name("recipe-link")
length = len(recipe_links)

for index, link in enumerate(recipe_links):
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
		ingredients.append(ingredient.text)

	link = driver.find_element(By.XPATH, '//a[@target="_blank"]')

	recipes.append([recipe_name, link.get_attribute("href"),ingredients])
	driver.close()
	driver.switch_to.window(tabs[0])
	print("Finished recipe: {}/{}".format(index+1, length))
	time.sleep(5)



print(recipes)

with open("recipes.csv", "w+") as file:
	csvWrite = csv.writer(file, delimiter=",")
	csvWrite.writerows(recipes)