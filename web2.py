import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def open_chart(currency_pair=None):
    # Set the path to your WebDriver executable
    driver_path = "/Users/Anshul/PycharmProjects/pythonProject/chromedriver"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("https://www.tradingview.com/")

    # Wait for the page to load
    time.sleep(2)

    #Find the search bar and enter the currency pair
    search_bar = driver.find_element_by_xpath("//*[@id='tv-content']/div[1]/div[1]/div[2]/div[1]/div/button/span")
    search_bar.click()
    time.sleep(2)
    search_bar = driver.find_element_by_xpath("//input[ contains(@placeholder, 'Symbol')]")
    time.sleep(2)
    search_bar.send_keys('BTCUSD')
    search_bar.send_keys(Keys.RETURN)
    chartIndex = 0
    # Wait for the chart to load
    time.sleep(5)

    # Find the chart element
    chart = driver.find_element_by_xpath("//div[contains(@class, 'chart-gui-wrapper')]")

    # Get the chart dimensions
    chart_width = chart.size['width']
    chart_height = chart.size['height']

    # Create an ActionChains object
    actions = ActionChains(driver)

    # Generate random positions within the chart
    random_x1 = random.randint(0, chart_width)
    random_y1 = random.randint(0, chart_height)

    random_x2 = random.randint(0, chart_width)
    random_y2 = random.randint(0, chart_height)


    # Move the cursor to the first random point and press Alt + 'h'
    actions.move_to_element_with_offset(chart, random_x1, random_y1).key_down(Keys.ALT).send_keys('h').key_up(Keys.ALT).perform()

    actions.reset_actions()

    # Move the cursor back to the first random point and double-click
    actions.move_to_element_with_offset(chart, random_x1, random_y1).double_click().perform()
    time.sleep(2)
    coord = driver.find_element_by_xpath("//*[@id='coordinates']")
    coord.click()

    selected_text = driver.execute_script("return window.getSelection().toString();")
    # Print the selected text
    first_line_val = selected_text
    print(first_line_val)

    submit = driver.find_element_by_xpath("//*[@id='overlap-manager-root']/div/div/div[1]/div/div[4]/div/span/button")
    submit.click()

    actions_second_line = ActionChains(driver)
    actions_second_line.move_to_element_with_offset(chart, random_x2, random_y2).key_down(Keys.ALT)\
        .send_keys('h').key_up(Keys.ALT).perform()

    actions_second_line = ActionChains(driver)

    # Move the cursor back to the first random point and double-click
    actions_second_line.move_to_element_with_offset(chart, random_x2, random_y2).double_click().perform()
    time.sleep(2)
    coord = driver.find_element_by_xpath("//*[@id='coordinates']")
    coord.click()

    selected_text = driver.execute_script("return window.getSelection().toString();")
    # Print the selected text
    second_line_val = selected_text
    print(second_line_val)

    submit = driver.find_element_by_xpath("//*[@id='overlap-manager-root']/div/div/div[1]/div/div[4]/div/span/button")
    submit.click()
    time.sleep(2)
    driver.save_screenshot(f"/Users/Anshul/Downloads/chart1.png")
    """
    # Reset the actions
    actions.reset_actions()
    # Move the cursor to the second random point and press Alt + 'h'
    actions.move_to_element_with_offset(chart, random_x2, random_y2).key_down(Keys.ALT).send_keys('h').key_up(Keys.ALT).perform()
    # Reset the actions
    actions.reset_actions()
    actions.move_to_element_with_offset(chart, random_x1, random_y1).double_click().perform()
    time.sleep(2)
    coord = driver.find_element_by_xpath("//*[@id='coordinates']")
    coord.click()
    selected_text = driver.execute_script("return window.getSelection().toString();")
    # Print the selected text
    second_line_val = selected_text
    print(second_line_val)
    driver.save_screenshot(f"/Users/Anshul/Downloads/chart{chartIndex}.png")



    # Reset the actions
    actions.reset_actions()

    # Move the cursor back to the first random point and double-click
    actions.move_to_element_with_offset(chart, random_x1, random_y1).double_click().perform()

    coord = driver.find_element_by_xpath("//*[@id='coordinates']")
    coord.click()
    selected_text = driver.execute_script("return window.getSelection().toString();")
    # Print the selected text
    first_line_val = selected_text
    print(first_line_val)
    # Wait for a while
    """



if __name__ == "__main__":
    open_chart()
