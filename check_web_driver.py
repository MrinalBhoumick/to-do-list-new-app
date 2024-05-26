import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Verify if the chromedriver path exists
chrome_driver_path = r'C:\Users\Mrinal Bhoumick\Downloads\chrome-win32\chromedriver.exe'
print("ChromeDriver Path:", chrome_driver_path)
print("Path Exists:", os.path.exists(chrome_driver_path))

# Attempt to initialize WebDriver
try:
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.quit()
    print("WebDriver initialized successfully.")
except Exception as e:
    print("Error initializing WebDriver:", e)
