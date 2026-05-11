from selenium.webdriver.common.by import By

class MakeOderLocators:
    oder_button_top = (By.XPATH, ".//button[text()='Заказать']")
    oder_button_bottom = (By.XPATH, ".//button[text()='Заказать']")
    
    #для первой страницы оформления заказа 
    name_field = (By.XPATH, "//input[@placeholder='* Имя']")
    surname_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    adress_field =  (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

    @staticmethod
    def metro_station_locator(station_name: str):
        return (By.XPATH, f".//div[@class='select-search__select']//button[contains(., '{station_name}')]")
    
    metro_station_field = (By.XPATH, "//input[@placeholder='* Станция метро']")
    phone_number_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    
    next_button = (By.XPATH, ".//button[text()='Далее']")
    
    #для второй страницы оформлкния заказа
    when_bring_field = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rental_period_field = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    
    @staticmethod
    def rental_period_locator(rental_period: str):
        return (By.XPATH, f"//div[contains(text(), '{rental_period}')]")
    
    oder_button_lower = (By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    black = (By.ID, 'black')
    grey = (By.ID, 'grey')
    
    yes_button = (By.XPATH, ".//button[text()='Да']")

    #всплывающее окно с сообщением об успешном создании заказа
    successful_order = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]")

