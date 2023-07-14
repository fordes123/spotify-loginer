from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys, argparse, time


def main():
   parser = argparse.ArgumentParser()
   parser.add_argument("-e", "-u", "--email", help="Spotify account email", required=True)
   parser.add_argument("-p", "--password", help="Spotify account password", required=True)
   args = parser.parse_args()

   if not args.email or not args.password:
      print("Error: email and password cannot be empty")
      exit(1)

   chrome_options = Options()
   chrome_options.add_argument('--headless')
   chrome_options.add_argument('--no-sandbox')
   chrome_options.add_argument('--disable-dev-shm-usage')
   driver = webdriver.Chrome()
   driver.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F")
   
   # Wait for the page to load
   wait = WebDriverWait(driver, 10)
   wait.until(EC.presence_of_element_located((By.ID, "login-button")))

   # Login
   element = driver.find_element(By.ID, 'login-username')
   element.send_keys(args.email)
   element = driver.find_element(By.ID, "login-password")
   element.send_keys(args.password)
   element.send_keys(Keys.RETURN)

   # Wait for the page to load
   wait = WebDriverWait(driver, 10)
   wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "figure[data-testid='user-widget-avatar']")))
   time.sleep(5)

   # Check if login was successful
   if driver.current_url.startswith('https://open.spotify.com/'):
      print('Login successful')
      sys.exit(0)
   else:
      print('Login failed or timed out')
      sys.exit(1)

if __name__ == "__main__":
   main()
