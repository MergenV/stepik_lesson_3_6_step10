import time

import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_add_to_cart_button(browser):
    browser.get(link)
    element = len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"))
    assert element > 0, 'Cелектор кнопки не найден'
    time.sleep(3)



if __name__ == '__main__':
    pytest.main()


