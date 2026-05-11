import pytest
import allure
from pages.click_to_logo_page import ClickToLogoPage
from pages.base_page import BasePage
from locators.click_to_logo_locators import LogoLocators 
import data
#python -m pytest tests/test_click_to_logo.py

class TestQuestions:
    @allure.title('Переход на страницу Яндекс Дзен при клике на лого Яндекса')
    def test_click_to_yandex_logo(self, driver):
        page = ClickToLogoPage(driver)
        
        with allure.step('1. кликнуть на логотип Яндекс'):
            page.click_with_wait(LogoLocators.yandex_logo)

        with allure.step('2. переключение на новую вкладку'):
            page.go_to_new_window()

        with allure.step('3. проверить, что произошел переход на главную страницу Дзена'):
            assert data.url_dzen == driver.current_url

    @allure.title('Переход на страницу главную страницу Самоката при клике на лого Самокат')
    def test_click_to_scooter_logo(self, driver):
        page = BasePage(driver)

        with allure.step('1. кликнуть на кнопку "Заказать", чтобы уйти с главной страницы'):
            page.click(LogoLocators.oder_button)

        with allure.step('2. кликнуть на логотип Самокат'):
            page.click(LogoLocators.scooter_logo)

        with allure.step('3. проверить, что произошел переход на главную страницу Самоката'):
            assert driver.current_url == data.url
