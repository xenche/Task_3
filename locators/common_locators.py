from selenium.webdriver.common.by import By


class CommonLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Лента Заказов']")
    PROFILE_BUTTON = (By.XPATH, "//a[@href='/account']")
    LOADING_OVERLAY = (By.CSS_SELECTOR, "img[alt='loading animation']")
