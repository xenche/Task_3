import pytest
from pages.orders_feed_page import OrdersFeedPage
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
import allure


class TestOrdersFeed:

    @allure.title('Проверка открытия модалки заказа')
    @allure.description('Тест проверяет открытие модалки заказа в Ленте заказов')
    def test_order_modal_opens_on_click(self, browser):
        orders_feed_page = OrdersFeedPage(browser)
        orders_feed_page.open()
        orders_feed_page.click_order_card()
        assert orders_feed_page.is_order_modal_visible()

    @allure.title('Проверка отображения заказов юзера в ленте заказов')
    @allure.description('Тест проверяет отображение заказов юзера на странице Ленты зказов')
    def test_user_orders_appear_in_feed(self, browser, test_user):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login(test_user["email"], test_user["password"])
        constructor_page = ConstructorPage(browser)
        ingredients = constructor_page.get_ingredient_items()
        first_ingredient = ingredients[0]
        ingredient_target = constructor_page.find_ingredient_target()
        constructor_page.move_ingredient(first_ingredient, ingredient_target)
        constructor_page.click_order_button()
        constructor_page.close_order_modal()
        constructor_page.click_profile_button()
        profile_page = ProfilePage(browser)
        profile_page.click_orders_link()
        profile_order_numbers = profile_page.get_order_numbers()
        orders_feed_page = OrdersFeedPage(browser)
        orders_feed_page.open()
        constructor_page.open()
        orders_feed_page.open()
        feed_order_numbers = orders_feed_page.get_order_numbers()
        profile_set = set(profile_order_numbers)
        feed_set = set(feed_order_numbers)
        common_orders = profile_set.intersection(feed_set)
        assert common_orders, f"Нет общих заказов! Profile: {profile_order_numbers}, Feed: {feed_order_numbers}"

    @allure.title('Проверка увеличения "Выполнено за все время" при создании заказа')
    @allure.description('Тест проверяет увеличение количества заказов в "Выполнено за все время" после создания заказа')
    def test_orders_done_total_counter_increases(self, browser, test_user):
        orders_feed_page = OrdersFeedPage(browser)
        orders_feed_page.open()
        initial_total = int(orders_feed_page.get_orders_done_total())
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login(test_user["email"], test_user["password"])
        constructor_page = ConstructorPage(browser)
        ingredients = constructor_page.get_ingredient_items()
        first_ingredient = ingredients[0]
        ingredient_target = constructor_page.find_ingredient_target()
        constructor_page.move_ingredient(first_ingredient, ingredient_target)
        constructor_page.click_order_button()
        constructor_page.close_order_modal()
        orders_feed_page.open()
        new_total = int(orders_feed_page.get_orders_done_total())
        assert new_total > initial_total

    @allure.title('Проверка увеличения "Выполнено за сегодня" при создании заказа')
    @allure.description('Тест проверяет увеличение количества заказов в "Выполнено за сегодня" после создания заказа')
    def test_orders_done_today_counter_increases(self, browser, test_user):
        orders_feed_page = OrdersFeedPage(browser)
        orders_feed_page.open()
        initial_today = int(orders_feed_page.get_orders_done_today())
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login(test_user["email"], test_user["password"])
        constructor_page = ConstructorPage(browser)
        ingredients = constructor_page.get_ingredient_items()
        first_ingredient = ingredients[0]
        ingredient_target = constructor_page.find_ingredient_target()
        constructor_page.move_ingredient(first_ingredient, ingredient_target)
        constructor_page.click_order_button()
        constructor_page.close_order_modal()
        orders_feed_page.open()
        constructor_page.open()
        orders_feed_page.open()
        new_today = int(orders_feed_page.get_orders_done_today())
        assert new_today > initial_today

    @allure.title('Проверка отображения номера заказа в "В работе"')
    @allure.description('Тест проверяет отображение номера нового заказа в блоке "В работе"')
    def test_new_order_number_appears_in_work_section(self, browser, test_user):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login(test_user["email"], test_user["password"])
        constructor_page = ConstructorPage(browser)
        ingredients = constructor_page.get_ingredient_items()
        first_ingredient = ingredients[0]
        ingredient_target = constructor_page.find_ingredient_target()
        constructor_page.move_ingredient(first_ingredient, ingredient_target)
        constructor_page.click_order_button()
        new_order_number = constructor_page.get_order_number()
        constructor_page.close_order_modal() 
        orders_feed_page = OrdersFeedPage(browser)
        orders_feed_page.open_after_order_created()
        constructor_page.open()
        orders_feed_page.open_after_order_created()
        order_in_progress = orders_feed_page.get_orders_in_progress()
        assert new_order_number in order_in_progress
