from webdriver_manager.chrome import ChromeDriverManager


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Setup the WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

def open_chart(currency_pair):
    # Set the path to your WebDriver executable

    driver.get("https://www.tradingview.com/")

    # Wait for the page to load
    time.sleep(2)

    # Find the search bar and enter the currency pair
    search_bar = driver.find_element_by_xpath("//*[@id='tv-content']/div[1]/div[1]/div[2]/div[1]/div/button/span")
    search_bar.click()
    search_bar = driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div/div/div[1]/div/div[1]/span/form/input")
    search_bar.send_keys(currency_pair)
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(2)

    # Click the first search result
    first_result = driver.find_element_by_xpath("//div[@class='tv-feed-layout__card'][1]")
    first_result.click()

    print("Chart opened successfully.")

if __name__ == "__main__":
    currency_pair = "BTCUSD"  # Replace with your desired currency pair
    open_chart(currency_pair)
