from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators
from locators.common_locators import CommonLocators
import allure

class ConstructorPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу конструктора по URL')
    def open(self):
        return super().open("/")

    @allure.step('Нажимаем кнопку "Лента заказов"')
    def click_feed_button(self):
        self.click(CommonLocators.FEED_BUTTON)
        self.wait_for_url_contains("/feed")

    @allure.step('Нажимаем кнопку "Личный кбаинет"')
    def click_profile_button(self):
        self.wait_for_element_invisible(ConstructorLocators.ORDER_MODAL)
        self.click(CommonLocators.PROFILE_BUTTON)
        self.wait_for_url_contains("/profile")

    @allure.step('Получаем все ингредиенты')
    def get_ingredient_items(self):
        self.wait_for_element_invisible(CommonLocators.LOADING_OVERLAY)
        self.wait_for_element(ConstructorLocators.INGREDIENT_CARD)
        return self.find_elements(ConstructorLocators.INGREDIENT_CARD)

    @allure.step('Перемещаем ингредиенты в конктруктор')
    def move_ingredient(self, ingredient, target_area):
        script = """
        var source = arguments[0];
        var target = arguments[1];
        
        // Create dataTransfer object
        var dataTransfer = new DataTransfer();
        
        // Get the draggable element (anchor tag)
        var draggable = source;
        
        // Get the text/content to transfer
        var ingredientData = {
            _id: draggable.getAttribute('href').split('/')[2],
            type: 'ingredient'
        };
        dataTransfer.setData('application/json', JSON.stringify(ingredientData));
        dataTransfer.setData('text/plain', ingredientData._id);
        
        // Dispatch dragstart event
        var dragStartEvent = new DragEvent('dragstart', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        });
        draggable.dispatchEvent(dragStartEvent);
        
        // Dispatch dragover event on target (required for drop to work)
        var dragOverEvent = new DragEvent('dragover', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        });
        target.dispatchEvent(dragOverEvent);
        
        // Dispatch drop event on target
        var dropEvent = new DragEvent('drop', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        });
        target.dispatchEvent(dropEvent);
        
        // Dispatch dragend event
        var dragEndEvent = new DragEvent('dragend', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        });
        draggable.dispatchEvent(dragEndEvent);
        """
        self.execute_script(script, ingredient, target_area)
        self.wait_for_element_invisible(ConstructorLocators.INGREDIENT_TARGET, timeout=15)

    @allure.step('Проверяем, видна, ли модалка ингредиента"')
    def is_ingredient_modal_visible(self):
        return self.is_element_visible(ConstructorLocators.INGREDIENT_MODAL)

    @allure.step('Ждем, когда модалка ингредиента будет видна')
    def wait_for_ingredient_modal_visible(self):
        return self.wait_for_element_visible(ConstructorLocators.INGREDIENT_MODAL)

    @allure.step('Ждем, когда модалка ингредиента будет не видна')
    def wait_for_ingredient_modal_invisible(self):
            return self.wait_for_element_invisible(ConstructorLocators.INGREDIENT_MODAL)

    @allure.step('Закрываем модалку ингредиента')
    def close_ingredient_modal(self):
        self.wait_for_ingredient_modal_visible()
        self.click(ConstructorLocators.INGREDIENT_MODAL_CLOSE)
        self.wait_for_ingredient_modal_invisible()

    @allure.step('Нажимаем "Оформить заказ"')
    def click_order_button(self):
        self.click(ConstructorLocators.ORDER_BUTTON)
        self.wait_for_order_modal_visible()
        self.wait_fake_order_number_not_present()

    @allure.step('Закрываем модалку заказа')
    def close_order_modal(self):
        return self.click(ConstructorLocators.ORDER_MODAL_CLOSE)

    @allure.step('Ждем, когда модалка заказа будет видна')
    def wait_for_order_modal_visible(self):
        return self.wait_for_element_visible(ConstructorLocators.ORDER_MODAL)

    @allure.step('Проверяем, видна ли модалка заказа')
    def is_order_modal_visible(self):
        return self.is_element_visible(ConstructorLocators.ORDER_MODAL)

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        return self.get_text(ConstructorLocators.ORDER_NUMBER)

    @allure.step('Проверяем, отображается ли номер заказа')
    def order_number_visible(self):
        return self.is_element_visible(ConstructorLocators.ORDER_NUMBER)

    @allure.step('Находим каунтер ингредиента')
    def find_ingredient_counter_text(self, ingredient):
        counter = ingredient.find_element(*ConstructorLocators.INGREDIENT_COUNTER)
        return counter.text

    @allure.step('Находим место складывания ингредиентов')
    def find_ingredient_target(self):
        return self.find_element(ConstructorLocators.INGREDIENT_TARGET)

    @allure.step('Ждем, когда перестанет отображаться промежуточный номер заказа')
    def wait_fake_order_number_not_present(self):
        self.wait_text_not_present(ConstructorLocators.ORDER_NUMBER, "9999")
