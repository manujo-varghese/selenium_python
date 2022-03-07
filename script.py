from selenium import webdriver

PATH = "/Users/manuvarghese/Documents/SeleniumDrivers/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

print(driver.title)

driver.quit()