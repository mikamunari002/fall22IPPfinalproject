from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import messagebox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


wishList = ["backpack", "scooter", "cologne", "bike"]
#Amazon Navigation 
##Sign into Amazon Prime Account 

Username = "tun06662"
Password = "FFastBreakk44%"

def LaunchBrowser():
   
    driver = webdriver.Chrome()

    driver.get("https://www.amazon.com/")
    time.sleep(20)
    driver.quit()    
    
  
LaunchBrowser()  
    
"""
UserOptions = driver.find_element(By.ID, "nav-link-acciuntList=nav-line-1")
UserOptions.click()

signIn = driver.find_element(By.CLASS_NAME, "nav-action-inner")
signIn.click()
    



driver.find_element("name", "j_username").send_keys(Username)
driver.find_element("name", "j_password").send_keys(Password)
link = driver.find_element(By.type
link.click()

report = driver.find_element(By.LINK_TEXT, "Reports")
report.click()

trend_report = driver.find_element(By.LINK_TEXT, "Trend Reports")
trend_report.click()

Denial_Rate = driver.find_element(By.LINK_TEXT, "Denial Rate")
Denial_Rate.click()

time.sleep(15)


export_options = driver.find_element(By.LINK_TEXT, "Export Options")    
export_options.click() 

download_csv = driver.find_element(By.LINK_TEXT, "Download Details to CSV")
download_csv.click()


"""