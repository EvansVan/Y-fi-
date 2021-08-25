# os for file management
import os, webbrowser, selenium ,time
from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

def yFi():
    # Build tuple of (class, file) to turn in
    submission_dir = '/home/vans/Desktop/test/pass.txt'
    file_tup =open(submission_dir,"r")   

    newpass = file_tup.read()
    print(newpass)

    try:
        #using chrome to access web
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')

        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://192.168.100.1/')

        #find the username box and send value
        driver.find_element_by_id('txt_Username').send_keys('root')

        #find the password box and send value
        driver.find_element_by_id('txt_Password').send_keys('guX5Wd')

        #click login button
        driver.find_element_by_id('loginbutton').click()

        #select advanced tab
        driver.find_element_by_id('addconfig').click()
        
        #select WLAN
        driver.find_element_by_id('wlanconfig').click()

        driver.find_element_by_id('wlan2basic').click()
        
        driver.switch_to.frame("menuIframe")

        #
        #input new password
        driver.find_element_by_id('wlWpaPsk').clear()
        driver.find_element_by_id('wlWpaPsk').send_keys(newpass)
        
        driver.find_element_by_id('hidewlWpaPsk').click()
        time.sleep(3)
        print("yes")
        #
        #select 5g wlan
        #wlan5g = driver.find_element_by_id('wlan5basic')
        #
        #click apply btn
        #pply = driver.find_element_by_id('btnApplySubmit')
        #apply.click()

    except NoSuchElementException as e:
        print(e)

yFi()
