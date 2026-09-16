from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    FORGOT_EMAIL_INPUT = (By.CSS_SELECTOR, "input.input__textfield")
    FORGOT_RECOVER_BUTTON = (By.CSS_SELECTOR, "button.button_button_type_primary__1O7Bx")
    SHOW_PASSWORD_TOGGLE = (By.CSS_SELECTOR, "div.input__icon-action")
    PW_FOCUSED_INPUT = (By.CSS_SELECTOR, "label.input__placeholder-focused")
