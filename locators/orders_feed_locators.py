from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    ORDER_CARD = (By.CSS_SELECTOR, ".OrderHistory_orderCard__5j7Tw")
    ORDER_MODAL = (By.CSS_SELECTOR, ".Modal_modal__contentBox__sCy8X.pt-30.pb-30")
    ORDER_MODAL_CLOSE = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]//div[contains(@class, 'Modal_orderBox__1xWdi')]/ancestor::div//button[contains(@class, 'Modal_modal__close__TnseK')]")
    ORDERS_DONE_TOTAL = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDERS_DONE_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDERS_IN_PROGRESS = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi")
    ALL_ORDERS_READY = (By.XPATH, "//li[contains(text(), 'Все текущие заказы готовы')]")
