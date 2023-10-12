import click
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up the Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--disable-gpu")  # Applicable to windows os only
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--disable-extensions')

class WebsiteScreenshot:
    """
    A class used to capture a screenshot of a website
    """
    def __init__(self, url, width, height):
        self.url = url
        self.width = width
        self.height = height

    def capture_screenshot(self):
        """
        Capture a screenshot of the website
        """
        try:
            # Initialize the web driver (you need to download the corresponding WebDriver for your browser)
            driver = webdriver.Chrome(options=chrome_options)
            driver.set_window_size(self.width, self.height)  # set the window size
            driver.get(self.url)

            # Capture a screenshot and save it to the specified path
            screenshot = driver.get_screenshot_as_png()

            # Close the driver
            driver.quit()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
        return screenshot

@click.command()
@click.argument('url')
@click.option('--width', default=1280, help='The desired screen width.')
@click.option('--height', default=800, help='The desired screen height.')
def capture(url, width, height):
    """
    A simple command line tool to capture a screenshot of a website.
    """
    screenshot = WebsiteScreenshot(url, width, height).capture_screenshot()
    if screenshot:
        with open('screenshot.png', 'wb') as file:
            file.write(screenshot)
        click.echo('Screenshot saved as screenshot.png.')
    else:
        click.echo('Failed to capture the screenshot.')

if __name__ == '__main__':
    capture()
