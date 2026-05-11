from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import data


class ClickToLogoPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    #нажатие на лого с ожижанием 
    def click_with_wait(self, locator):
        self.click(locator)
        #ожидание открытия вкладки 
        WebDriverWait(self.driver, 10).until(ec.number_of_windows_to_be(2))

    #переключение на новую вкладку (с ожиданием)
    def go_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        #ожидание загрузки
        WebDriverWait(self.driver, 10).until(ec.url_to_be(data.url_dzen))