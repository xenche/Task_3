from selenium.webdriver.common.by import By


class ConstructorLocators:

    INGREDIENT_CARD = (By.XPATH, "//a[@href='/ingredient/691577430cc94f001a65b859']")
    INGREDIENT_TARGET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']")
    INGREDIENT_COUNTER = (By.XPATH, "//a[@href='/ingredient/691577430cc94f001a65b859']//p[contains(@class, 'counter_counter__num__3nue1')]")
    INGREDIENT_MODAL = (By.CSS_SELECTOR, ".Modal_modal__contentBox__sCy8X.pt-10.pb-15")
    INGREDIENT_MODAL_CLOSE = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]/ancestor::div//button[contains(@class, 'Modal_modal__close__TnseK')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (By.CSS_SELECTOR, ".Modal_modal__contentBox__sCy8X.pt-30.pb-30")
    ORDER_NUMBER = (By.CSS_SELECTOR, ".Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8")
    ORDER_MODAL_CLOSE = (By.XPATH, "//p[contains(text(), 'Ваш заказ начали готовить')]/ancestor::div//button[contains(@class, 'Modal_modal__close__TnseK')]")
