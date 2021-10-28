import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import creds for the payload login
import creds

"""
In order to run the program, go to the creds.py, change the username
and password to your own, then just run the code. 
It should automatically navigate through canvas, enter your credentials,
and send you a duo authentication. You should then be logged into Canvas.
"""

# url for UW-Parkside Canvas login page
url = 'https://www.uwp.edu/explore/offices/campustechnologyservices/innovationsinlearning/canvas-login.cfm'
# url for secure login
secure_url = 'https://uwpks.instructure.com/?login_success=1'

# dictionary for personal UWP login
payload = {
    'userNameInput': creds.username,
    'passwordInput': creds.password
}

try:

    # chrome webdriver
    driver = webdriver.Chrome()

    # implicit wait for 60 seconds
    driver.implicitly_wait(60)

    # navigation to the assigned url
    driver.get(url)

    # locating the canvas user login button
    canvas_login = driver.find_element(By.CLASS_NAME, 'CS_Image_IMG')
    # clicks on the button
    canvas_login.click()

    # locating the campus selection list
    select_org = driver.find_element(By.ID, "campus-select")
    # clicks to open the list options
    select_org.click()

    # locating the UW-Parkside list option
    park_side = driver.find_element(By.XPATH, './/*[@id="campus-select"]/option[9]')
    # clicks on UW-Parkside option
    park_side.click()

    # locating the go button
    submit_go = driver.find_element(By.ID, 'submit-go')
    # clicks on the go button
    submit_go.click()

    # grabs the dynamic login page url
    login_url = driver.current_url

    # enters the username from payload
    driver.find_element(By.ID, 'userNameInput').send_keys(payload['userNameInput'])
    # enters the password from payload
    driver.find_element(By.ID, 'passwordInput').send_keys(payload['passwordInput'])

    # locating the submit button
    sign_in = driver.find_element(By.ID, 'submitButton')
    # clicks on the submit button
    sign_in.click()

    # sets driver focus on the duo iFrame
    driver.switch_to.frame(driver.find_element(By.XPATH, './/*[@id="duo_iframe"]'))

    # locating the Send Me a Push Button for duo authentication
    send_push = driver.find_element(By.XPATH, './/*[@id="auth_methods"]/fieldset/div[1]/button')
    # clicks on the send_push button
    send_push.click()

    WebDriverWait(driver, 60).until(
        EC.url_changes(login_url)
    )

    # waits 10 seconds
    # placeholder for testing
    time.sleep(10)

    # prints out the title of the dashboard to confirm the login
    # just a place holder
    new_url = driver.current_url
    print(new_url)

    # extraction code will go below

finally:
    # stop program
    driver.quit()
