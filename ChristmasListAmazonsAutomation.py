from selenium import webdriver 
from selenium.webdriver.common.by import By

import time

email = ######enter your email and password if you have
password =  #####enter your email and password if you have
wishList = ["socks"] ##Create a list of items that we want to order




def ShoppingAuto():
   
    driver = webdriver.Chrome()

    driver.get("https://www.amazon.com/")

    ##Find the hover for the sign in options
    button1 = driver.find_element(By.XPATH, '//*[@id="nav-link-accountList-nav-line-1"]')
    button1.click()
    time.sleep(15) ##might need to enter in letters manually to prove you're not a robot
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
        time.sleep(5) ##because of the simplicity of the concept and so the rest of the code can cont (unless I can think of something clever to do before submission),
        ##I'm just going to have the bot sleep, while the user will click on the first item of the page
        atc= driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]')
        atc.click()
        Search2 = driver.find_element(By.ID, "twotabsearchtextbox").clear()
        
    ##Finished up shopping
    checkOut1 = driver.find_element(By.ID, "nav-cart-count-container")
    checkOut1.click()
    proceed = driver.find_element(By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span/input')
    ###proceed.click()

    """
    This is where I'll end the code since it's getting to the point where
    we want human interaction to ensure out bot "did it right"
    """
    
    
   
  
    
  
ShoppingAuto()

