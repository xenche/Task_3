from selenium.webdriver.common.by import By


class ProfileLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='button' and text()='Выход']")
    ORDERS_HISTORY = (By.CSS_SELECTOR, "a[href='/account/order-history']")
    ORDER_ITEM = (By.CSS_SELECTOR, ".OrderHistory_link__1iNby")
