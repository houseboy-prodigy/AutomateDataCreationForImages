import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def open_chart(currency_pair=None):
    # Set the path to your WebDriver executable
    driver_path = "/Users/Anshul/PycharmProjects/pythonProject/chromedriver"
    driver = webdriver.Safari()

    driver.get("https://www.tradingview.com/")

    # Wait for the page to load
    time.sleep(2)

    # Find the search bar and enter the currency pair
    search_bar = driver.find_element_by_xpath("//*[@id='tv-content']/div[1]/div[1]/div[2]/div[1]/div/button/span")
    search_bar.click()
    time.sleep(2)
    search_bar = driver.find_element_by_xpath("//input[ contains(@placeholder, 'Symbol')]")
    time.sleep(2)
    search_bar.send_keys('BTCUSD')
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(2)

if __name__ == "__main__":
    open_chart()
