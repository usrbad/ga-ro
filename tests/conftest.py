import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--window-size=1600,1200')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
