from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/forgot-password']")
