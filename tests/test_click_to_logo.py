import pytest
from pages.base_for_pages import BaseForPages 
from locators.click_to_logo_locators import LogoLocators as ll
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import data

#python -m pytest tests/test_click_to_logo.py

class TestQuestions:
    def test_click_to_yandex_logo(self, driver):
        page = BaseForPages(driver)
        
        #кликнуть на логотип Яндекс
        page.click(ll.yandex_logo)

        #ожидание открытия вкладки 
        WebDriverWait(driver, 10).until(ec.number_of_windows_to_be(2))

        # Переключение на новую вкладку
        driver.switch_to.window(driver.window_handles[1])

        #ожидание загрузки
        WebDriverWait(driver, 10).until(ec.url_to_be(data.url_dzen))

        #проверить, что произошел переход на главную страницу Дзена(не переходит...)
        assert data.url_dzen == driver.current_url

    def test_click_to_scooter_logo(self, driver):
        page = BaseForPages(driver)

        #кликнуть на кнопку "Заказать", чтобы уйти с главной страницы
        page.click(ll.oder_button)

        #кликнуть на логотип Самокат
        page.click(ll.scooter_logo)

        #проверить, что произошел переход на главную страницу Самоката
        assert driver.current_url == "https://qa-scooter.education-services.ru/"
