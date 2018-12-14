from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.food2fork.com/")


#Todo: add loop to continually go to the bottom
"""
for i in range(10)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	time.sleep(5)
"""
recipes = []

for link in driver.find_elements_by_class_name("recipe-link")[:3]:
	
	driver.execute_script('''window.open("http://www.google.com","_blank");''')
	url = link.get_attribute("href")
	tabs = driver.window_handles
	driver.switch_to.window(tabs[1])
	driver.get(url)
	

	recipe_name = driver.find_elements_by_class_name("recipe-title")[0].text
	ingredients = [] 

	for ingredient in driver.find_elements_by_tag_name("li")[6:]:
		ingredients.append(ingredient.text)

	recipes.append([recipe_name, ingredients])
	driver.close()
	driver.switch_to.window(tabs[0])
	time.sleep(5)



print(recipes)
