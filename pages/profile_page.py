from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators
import allure


class ProfilePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажимаем История заказов')
    def click_orders_link(self):
        return self.click(ProfileLocators.ORDERS_HISTORY)

    @allure.step('Нажимаем Выход')
    def click_logout_button(self):
        return self.click(ProfileLocators.LOGOUT_BUTTON)

    @allure.step('Получаем список заказов')
    def get_order_items(self):
        return self.find_elements(ProfileLocators.ORDER_ITEM)
