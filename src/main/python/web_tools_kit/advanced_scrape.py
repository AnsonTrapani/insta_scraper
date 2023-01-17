import selenium
from selenium import webdriver

driver = webdriver.Chrome()
username = input("Enter the username of the account exactly how it appears on Instagram: ")
base_url = "https://www.instagram.com/"
driver.get(base_url + username)

