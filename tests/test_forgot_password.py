import pytest
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
import allure


class TestPasswordRecovery:

    @allure.title('Проверка перехода на страницу восстановления пароля через "Восстановить пароль"')
    @allure.description('Тест проверяет переход на страницу восстановления пароля со страницы логина нажатием на кнопку "Восстановить пароль"')
    def test_navigate_to_forgot_password_from_login_page(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.click_forgot_password_link()
        assert "/forgot-password" in browser.current_url

    @allure.title('Проверка ввода пароля и нажатия "Восстановить"')
    @allure.description('Тест проверяет ввод пароля и нажатие на кнопку "Восстановить')
    def test_enter_email_and_click_recover(self, browser):
        forgot_page = ForgotPasswordPage(browser)
        forgot_page.open()
        test_email = "test@example.com"
        forgot_page.enter_email(test_email)
        forgot_page.click_recover_button()
        assert "/reset-password" in browser.current_url

    @allure.title('Проверка подсветки поля пароля при нажатии тоггла')
    @allure.description('Тест проверяет появление подсветки и активации поля пароля при нажатии тоггла ')
    def test_show_hide_password_toggle_activates_field(self, browser):
        forgot_page = ForgotPasswordPage(browser)
        forgot_page.open()
        test_email = "test@example.com"
        forgot_page.enter_email(test_email)
        forgot_page.click_recover_button()
        forgot_page.click_show_password_toggle()
        assert forgot_page.is_pw_input_focused()
