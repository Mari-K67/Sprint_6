from .base_for_pages import BaseForPages
from locators.make_oder_locators import MakeOderLocators as mol
from selenium.webdriver.common.by import By

class MakeOder(BaseForPages):
    def __init__(self, driver):
        self.driver = driver
    
    #заполнить первую часть формы заказа
    def first_oder_blank_fill(self, name, surname, adress,metro_station, phone_number):
        #Заполнить поле Имя
        self.send_keys(mol.name_field, name)
        #Заполнить поле Фамилия
        self.send_keys(mol.surname_field, surname)
        #Заполнить поле Адрес
        self.send_keys(mol.adress_field, adress)
        #Заполнить поле Станция метро
        self.click(mol.metro_station_field)
        metro_station_locator = (By.XPATH, f".//div[@class='select-search__select']//button[contains(., '{metro_station}')]")
        self.click(metro_station_locator)
        #Заполнить поле телефон
        self.send_keys(mol.phone_number_field, phone_number)

    #заполнить вторую часть формы заказа
    def second_oder_blank_fill(self, date, rental_period, color):
        #Заполнить поле Срок аренды
        self.click(mol.rental_period_field)
        self.click((By.XPATH, f"//div[contains(text(), '{rental_period}')]")) 
        #Заполнить поле Когда привезти
        self.send_keys(mol.when_bring_field, date)
        #Выбрать цвет
        self.click(color) 

        