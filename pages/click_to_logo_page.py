from .base_page import BasePage

class ClickToLogoPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    #нажатие на лого с ожижанием 
    def click_with_wait(self, locator):
        self.click(locator)
        #ожидание открытия вкладки 
        self.waite_2_page()