import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import requests
import uuid
from data.urls import BASE_API_URL


class WebDriverFactory:
    
    @staticmethod
    def get_driver(browser_name):
        browser_name = browser_name.lower()
        
        if browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--start-maximized")
            return webdriver.Chrome(options=options)
        
        elif browser_name == "firefox":
            options = FirefoxOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            return webdriver.Firefox(options=options)
        
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def browser(request):
    browser_name = request.param
    driver = WebDriverFactory.get_driver(browser_name)
    if browser_name == "firefox":
        driver.maximize_window()
    yield driver
    driver.quit()


def create_test_user():
    unique_id = str(uuid.uuid4())[:8]
    user_data = {
        "email": f"test_{unique_id}@test.com",
        "name": f"TestUser_{unique_id}",
        "password": "TestPass123!"
    }
    response = requests.post(
        f"{BASE_API_URL}/auth/register",
        json=user_data
    )
    if response.status_code == 200:
        return user_data
    else:
        raise Exception(f"Failed to create test user: {response.text}")


def delete_test_user(email):
    try:
        login_response = requests.post(
            f"{BASE_API_URL}/auth/login",
            json={"email": email, "password": "TestPass123!"}
        )
        
        if login_response.status_code == 200:
            token = login_response.json().get("accessToken")
            
            requests.delete(
                f"{BASE_API_URL}/auth/user",
                headers={"Authorization": f"Bearer {token}"}
            )
    except Exception:
        pass 


@pytest.fixture
def test_user():
    user_data = create_test_user()
    yield user_data
    delete_test_user(user_data["email"])
