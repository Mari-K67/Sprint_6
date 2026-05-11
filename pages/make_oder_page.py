from .base_page import BasePage
from locators.make_oder_locators import MakeOderLocators

class MakeOderPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    
    #заполнить первую часть формы заказа
    def first_oder_blank_fill(self, name, surname, adress,metro_station, phone_number):
        #Заполнить поле Имя
        self.send_keys(MakeOderLocators.name_field, name)
        #Заполнить поле Фамилия
        self.send_keys(MakeOderLocators.surname_field, surname)
        #Заполнить поле Адрес
        self.send_keys(MakeOderLocators.adress_field, adress)
        #Заполнить поле Станция метро
        self.click(MakeOderLocators.metro_station_field)
        self.click(MakeOderLocators.metro_station_locator(metro_station))
        #Заполнить поле телефон
        self.send_keys(MakeOderLocators.phone_number_field, phone_number)

    #заполнить вторую часть формы заказа
    def second_oder_blank_fill(self, date, rental_period, color):
        #Заполнить поле Срок аренды
        self.click(MakeOderLocators.rental_period_field)
        self.click(MakeOderLocators.rental_period_locator(rental_period)) 
        #Заполнить поле Когда привезти
        self.send_keys(MakeOderLocators.when_bring_field, date)
        #Выбрать цвет
        self.click(color) 
     
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)