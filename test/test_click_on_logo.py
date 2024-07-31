from pages.main_page import MainPageScooterService
from pages.order_form_page import OrderFormPage
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pages.variables
from pages.objects_locators import *


class TestLogoClick:

    @allure.title('Проверка перехода на главную страницу через клик по лого "Самокат"')
    def test_click_on_samokat_logo_go_to_main_page(self, driver):
        order_page = OrderFormPage(driver)

        # Переход на страницу с формой заказа
        order_page.go_to_main_page()
        order_page.wait_element_to_be_visible(OrderPageLocators.name_field[0], OrderPageLocators.name_field[1])

        # Клик на лого "Самокат"
        order_page.click_on_logo_samokat()
        current_url = driver.current_url

        with allure.step(f'Проверяем, что мы перешли на страницу {pages.variables.MAIN_PAGE_URL}'):
            assert current_url == pages.variables.MAIN_PAGE_URL

    @allure.title('Проверка перехода на сайт Дзен через клик по лого "Яндекс"')
    def test_click_on_yandex_logo_go_to_dzen_page(self, driver):
        main_page = MainPageScooterService(driver)

        # Переход на главную страницу сайта
        main_page.go_to_main_page()
        element = driver.find_element(*CommonLocators.logo_yandex)
        main_page.check_if_element_is_clickable(element, CommonLocators.logo_yandex[0],
                                                CommonLocators.logo_yandex[1])

        # Клик на лого "Яндекс", проверка url
        driver.switch_to.window(driver.window_handles[1])

        with allure.step(f'Проверяем, что мы перешли на  страницу {pages.variables.DZEN_PAGE_URL}'):
            assert WebDriverWait(driver, 3).until(
                expected_conditions.url_to_be(pages.variables.DZEN_PAGE_URL))
