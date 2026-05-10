import pytest
from selenium import webdriver
import data

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(data.url)
    yield driver
    driver.quit()