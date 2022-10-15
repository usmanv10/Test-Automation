from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Using a service to open the chrome driver. Needs to be defined above
s=Service("C:/Users/usman.ali/PycharmProjects/pythonProject/chromedriver.exe")

# Starts the chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# URL
url = "https://web.esp-test.net/enterprise/ets/login"
driver.get(url)

username = "espe.admin@collectionhq.com"
password = "d1sc0ver"

driver.implicitly_wait(10)
search = driver.find_element(By.ID, "username")
search.send_keys("espe.admin@collectionhq.com")

search = driver.find_element(By.ID, "password")
search.send_keys("d1sc0ver")

search = driver.find_element(By.ID, "submit_signin").click()

driver.implicitly_wait(10)

search = driver.find_element(By.XPATH("//*[text()='Carts']"));

# search = driver.find_element(By.NAME, "Carts")

# search.send_keys(Keys.ENTER)


