import pytest
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.constructor_page import ConstructorPage
import allure


class TestProfile:

    @allure.title('Проверка перехода в профиль кликом на кнопку "Личный кабинет"')
    @allure.description('Тест проверяет переход в профиль через клик на кнопку "Личный кабинет"')
    def test_navigate_to_profile_by_clicking_profile_button(self, browser, test_user):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.wait_for_loader_to_disappear()
        login_page.login(test_user["email"], test_user["password"])
        constructor_page = ConstructorPage(browser)
        constructor_page.wait_for_loader_to_disappear()
        constructor_page.click_profile_button()
        profile_page = ProfilePage(browser)
        profile_page.wait_for_url_contains("/profile")
        assert "/profile" in browser.current_url

    @allure.title('Проверка перехода в Историю заказов')
    @allure.description('Тест проверяет переход в историю заказов из профиля')
    def test_navigate_to_orders_history_from_profile(self, browser, test_user):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.wait_for_loader_to_disappear()
        login_page.login(test_user["email"], test_user["password"])
        constructor_page = ConstructorPage(browser)
        constructor_page.wait_for_loader_to_disappear()
        constructor_page.click_profile_button()
        profile_page = ProfilePage(browser)
        profile_page.wait_for_url_contains("/profile")
        profile_page = ProfilePage(browser)
        constructor_page.wait_for_loader_to_disappear()
        profile_page.click_orders_link()
        profile_page.wait_for_url_contains("/order-history")
        assert "/order-history" in browser.current_url

    @allure.title('Проверка разлогина')
    @allure.description('Тест проверяет разлогин из профиля через кнопку "Выход""')
    def test_logout_from_account(self, browser, test_user):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.wait_for_loader_to_disappear()
        login_page.login(test_user["email"], test_user["password"])
        constructor_page = ConstructorPage(browser)
        constructor_page.wait_for_loader_to_disappear()
        constructor_page.click_profile_button()
        profile_page = ProfilePage(browser)
        profile_page.wait_for_url_contains("/profile")
        profile_page.wait_for_loader_to_disappear()
        profile_page.click_logout_button()
        login_page.wait_for_url_contains("/login")
        assert "/login" in browser.current_url
