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

    # sets driver focus back to the parent frame
    driver.switch_to.parent_frame()

    # locating the courses tab in canvas
    courses_tab = driver.find_element(By.ID, 'global_nav_courses_link')
    # clicks on the courses tab
    courses_tab.click()

    # the program waits up to 10 seconds for the sandbox element to be visible
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(driver.find_element(By.XPATH, './/*[@id="nav-tray-portal"]/span/span/div/div/div/div/div/ul[1]/li[1]/a'))
    )

    # locating the sandbox course
    sandbox = driver.find_element(By.XPATH, './/*[@id="nav-tray-portal"]/span/span/div/div/div/div/div/ul[1]/li[1]/a')
    # clicks on the sandbox course
    sandbox.click()

    # locating the discussions tab
    discussions = driver.find_element(By.CLASS_NAME, 'discussions')
    # clicks on the tab
    discussions.click()

    # locating the discussion rows
    disc_rows = driver.find_element(By.CLASS_NAME, 'ic-discussion-row-container')
    print(disc_rows.text)

finally:
    # stop program
    driver.quit()
