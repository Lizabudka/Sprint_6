from selenium.webdriver.common.by import By


class MainPageLocators:
    order_button = [[By.XPATH, './/*[@class="Button_Button__ra12g" and text()="Заказать"]'],
                    [By.XPATH, './/*[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]']]
    questions_locators = [[By.ID, 'accordion__heading-0'],
                          [By.ID, 'accordion__heading-1'],
                          [By.ID, 'accordion__heading-2'],
                          [By.ID, 'accordion__heading-3'],
                          [By.ID, 'accordion__heading-4'],
                          [By.ID, 'accordion__heading-5'],
                          [By.ID, 'accordion__heading-6'],
                          [By.ID, 'accordion__heading-7']]
    answers_locators = [[By.ID, 'accordion__panel-0'],
                        [By.ID, 'accordion__panel-1'],
                        [By.ID, 'accordion__panel-2'],
                        [By.ID, 'accordion__panel-3'],
                        [By.ID, 'accordion__panel-4'],
                        [By.ID, 'accordion__panel-5'],
                        [By.ID, 'accordion__panel-6'],
                        [By.ID, 'accordion__panel-7']]


class OrderPageLocators:
    # локаторы первой формы заполнения заказа
    name_field = [By.XPATH, './/input[@placeholder="* Имя"]']
    surname_field = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    address_field = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_station_field = [By.XPATH, './/input[@placeholder="* Станция метро"]']
    phone_number_field = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']
    next_button = [By.XPATH, './/button[text()="Далее"]']

    # локаторы второй формы заполнения заказа
    metro_example = [[By.XPATH, './/*[text()="Черкизовская"]'],
                     [By.XPATH, './/*[text()="Бульвар Рокоссовского"]']]
    date_field = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    date_next_month_button = [By.XPATH, './/button[@aria-label="Next Month"]']
    date_day_to_choose = [By.XPATH, './/div[@class="react-datepicker__week"][1]/div[7]']
    term_field = [By.XPATH, './/*[text()="* Срок аренды"]']
    term_example_field = [By.XPATH, './/div[@class="Dropdown-menu"]/div[1]']
    colour_field = [[By.XPATH, './/*[text()="чёрный жемчуг"]'],
                    [By.XPATH, './/*[text()="серая безысходность"]']]
    comment_field = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']
    form_order_button = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']

    # локаторы всплывающих оуон
    order_header = [By.XPATH, './/*[text()="Про аренду"]']
    confirm_window = [By.XPATH, './/*[text()="Хотите оформить заказ?"]']
    button_yes = [By.XPATH, './/button[text()="Да"]']
    order_is_confirmed_window = [By.XPATH, './/div[text()="Заказ оформлен"]']


class CommonLocators:
    cookie_button = [By.XPATH, './/*[text()="да все привыкли"]']
    logo_samokat = [By.XPATH, './/*[@alt="Scooter"]']
    logo_yandex = [By.XPATH, './/*[@alt="Yandex"]']
