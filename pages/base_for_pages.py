from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BaseForPages:

    def __init__(self, driver):
        self.driver = driver

    #Метод, чтобы кликнуть на элемент
    def click(self, locator):
        element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    #Метод, чтобы получить текст элемента
    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator)).text

    #Видимость элемента
    def is_displayed(self, locator):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator)).is_displayed()
    
    #заполнение поля
    def send_keys(self, locator, value):
        return self.driver.find_element(*locator).send_keys(value) 
