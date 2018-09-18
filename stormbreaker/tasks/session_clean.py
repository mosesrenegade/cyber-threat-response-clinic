from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os

success = True

wd = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://console.amp.cisco.com")
    wd.find_element_by_id("user_email").click()
    wd.find_element_by_id("user_email").clear()
    wd.find_element_by_id("user_email").send_keys("moses+HT@cisco.com")
    wd.find_element_by_id("user_password").click()
    wd.find_element_by_id("user_password").clear()
    wd.find_element_by_id("user_password").send_keys("C1sc012345+")
    wd.find_element_by_name("button").click()
    wd.find_element_by_xpath("//li[@class='management']//button[normalize-space(.)='Management']").click()
    wd.find_element_by_link_text("Computers").click()
    
    try:
        wd.find_element_by_xpath("//span[@id='selected-row-actions']/button[1]").click()
        wd.find_element_by_xpath("//span[@id='selected-row-actions']/button[3]").click()
        wd.find_element_by_xpath("//form[@id='delete-selected-form']//button[.='Delete']").click()
    except:
        pass
    
    if not ("No computers" in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")

    else:
        success = True
        print("No computers where probably in the system mate!")

    wd.get("https://console.amp.cisco.com/logout")
    
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
