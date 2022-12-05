from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import messagebox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

email = "mikamunari002@gmail.com"
password =  "FastBreak!"
wishList = ["backpack", "scooter"]
#Amazon Navigation 
##Sign into Amazon Prime Account 


item = "bike"
def LaunchBrowser():
   
    driver = webdriver.Chrome()

    driver.get("https://www.amazon.com/")
    time.sleep(10)

    ##Find the hover for the sign in options
    button1 = driver.find_element(By.XPATH, '//*[@id="nav-link-accountList-nav-line-1"]')
    button1.click()
    
    ##enter credentials to sign into personal account
    Sign = driver.find_element(By.ID, "ap_email")
    Sign.click()
    Sign.send_keys(email)
    confirm1= driver.find_element(By.XPATH, '//*[@id="continue"]')
    confirm1.click()
    
    Pass = driver.find_element(By.XPATH, '//*[@id="ap_password"]')
    Pass.click()
    Pass.send_keys(password)
    confirm2= driver.find_element(By.XPATH, '//*[@id="signInSubmit"]')
    confirm2.click()
    

    for item in wishList:
        ##Searches for items
        Search = driver.find_element(By.ID, "twotabsearchtextbox")
        Search.click()
        Search.send_keys(item)
        driver.find_element(By.ID, "nav-search-submit-button").click()
        time.sleep(10) ##because of the simplicity of the concept and so the rest of the code can cont (unless I can think of something clever do do before submission),
        ##I'm just going to have the bot sleep, us the user will click on items

        ##Adds items to Cart
        atc= driver.find_element(By.ID, "add-to-cart-button")
        atc.click
    ##Finished up shopping
    checkOut1 = driver.find_element(By.ID, "nav-cart-count-container")
    checkOut1.click()
    proceed = driver.find_element(By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span/input')
    ###proceed.click()

    """
    This is where I'll end the code since it's getting to the point where
    we want human interaction to ensure out bot "did it right"
    """
    
    
   
  
    
  
LaunchBrowser()  
