import pytest
from pages.make_oder import MakeOder as mo
from pages.base_for_pages import BaseForPages as bfp
from locators.make_oder_locators import MakeOderLocators as mol
#python -m pytest tests/test_make_oder.py

class TestQuestions:

    @pytest.mark.parametrize("name, surname, adress, metro_station, phone_number, date, rental_period, color", [
       ('Иван', 'Васечкин', 'Твардовского 1', 'Черкизовская', '89169677891', '15.05.2026', 'трое суток', mol.black),
       ('Алена', 'Кирова', 'Правды 26', 'Сокольники', '89168965891', '20.05.2026', 'двое суток', mol.grey)
       ])
    def test_make_oder(self, driver, name, surname, adress, metro_station, phone_number, date, rental_period, color):
        main_page = bfp(driver)
        oder_page = mo(driver)

        #кликнуть на кнопку заказать
        main_page.click(mol.oder_button)
        
        #заполнить первую часть формы заказа
        oder_page.first_oder_blank_fill(name, surname, adress, metro_station, phone_number)

        #кликнуть на кнопку Далее
        oder_page.click(mol.next_button)

        #заполнить вторую часть формы заказа
        oder_page.second_oder_blank_fill(date, rental_period, color)

        #кликнуть на кнопку Заказать 
        oder_page.click(mol.oder_button_lower)

        #кликнуть на кнопку Да
        oder_page.click(mol.yes_button)

        #проверить, что появилось всплывающее окно с сообщением об успешном создании заказа
        assert oder_page.is_displayed(mol.successful_order)
