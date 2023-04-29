import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def open_chart(index):
    driver = initialize_driver()
    driver.get("https://www.tradingview.com/")
    time.sleep(2)

    search_currency_pair(driver, 'BTCUSD')
    time.sleep(5)

    for _ in range(2):
        random_x1, random_y1, random_x2, random_y2 = make_lines_and_get_screenshot(driver, index)
        index += 1
        remove_drawings(driver, random_x1, random_y1)
        remove_drawings(driver, random_x2, random_y2)

def initialize_driver():
    driver_path = "/Users/Anshul/PycharmProjects/pythonProject/chromedriver"
    driver = webdriver.Chrome(executable_path=driver_path)
    return driver

def search_currency_pair(driver, currency_pair):
    search_bar = driver.find_element_by_xpath("//*[@id='tv-content']/div[1]/div[1]/div[2]/div[1]/div/button/span")
    search_bar.click()
    time.sleep(2)
    search_bar = driver.find_element_by_xpath("//input[contains(@placeholder, 'Symbol')]")
    time.sleep(2)
    search_bar.send_keys(currency_pair)
    search_bar.send_keys(Keys.RETURN)

def make_lines_and_get_screenshot(driver, index):
    chart = get_chart_element(driver)
    chart_width, chart_height = get_chart_dimensions(chart)


    random_x1, random_y1 = generate_random_coordinates(chart_width, chart_height)
    random_x2, random_y2 = generate_random_coordinates(chart_width, chart_height)

    draw_horizontal_line(driver,chart, random_x1, random_y1)
    first_line_val = get_line_value(driver)
    print(first_line_val)

    draw_horizontal_line(driver, chart, random_x2, random_y2)
    second_line_val = get_line_value(driver)
    print(second_line_val)

    time.sleep(2)
    chart.click()
    time.sleep(2)
    driver.save_screenshot(f"/Users/Anshul/PycharmProjects/pythonProject/testPhotos/chart{index}.png")

    return random_x1, random_y1, random_x2, random_y2

def get_chart_element(driver):
    return driver.find_element_by_xpath("//div[contains(@class, 'chart-gui-wrapper')]")

def get_chart_dimensions(chart):
    return chart.size['width'], chart.size['height']

def generate_random_coordinates(chart_width, chart_height):
    return random.randint(0, chart_width), random.randint(0, chart_height)

def draw_horizontal_line(driver,chart, x, y):
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(chart, x, y).key_down(Keys.ALT).send_keys('h').key_up(Keys.ALT).perform()
    actions2 = ActionChains(driver)
    actions2.move_to_element_with_offset(chart, x, y).double_click().perform()
    time.sleep(2)

def get_line_value(driver):
    coord = driver.find_element_by_xpath("//*[@id='coordinates']")
    coord.click()
    selected_text = driver.execute_script("return window.getSelection().toString();")
    submit = driver.find_element_by_xpath("//*[@id='overlap-manager-root']/div/div/div[1]/div/div[4]/div/span/button")
    submit.click()
    return selected_text

def remove_drawings(driver, random_x1, random_y1):
    chart = get_chart_element(driver)
    new_Action = ActionChains(driver)
    new_Action.move_to_element_with_offset(chart, random_x1, random_y1).click().send_keys(Keys.DELETE).perform()

if __name__ == "__main__":
    ChartIndex = 5
    open_chart(ChartIndex)
