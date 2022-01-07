from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "/Library/chromedriver"

search_input = input("Enter search: ")
print("Please wait...")
driver = webdriver.Chrome(PATH)
driver.get("https://google.com")
search = driver.find_element_by_name("q")
search.send_keys(search_input)
search.send_keys(Keys.RETURN)
