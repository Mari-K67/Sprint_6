from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:

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

    #прокрутка страницы вниз
    def scroll_to_botton(self, driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #прокрутка до элемента
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    #ожидание открытия второго окна
    def waite_2_page(self):  
        WebDriverWait(self.driver, 10).until(ec.number_of_windows_to_be(2))

    #переключение на новую вкладку
    def go_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    #получение текущей ссылки
    def get_current_url(self):
        return self.driver.current_url