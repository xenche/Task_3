from pages.base_page import BasePage
from locators.orders_feed_locators import OrdersFeedLocators
import allure


class OrdersFeedPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу Лента заказов по URL')
    def open(self):
        return super().open("/feed")

    @allure.step('Получаем все карточки заказов')
    def get_order_cards(self):
        return self.find_elements(OrdersFeedLocators.ORDER_CARD)

    @allure.step('Проверяем, видима ли модалка заказа')
    def is_order_modal_visible(self):
        return self.is_element_visible(OrdersFeedLocators.ORDER_MODAL)

    @allure.step('Получаем все выполненные заказы')
    def get_orders_done_total(self):
        return self.get_text(OrdersFeedLocators.ORDERS_DONE_TOTAL)

    @allure.step('Получаем все выполненные заказы за сегодня')
    def get_orders_done_today(self):
        return self.get_text(OrdersFeedLocators.ORDERS_DONE_TODAY)

    @allure.step('Получаем заказы в работе')
    def get_orders_in_progress(self):
        return self.get_text(OrdersFeedLocators.ORDERS_IN_PROGRESS)
