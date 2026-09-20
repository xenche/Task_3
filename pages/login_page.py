from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from locators.common_locators import CommonLocators
import allure


class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу логина по URL')
    def open(self):
        return super().open("/login")

    @allure.step('Вводим емейл')
    def enter_email(self, email):
        return self.input_text(LoginLocators.LOGIN_EMAIL_INPUT, email)

    @allure.step('Вводим пароль')
    def enter_password(self, password):
        return self.input_text(LoginLocators.LOGIN_PASSWORD_INPUT, password)

    @allure.step('Нажимаем кнопку "Войти"')
    def click_login_button(self):
        return self.click(LoginLocators.LOGIN_BUTTON)

    @allure.step('Нажимаем "Восстановить пароль"')
    def click_forgot_password_link(self):
        self.click(LoginLocators.FORGOT_PASSWORD_LINK)
        self.wait_for_url_contains("/forgot-password")

    @allure.step('Заполняем форму логина и входим')
    def login(self, email, password):
        self.wait_for_element_invisible(CommonLocators.LOADING_OVERLAY)
        self.enter_email(email)
        self.enter_password(password)
        self.wait_for_element_clickable(LoginLocators.LOGIN_BUTTON)
        self.click_login_button()
        self.wait_for_element_invisible(CommonLocators.LOADING_OVERLAY)

    @allure.step('Нажимаем "Конструктор"')
    def click_constructor_button(self):
        return self.click(CommonLocators.CONSTRUCTOR_BUTTON)
