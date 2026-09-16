from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators.common_locators import CommonLocators
from data.urls import BASE_URL
import allure


class BasePage:
    
    def __init__(self, driver, url=BASE_URL):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Открываем страницу по URL')
    def open(self, path=""):
        full_url = f"{self.url}{path}"
        self.driver.get(full_url)
        return self

    @allure.step('Находим элемент на странице')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Находим все элементы на странице')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Ждем появления элемента на странице')
    def wait_for_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    @allure.step('Ждем, пока элемент станет видимым')
    def wait_for_element_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ждем, пока элемент станет кликабельным')
    def wait_for_element_clickable(self, locator, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Ждем, пока элемент станет невидимым')
    def wait_for_element_invisible(self, locator, timeout=20):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element_located(locator))

    @allure.step('Кликаем по элементу')
    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        return element.click()

    @allure.step('Вводим текст')
    def input_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step('Проверяем, присутствует ли элемент на странице')
    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    @allure.step('Проверяем, виден ли элемент на странице')
    def is_element_visible(self, locator):
        try:
            element = self.wait_for_element_visible(locator, timeout=5)
            return element.is_displayed()
        except TimeoutException:
            return False
        
    @allure.step('Получаем актуальный URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ждем, пока в URL не появится текст')
    def wait_for_url_contains(self, substring, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.url_contains(substring))

    @allure.step('Ждем, пока лоадер исчезнет')
    def wait_for_loader_to_disappear(self):
        self.wait_for_element_invisible(CommonLocators.LOADING_OVERLAY)
    
