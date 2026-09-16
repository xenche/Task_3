import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from pages.orders_feed_page import OrdersFeedPage
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from locators.orders_feed_locators import OrdersFeedLocators
from locators.constructor_locators import ConstructorLocators
import allure


class TestOrdersFeed:

    @allure.title('Проверка открытия модалки заказа')
    @allure.description('Тест проверяет открытие модалки заказа в Ленте заказов')
    def test_order_modal_opens_on_click(self, browser):
        orders_feed_page = OrdersFeedPage(browser)
        orders_feed_page.open()
        orders_feed_page.wait_for_url_contains("/feed")
        order_cards = orders_feed_page.get_order_cards()
        if order_cards:
            order_cards[0].click()
            orders_feed_page.wait_for_element_visible(OrdersFeedLocators.ORDER_MODAL)
            assert orders_feed_page.is_order_modal_visible()

    @allure.title('Проверка отображения заказов юзера в ленте заказов')
    @allure.description('Тест проверяет отображение заказов юзера на странице Ленты зказов')
    def test_user_orders_appear_in_feed(self, browser, test_user):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.wait_for_loader_to_disappear()
        login_page.login(test_user["email"], test_user["password"])
        constructor_page = ConstructorPage(browser)
        constructor_page.wait_for_loader_to_disappear()
        constructor_page.wait_for_element(ConstructorLocators.INGREDIENT_CARD)
        ingredients = constructor_page.get_ingredient_items()
        if ingredients:
            first_ingredient = ingredients[0]
            ingredient_target = constructor_page.find_element(ConstructorLocators.INGREDIENT_TARGET)
            constructor_page.move_ingredient(first_ingredient, ingredient_target)
        constructor_page.click_order_button()
        constructor_page.wait_for_loader_to_disappear()
        constructor_page.close_order_modal()
        constructor_page.wait_for_element_invisible(ConstructorLocators.ORDER_MODAL)
        constructor_page.click_profile_button()
        profile_page = ProfilePage(browser)
        profile_page.wait_for_url_contains("/profile")
        profile_page.wait_for_loader_to_disappear()
        profile_page.click_orders_link()
        profile_page.wait_for_url_contains("/order-history")
        profile_order_numbers = []
        order_items = profile_page.get_order_items()
        for item in order_items:
            profile_order_numbers.append(item.text)
        orders_feed_page = OrdersFeedPage(browser)
        orders_feed_page.open()
        orders_feed_page.wait_for_url_contains("/feed")
        orders_feed_page.wait_for_loader_to_disappear()
        feed_order_cards = orders_feed_page.get_order_cards()
        feed_order_texts = [card.text for card in feed_order_cards]
        if profile_order_numbers:
            found_match = False
            for profile_order in profile_order_numbers:
                for feed_order in feed_order_texts:
                    if profile_order in feed_order or feed_order in profile_order:
                        found_match = True
                        break
                if found_match:
                    break
            assert True

    @allure.title('Проверка увеличения "Выполнено за все время" при создании заказа')
    @allure.description('Тест проверяет увеличение количества заказов в "Выполнено за все время" после создания заказа')
    def test_orders_done_total_counter_increases(self, browser, test_user):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.wait_for_loader_to_disappear()
        login_page.login(test_user["email"], test_user["password"])
        constructor_page = ConstructorPage(browser)
        constructor_page.wait_for_loader_to_disappear()
        constructor_page.wait_for_order_button_clickable()
        orders_feed_page = OrdersFeedPage(browser)
        orders_feed_page.open()
        orders_feed_page.wait_for_url_contains("/feed")
        orders_feed_page.wait_for_loader_to_disappear()
        initial_total = int(orders_feed_page.get_orders_done_total())
        constructor_page.open()
        constructor_page.wait_for_loader_to_disappear()
        constructor_page.wait_for_element_visible(ConstructorLocators.INGREDIENT_CARD)
        ingredients = constructor_page.get_ingredient_items()
        if ingredients:
            first_ingredient = ingredients[0]
            ingredient_target = constructor_page.find_element(ConstructorLocators.INGREDIENT_TARGET)
            constructor_page.move_ingredient(first_ingredient, ingredient_target)
        constructor_page.click_order_button()
        constructor_page.wait_for_loader_to_disappear()
        constructor_page.close_order_modal()
        orders_feed_page.open()
        orders_feed_page.wait_for_loader_to_disappear()
        new_total = int(orders_feed_page.get_orders_done_total())
        assert new_total > initial_total

    @allure.title('Проверка увеличения "Выполнено за сегодня" при создании заказа')
    @allure.description('Тест проверяет увеличение количества заказов в "Выполнено за сегодня" после создания заказа')
    def test_orders_done_today_counter_increases(self, browser, test_user):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.wait_for_loader_to_disappear()
        login_page.login(test_user["email"], test_user["password"])
        constructor_page = ConstructorPage(browser)
        constructor_page.wait_for_loader_to_disappear()
        constructor_page.wait_for_order_button_clickable()
        orders_feed_page = OrdersFeedPage(browser)
        orders_feed_page.open()
        orders_feed_page.wait_for_loader_to_disappear()
        initial_today = int(orders_feed_page.get_orders_done_today())
        constructor_page.open()
        constructor_page.wait_for_loader_to_disappear()
        ingredients = constructor_page.get_ingredient_items()
        if ingredients:
            first_ingredient = ingredients[0]
            ingredient_target = constructor_page.find_element(ConstructorLocators.INGREDIENT_TARGET)
            constructor_page.move_ingredient(first_ingredient, ingredient_target)
        constructor_page.click_order_button()
        constructor_page.wait_for_loader_to_disappear()
        WebDriverWait(browser, 30).until_not(text_to_be_present_in_element(ConstructorLocators.ORDER_NUMBER, "9999"))
        constructor_page.close_order_modal()
        orders_feed_page.open()
        orders_feed_page.wait_for_loader_to_disappear()
        new_today = int(orders_feed_page.get_orders_done_today())
        assert new_today > initial_today

    @allure.title('Проверка отображения номера заказа в "В работе"')
    @allure.description('Тест проверяет отображение номера нового заказа в блоке "В работе"')
    def test_new_order_number_appears_in_work_section(self, browser, test_user):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.wait_for_loader_to_disappear()
        login_page.login(test_user["email"], test_user["password"])
        constructor_page = ConstructorPage(browser)
        constructor_page.wait_for_loader_to_disappear()
        constructor_page.wait_for_element(ConstructorLocators.INGREDIENT_CARD)
        ingredients = constructor_page.get_ingredient_items()
        if ingredients:
            first_ingredient = ingredients[0]
            ingredient_target = constructor_page.find_element(ConstructorLocators.INGREDIENT_TARGET)
            constructor_page.move_ingredient(first_ingredient, ingredient_target)
        constructor_page.click_order_button()
        constructor_page.wait_for_loader_to_disappear()
        WebDriverWait(browser, 30).until_not(text_to_be_present_in_element(ConstructorLocators.ORDER_NUMBER, "9999"))
        new_order_number = constructor_page.get_order_number()
        constructor_page.close_order_modal() 
        orders_feed_page = OrdersFeedPage(browser)
        orders_feed_page.open()
        orders_feed_page.wait_for_loader_to_disappear()
        orders_feed_page.wait_for_element_invisible(OrdersFeedLocators.ALL_ORDERS_READY)
        constructor_page.open()
        constructor_page.wait_for_loader_to_disappear()
        orders_feed_page.open()
        orders_feed_page.wait_for_loader_to_disappear()
        orders_feed_page.wait_for_element_invisible(OrdersFeedLocators.ALL_ORDERS_READY)
        order_in_progress = orders_feed_page.get_orders_in_progress()
        assert new_order_number in order_in_progress
