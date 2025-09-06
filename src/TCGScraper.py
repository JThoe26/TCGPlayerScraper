from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_driver():
    """Set up the Selenium WebDriver."""
    chrome_options = Options()
    # chrome_options.add_argument("--headless") 
    # chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def scrape_website(url):
    """Scrape data from the given URL."""
    driver = setup_driver()
    try:
        driver.get(url)

        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='profile-menu-btn']/span"))
        )
        element.click()
        
        login_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='user-profile-menu']/div/div[2]/span[2]/a[1]"))
        )
        login_button.click()

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    target_url = "https://www.tcgplayer.com"
    scrape_website(target_url)