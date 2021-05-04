#import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_btn_exists(browser):
    browser.get(link)
    add_to_cart_btns_count = len(browser.find_elements_by_class_name("btn-add-to-basket"))
    #time.sleep(10)
    assert add_to_cart_btns_count == 1, "Кнопка добавления в корзину не найдена или найдено более 1 кнопки с классом 'btn-add-to-basket'"