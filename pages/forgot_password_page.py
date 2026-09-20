from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
import allure


class ForgotPasswordPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу восстановления пароля по URL')
    def open(self):
        return super().open("/forgot-password")

    @allure.step('Заполняем емейл в форме восстановления пароля')
    def enter_email(self, email):
        return self.input_text(ForgotPasswordLocators.FORGOT_EMAIL_INPUT, email)

    @allure.step('Нажимаем кнопку "Восстановить"')
    def click_recover_button(self):
        self.click(ForgotPasswordLocators.FORGOT_RECOVER_BUTTON)
        self.wait_for_url_contains("/reset-password")

    @allure.step('Нажимаем тоггл просмотра пароля')
    def click_show_password_toggle(self):
        self.click(ForgotPasswordLocators.SHOW_PASSWORD_TOGGLE)
        self.wait_pw_input_focused()

    @allure.step('Проверяем, что поле пароля подсвечено')
    def is_pw_input_focused(self):
        return self.is_element_present(ForgotPasswordLocators.PW_FOCUSED_INPUT)

    @allure.step('Проверяем, что поле пароля подсвечено')
    def wait_pw_input_focused(self):
        return self.wait_for_element(ForgotPasswordLocators.PW_FOCUSED_INPUT)
