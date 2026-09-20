from selenium.webdriver.common.by import By


class ProfileLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='button' and text()='Выход']")
    ORDERS_HISTORY = (By.CSS_SELECTOR, "a[href='/account/order-history']")
    ORDER_NUMBER = (By.CSS_SELECTOR, "p.text_type_digits-default")
