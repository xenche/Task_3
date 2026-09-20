from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators
from locators.common_locators import CommonLocators
import allure


class ProfilePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажимаем История заказов')
    def click_orders_link(self):
        self.click(ProfileLocators.ORDERS_HISTORY)
        self.wait_for_url_contains("/order-history")

    @allure.step('Нажимаем Выход')
    def click_logout_button(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)
        self.wait_for_url_contains("/login")

    @allure.step('Получаем номера заказов из истории')
    def get_order_numbers(self):
        self.wait_for_element_invisible(CommonLocators.LOADING_OVERLAY)
        self.wait_for_element(ProfileLocators.ORDER_NUMBER, timeout=15)
        order_numbers = []
        number_elements = self.find_elements(ProfileLocators.ORDER_NUMBER)
        for elem in number_elements:
            text = elem.text.strip()
            if text.startswith('#'):
                order_numbers.append(text)
        return order_numbers
