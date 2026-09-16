import pytest
from pages.constructor_page import ConstructorPage
from pages.orders_feed_page import OrdersFeedPage
from pages.login_page import LoginPage
from locators.constructor_locators import ConstructorLocators
import allure
from data.urls import BASE_URL


class TestConstructorFunctionality:

    @allure.title('Проверка перехода в конструктор через кнопку "Конструктор"')
    @allure.description('Тест проверяет переход в конструктор кликом на кнопку "Конструктор"')
    def test_navigate_to_constructor_by_clicking_button(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.wait_for_loader_to_disappear()
        login_page.click_constructor_button()
        assert browser.current_url == f"{BASE_URL}/"

    @allure.title('Проверка перехода в ленту заказов через кнопку "Лента заказов"')
    @allure.description('Тест проверяет переход в ленту заказов кликом на кнопку "Лента заказов"')
    def test_navigate_to_feed_by_clicking_button(self, browser):
        constructor_page = ConstructorPage(browser)
        constructor_page.open()
        constructor_page.wait_for_loader_to_disappear()
        constructor_page.click_feed_button()
        orders_feed_page = OrdersFeedPage(browser)
        orders_feed_page.wait_for_url_contains("/feed")
        assert "/feed" in browser.current_url

    @allure.title('Проверка открытия модалки ингредиента')
    @allure.description('Тест проверяет открытие модалки ингредиента кликом на нее')
    def test_ingredient_modal_opens_on_click(self, browser):
        constructor_page = ConstructorPage(browser)
        constructor_page.open()
        constructor_page.wait_for_loader_to_disappear()
        ingredients = constructor_page.get_ingredient_items()
        if ingredients:
            first_ingredient = ingredients[0]
            first_ingredient.click()
            constructor_page.wait_for_ingredient_modal_visible()
            assert constructor_page.is_ingredient_modal_visible()

    @allure.title('Проверка закрытия модалки ингредиента')
    @allure.description('Тест проверяет закрытие модалки ингредиента кликом на крестик')
    def test_ingredient_modal_closes_on_x_button(self, browser):
        constructor_page = ConstructorPage(browser)
        constructor_page.open()
        constructor_page.wait_for_loader_to_disappear()
        ingredients = constructor_page.get_ingredient_items()
        if ingredients:
            ingredients[0].click()
            constructor_page.wait_for_ingredient_modal_visible()
            constructor_page.close_ingredient_modal()
            constructor_page.wait_for_element_invisible(ConstructorLocators.INGREDIENT_MODAL)
            assert not constructor_page.is_ingredient_modal_visible()

    @allure.title('Проверка увеличения каунтера ингредиента')
    @allure.description('Тест проверяет увеличение каунтера ингредиента при добавлении в заказ')
    def test_ingredient_counter_increases_on_add(self, browser):
        constructor_page = ConstructorPage(browser)
        constructor_page.open()
        constructor_page.wait_for_loader_to_disappear()
        ingredients = constructor_page.get_ingredient_items()
        if ingredients:
            first_ingredient = ingredients[0]
            counter_element = first_ingredient.find_element(*ConstructorLocators.INGREDIENT_COUNTER)
            counter_num = int(counter_element.text)
            ingredient_target = constructor_page.find_element(ConstructorLocators.INGREDIENT_TARGET)
            constructor_page.move_ingredient(first_ingredient, ingredient_target)
            counter_element_dropped = first_ingredient.find_element(*ConstructorLocators.INGREDIENT_COUNTER)
            counter_num_dropped = int(counter_element_dropped.text)
            assert counter_num_dropped == counter_num + 2

    @allure.title('Проверка оформления заказа авторизованным юзером')
    @allure.description('Тест проверяет, что авторизованный юзер может создать заказ')
    def test_logged_in_user_can_place_order(self, browser, test_user):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.wait_for_loader_to_disappear()
        login_page.login(test_user["email"], test_user["password"])
        constructor_page = ConstructorPage(browser)
        constructor_page.wait_for_loader_to_disappear()
        ingredients = constructor_page.get_ingredient_items()
        if ingredients:
            first_ingredient = ingredients[0]
            ingredient_target = constructor_page.find_element(ConstructorLocators.INGREDIENT_TARGET)
            constructor_page.move_ingredient(first_ingredient, ingredient_target)
        constructor_page.click_order_button()
        constructor_page.wait_for_element_visible(ConstructorLocators.ORDER_MODAL)
        constructor_page.wait_for_loader_to_disappear()
        assert constructor_page.is_order_modal_visible()
        assert constructor_page.order_number_visible()
