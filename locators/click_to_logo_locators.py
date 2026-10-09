from selenium.webdriver.common.by import By

class LogoLocators:
    yandex_logo = (By.XPATH, "//img[@alt='Yandex']")
    scooter_logo = (By.XPATH, "//img[@alt='Scooter']")
    oder_button = (By.XPATH, ".//button[text()='Заказать']")