from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--disable-gpu")  # Applicable to windows os only
chrome_options.add_argument('start-maximized') 
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--disable-extensions')

# Set the location of the webdriver
service = Service('chromedriver')  # Update with the path to your chromedriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to URL
    driver.get('http://www.example.com')
    print('Page title: %s' % driver.title)
    # Maybe you need to click some options; use driver.find_element to locate the options and .click() to click on them

    # Wait for the necessary page elements to load before taking a screenshot
    driver.implicitly_wait(3)  # seconds

    # Take screenshot
    driver.get_screenshot_as_file('screenshot.png')  # Update with desired screenshot file path
    print('Screenshot taken!')
finally:
    # Close the browser
    driver.quit()
