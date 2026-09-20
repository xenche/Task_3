from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    ORDER_CARD = (By.XPATH, "(//a[contains(@class, 'OrderHistory_link__1iNby')])[1]")
    ORDER_CARDS = (By.CSS_SELECTOR, "a.OrderHistory_link__1iNby")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default') and starts-with(text(), '#')]")
    ORDER_MODAL = (By.CSS_SELECTOR, "div.Modal_orderBox__1xWdi.Modal_modal__contentBox__sCy8X")
    ORDER_MODAL_CLOSE = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]//div[contains(@class, 'Modal_orderBox__1xWdi')]/ancestor::div//button[contains(@class, 'Modal_modal__close__TnseK')]")
    ORDERS_DONE_TOTAL = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDERS_DONE_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDERS_IN_PROGRESS = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi")
    ALL_ORDERS_READY = (By.XPATH, "//li[contains(text(), 'Все текущие заказы готовы')]")
