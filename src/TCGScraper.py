from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set creds
TCG_PLAYER_URL = "https://www.tcgplayer.com"
USERNAME = "<YOUR_EMAIL_HERE>"
PASSWORD = "<YOUR_PASSWORD_HERE>"

def setup_driver():
    """Set up the Selenium WebDriver"""
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def main(url):
    
    driver = setup_driver()
    try:
        driver.get(url)

        login_user(driver)

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()

def login_user(driver: webdriver.Chrome):

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='profile-menu-btn']/span"))
    )
    element.click()

    login_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='user-profile-menu']/div/div[2]/span[2]/a[1]"))
    )
    login_button.click()

    username_field = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "Email"))
    )
    username_field.send_keys(USERNAME)

    password_field = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.NAME, "Password"))
    )
    
    password_field.send_keys(PASSWORD)

    login_button = driver.find_element(By.XPATH, "//*[@id='signInForm']/button/span")
    login_button.click()
    time.sleep(30)  # Wait for login to complete
    print("Logged in successfully")

if __name__ == "__main__":
    main(TCG_PLAYER_URL)