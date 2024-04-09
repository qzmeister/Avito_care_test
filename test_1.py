import os
from playwright.sync_api import sync_playwright

def test_1():
    # Создание папки для скриншотов
    os.makedirs("output", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()

        page = context.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")

        # Таймаут для прогрузки страницы и элементов
        context.set_default_timeout(30000)
        page.wait_for_selector(".desktop-wrapper-OutiE")

        # Элемент на странице со счётчиками
        element = page.query_selector(".desktop-wrapper-OutiE")

        if element:
            element.screenshot(path="output/test_1.png")
        else:
            print("Элемент с классом 'desktop-wrapper-OutiE' не был найден")

        browser.close()
