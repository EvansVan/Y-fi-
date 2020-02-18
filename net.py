# os for file management
import os, webbrowser, selenium 
from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def yFi():
    # Build tuple of (class, file) to turn in
    submission_dir = '/home/vans/Desktop/test'

    dir_list = list(os.listdir(submission_dir))
    for directory in dir_list:
        file_list = list(os.listdir(os.path.join(submission_dir,directory)))
        if len(file_list) != 0:
            file_tup = (directory, file_list[0])

    print(file_tup)

    #using chrome to access web
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://192.168.100.1/')

    #find the username box and send value
    driver.find_element_by_id('txt_Username').send_keys('root')

    #find the password box and send value
    driver.find_element_by_id('txt_Password').send_keys('@Idontlike5')

    #click login button
    driver.find_element_by_id('loginbutton').click()

    #select advanced tab
    driver.find_element_by_id('addconfig').click()
    #
    #select WLAN
    driver.find_element_by_id('wlanconfig').click()
    #
    ##input new password
    table = driver.find_element_by_css_selector('wlWpaPsk')
    #
    #select 5g wlan
    wlan5g = driver.find_element_by_id('wlan5basic')
    #
    #click apply btn
    apply = driver.find_element_by_id('btnApplySubmit')
    apply.click()

yFi()
