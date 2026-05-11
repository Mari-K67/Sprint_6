import pytest
import allure
from pages.make_oder_page import MakeOderPage
from locators.make_oder_locators import MakeOderLocators
import data
#python -m pytest tests/test_make_oder1.py

class TestQuestions:
    @allure.title('Успешное оформление заказа через верхнюю кнопку')
    @pytest.mark.parametrize("name, surname, adress, metro_station, phone_number, date, rental_period, color", [
       (data.name_1, data.surname_1, data.adress_1, data.metro_station_1, data.phone_number_1, data.date_1, data.rental_period_1, MakeOderLocators.black)
       ])
    def test_make_oder_top_order_button(self, driver, name, surname, adress, metro_station, phone_number, date, rental_period, color):
        page = MakeOderPage(driver)

        with allure.step('1. кликнуть на кнопку заказать'):
            page.click(MakeOderLocators.oder_button_top)
        
        with allure.step('2. заполнить первую часть формы заказа'):
            page.first_oder_blank_fill(name, surname, adress, metro_station, phone_number)

        with allure.step('3. кликнуть на кнопку Далее'):
            page.click(MakeOderLocators.next_button)

        with allure.step('4. заполнить вторую часть формы заказа'):
            page.second_oder_blank_fill(date, rental_period, color)

        with allure.step('5. кликнуть на кнопку Заказать'): 
            page.click(MakeOderLocators.oder_button_lower)

        with allure.step('6.кликнуть на кнопку Да'):
            page.click(MakeOderLocators.yes_button)

        with allure.step('7.проверить, что появилось всплывающее окно с сообщением об успешном создании заказа'):
            assert page.is_displayed(MakeOderLocators.successful_order)
    
    @allure.title('Успешное оформление заказа через нижнюю кнопку')
    @pytest.mark.parametrize("name, surname, adress, metro_station, phone_number, date, rental_period, color", [
       (data.name_2, data.surname_2, data.adress_2, data.metro_station_2, data.phone_number_2, data.date_2, data.rental_period_2, MakeOderLocators.grey)
       ])
    def test_make_oder_bottom_order_button(self, driver, name, surname, adress, metro_station, phone_number, date, rental_period, color):
        page = MakeOderPage(driver)

        with allure.step('1. прокрутка страницы'):
            page.scroll_to_element(MakeOderLocators.oder_button_bottom)

        with allure.step('2. кликнуть на кнопку заказать'):
            page.click(MakeOderLocators.oder_button_bottom)
        
        with allure.step('3. заполнить первую часть формы заказа'):
            page.first_oder_blank_fill(name, surname, adress, metro_station, phone_number)

        with allure.step('4. кликнуть на кнопку Далее'):
            page.click(MakeOderLocators.next_button)

        with allure.step('5. заполнить вторую часть формы заказа'):
            page.second_oder_blank_fill(date, rental_period, color)

        with allure.step('6. кликнуть на кнопку Заказать'): 
            page.click(MakeOderLocators.oder_button_lower)

        with allure.step('7.кликнуть на кнопку Да'):
            page.click(MakeOderLocators.yes_button)

        with allure.step('8.проверить, что появилось всплывающее окно с сообщением об успешном создании заказа'):
            assert page.is_displayed(MakeOderLocators.successful_order)