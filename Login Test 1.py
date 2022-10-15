from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Using a service to open the chrome driver. Needs to be defined above
s=Service("C:/Users/usman.ali/PycharmProjects/pythonProject/chromedriver.exe")

# define the values
username = "espe.admin@collectionhq.com"
password = "d1sc0ver"

# Starts the chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# URL
url = "https://web.esp-test.net/enterprise/ets/login"
driver.get(url)


driver.implicitly_wait(10)

# finds the username textbox and enters the username
search = driver.find_element(By.ID, "username")
search.send_keys("espe.admin@collectionhq.com")

# finds the password textbox and enters the password
search = driver.find_element(By.ID, "password")
search.send_keys("d1sc0ver")

# finds the sign in button and clicks it
search = driver.find_element(By.ID, "submit_signin").click()

print("logged in successfully")

driver.implicitly_wait(10)

# Tries to find the text "Carts"

driver.find_element(By.XPATH, "//*[contains(text(), 'Carts')]")

print ("the text Carts has been found!")

driver.close()





