from selenium.webdriver.common.by import By

class MakeOderLocators:
    oder_button = (By.XPATH, ".//button[text()='Заказать']")
    
    #для первой страницы оформления заказа 
    name_field = (By.XPATH, "//input[@placeholder='* Имя']")
    surname_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    adress_field =  (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_station_field = (By.XPATH, "//input[@placeholder='* Станция метро']")
    phone_number_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    
    next_button = (By.XPATH, ".//button[text()='Далее']")
    
    #для второй страницы оформлкния заказа
    when_bring_field = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rental_period_field = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    
    oder_button_lower = (By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    black = (By.ID, 'black')
    grey = (By.ID, 'grey')
    
    yes_button = (By.XPATH, ".//button[text()='Да']")

    #всплывающее окно с сообщением об успешном создании заказа
    successful_order = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]")

