print("=== INSTAGRAM FOLLOWERS EXTRACTING TOOL  ===")
print('===== DEVELOPER: anhvi.02 (github) =====')


# INPUT WHETHER OR NOT TO FIND UNFOLLOWERS 
print('=== THIS PROGRAMM WILL EXTRACT YOUR INSTAGRAM CURRENT FOLLOWERS AND FIND UNFOLLOWERS ===')
print('= PRESS 1 IF YOU ONLY WANT TO EXTRACT YOUR INSTAGRAM CURRENT FOLLOWERS ===')
print('= PRESS 2 IF YOU WANT TO EXTRACT YOUR INSTAGRAM CURRENT FOLLOWERS AND FIND UNFOLLOWERS ===')
find_unfollower = int(input('---> YOUR ANSWER: (1 or 2): '))
if find_unfollower == 2:
    # input old users file name
    while True:
        try:
            old_users_file_name = input('---> INPUT FILE NAME FOR OLD FOLLOWERS (make sure this file is in path): ')
            old_users_file_name = str(old_users_file_name) + '.txt'
            old_users = []
            with open(old_users_file_name, "r", encoding="utf-8") as file:
                # Read each line from the file
                lines = file.readlines()
                # Iterate over each line
                for line in lines:
                    old_users.append(line.strip())
            print(f'=== CONFIRM FILE NAME: {old_users_file_name} ===')
            break
        except:
            print('=== FAILED TO OPEN OLD USERS LIST FILE, TRY AGAIN ===')

# input current users file name
current_users_file_name = input('--> INPUT FILE NAME TO SAVE CURRENT FOLLOWERS (name of the file to save current followers): ')
current_users_file_name = str(current_users_file_name) + '.txt'
print(f'=== CONFIRM FILE NAME: {current_users_file_name} ===')

# INPUT WHETHER OR NOT TO RUN WITH CHROME UI
print('=== DO YOU WANT TO RUN THE CRAWLER WITH CHROME INTERFACE ===')
print('= PRESS 1 IF YOU DO ===')
print('= PRESS 2 IF YOU DO NOT ===')
headless_option = int(input('---> YOUR ANSWER: (1 or 2): '))

# input account info
username = input('---> INPUT INSTAGRAM USERNAME: ')

import getpass
password = getpass.getpass('---> INPUT INSTAGRAM PASSWORD: ')


# INSTALL LIBRARIES
print("=== CHECKING LIBRARIES IN ENVIRONMENT ===")
import importlib
import subprocess

def check_and_install(package):
    try:
        importlib.import_module(package)
        print(f"{package} is already installed.")
    except ImportError:
        print(f"{package} is not installed. Installing...")
        subprocess.check_call(["pip", "install", package])

# List of required packages
required_packages = ['webdriver_manager', 'selenium', 'beautifulsoup4', 'bs4']

# Check and install missing packages
for package in required_packages:
    check_and_install(package)



# IMPORT LIBRARIES
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import os
# ignore warning
import warnings
warnings.filterwarnings('ignore')



# SETTING BROWER
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--start-maximized")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")
options.add_argument("--no-sandbox")
# maximize window for Mac
options.add_argument("--kiosk")
if headless_option == 2:
    options.add_argument("--headless")

# OPEN BROWSER
chrome_install = ChromeDriverManager().install()

folder = os.path.dirname(chrome_install)
chromedriver_path = os.path.join(folder, "chromedriver.exe")

service = ChromeService(chromedriver_path)

driver = webdriver.Chrome(service=service)
driver.implicitly_wait(0)

# maximize window
driver.maximize_window()

print("=== DRIVER SET UP AND BROWSER OPENED ===")

# A FUNCTION TO WAIT FOR ELEMENT TO PRESENT
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def wait_for_element(driver, locator, timeout=20):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        print("Element not found within the specified timeout period.")

# ACCESS INSTAGRAM
sleep(3)
link = 'https://www.instagram.com/'
driver.get(link)
element_locator = (By.CSS_SELECTOR, "div[class='_ab1y']")
wait_for_element(driver, element_locator)


# LOGIN
# input username
sleep(3)
css_username = 'label._aa48'
object_username = driver.find_elements(By.CSS_SELECTOR, css_username)[0]
object_username.send_keys(username)

# input password
sleep(3)
css_password = 'label._aa48'
object_password = driver.find_elements(By.CSS_SELECTOR, css_username)[1]
object_password.send_keys(password)

# submit
sleep(3)
driver.find_element(By.ID, 'loginForm').submit()
print("=== LOGIN SUCCESSFULLY ===")



# ACCESS PROFILE
sleep(3)
element_locator = (By.LINK_TEXT, 'Profile')
wait_for_element(driver, element_locator)

object_profile = driver.find_element(*element_locator)
object_profile.click()


print("=== PROFILE ACCESSED ===")

# EXTRACTING FOLLOWERS
action = webdriver.ActionChains(driver)
# click followers button
sleep(3)
element_locator_followers = (By.PARTIAL_LINK_TEXT, 'followers')
wait_for_element(driver, element_locator_followers)

object_button_followers = driver.find_element(*element_locator_followers)
object_button_followers.click()



# move to follower list
sleep(3)
element_locator_follower_list = (By.CSS_SELECTOR, 'div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6')
wait_for_element(driver, element_locator_follower_list)

object_follower_list = driver.find_element(*element_locator_follower_list)
action.move_to_element(object_follower_list).perform()

# scroll through the follower list
# scrollable object
sleep(3)
object_followers_list = driver.find_element(By.CSS_SELECTOR, 'div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6')

# start to scroll
last_ht, height = 0, 1
while last_ht != height:
    last_ht = height
    sleep(4.5)
    # scroll down and retrun the height of scroll
    height = driver.execute_script(""" 
    arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight; """, object_followers_list)
    
# get loaded html docs
html = driver.page_source
soup = BeautifulSoup(html)

# extract users
current_users = []
list_followers = list(soup.select('div[class="xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6"] > div > div')[0])
for follower in list_followers:
    user = follower.text.replace('Remove','').replace('·','').replace('Follows you','').replace('Follow','')
    current_users.append(user)
    
# SAVE CURRENT USERS LIST TO FILE
with open(current_users_file_name, "w", encoding="utf-8") as file:
    # Iterate over the list of names
    for user in current_users:
        # Write each name followed by a newline character
        file.write(user + "\n")
print(f' === CURRENT USERS LIST SAVED SUCCESSFULLY TO {current_users_file_name} ===')

# end session
driver.quit()

if find_unfollower == 2:
    # SPECIFY UNFOLLOWERS AND NEW FOLLOWERS
    current_users = set(current_users)
    old_users = set(old_users)
    # Find unfollowed users
    unfollowed_users = old_users - current_users

    # Find new followers
    new_followers = current_users - old_users

    # Convert sets back to lists if needed
    unfollowed_users_list = list(unfollowed_users)
    new_followers_list = list(new_followers)

    print('\n')
    print('=== RESULT: ===')
    print("=== Unfollowed users:", unfollowed_users_list)
    print("=== New followers:", new_followers_list)
