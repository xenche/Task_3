from pages.base_page import BasePage
from locators.orders_feed_locators import OrdersFeedLocators
from locators.common_locators import CommonLocators
import allure


class OrdersFeedPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу Лента заказов по URL')
    def open(self):
        super().open("/feed")
        self.wait_for_url_contains("/feed")

    @allure.step('Открываем страницу Лента заказов по URL после создания заказа')
    def open_after_order_created(self):
        self.open()
        self.wait_for_all_orders_ready_invisible()

    @allure.step('Получаем все карточки заказов')
    def get_order_cards(self):
        return self.find_elements(OrdersFeedLocators.ORDER_CARDS)

    @allure.step('Кликаем по карточке заказа')
    def click_order_card(self):
        return self.click(OrdersFeedLocators.ORDER_CARD)

    @allure.step('Получаем номера заказов из карточек')
    def get_order_numbers(self):
        self.wait_for_element_invisible(CommonLocators.LOADING_OVERLAY)
        order_cards = self.find_elements(OrdersFeedLocators.ORDER_CARDS)
        order_numbers = []
        for card in order_cards:
            try:
                number_elem = card.find_element(*OrdersFeedLocators.ORDER_NUMBER)
                order_numbers.append(number_elem.text)
            except:
                pass
        return order_numbers

    @allure.step('Проверяем, видима ли модалка заказа')
    def is_order_modal_visible(self):
        return self.is_element_visible(OrdersFeedLocators.ORDER_MODAL)

    @allure.step('Получаем все выполненные заказы')
    def get_orders_done_total(self):
        self.wait_for_element_invisible(CommonLocators.LOADING_OVERLAY)
        return self.get_text(OrdersFeedLocators.ORDERS_DONE_TOTAL)

    @allure.step('Получаем все выполненные заказы за сегодня')
    def get_orders_done_today(self):
        self.wait_for_element_invisible(CommonLocators.LOADING_OVERLAY)
        return self.get_text(OrdersFeedLocators.ORDERS_DONE_TODAY)

    @allure.step('Получаем заказы в работе')
    def get_orders_in_progress(self):
        self.wait_for_element_invisible(CommonLocators.LOADING_OVERLAY)
        return self.get_text(OrdersFeedLocators.ORDERS_IN_PROGRESS)

    @allure.step('Ждем не отображения Все заказы готовы')
    def wait_for_all_orders_ready_invisible(self):
        return self.wait_for_element_invisible(OrdersFeedLocators.ALL_ORDERS_READY)
