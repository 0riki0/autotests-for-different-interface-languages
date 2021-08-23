import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_the_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)

    lang = browser.find_elements_by_css_selector("[lang='fr']")
    if lang == "fr":
        button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
        assert button.text == "Ajouter au panier", "!!! НЕ НАШЕЛ КНОПКУ ДОБАВЛЕНИЯ В КОРЗИНУ !!!!!!"
    else:
        button = browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
        assert button, '!!! НЕ НАШЕЛ КНОПКУ ДОБАВЛЕНИЯ В КОРЗИНУ !!!!!!'
