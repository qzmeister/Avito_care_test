from playwright.sync_api import sync_playwright


def test_wrong_values():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()

        page = context.new_page()

        # Список подмен
        routes = [
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":-10,"energy":-10,"materials":-10,'
                            '"pineYears":-10,"water":-10}}},"isAuthorized":false},"status":"ok"}'
            },
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":"привет","energy":"привет",'
                            '"materials":"привет",'
                            '"pineYears":"привет","water":"привет"}}},"isAuthorized":false},"status":"ok"}'
            },
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":false,"energy":false,'
                            '"materials":false,"pineYears":false,"water":false}}},"isAuthorized":false},"status":"ok"}'
            },
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":null,"energy":null,'
                            '"materials":null,"pineYears":null,"water":null}}},"isAuthorized":false},'
                            '"status":"ok"}'
            }
        ]

        # Итерация подмен
        for i, route in enumerate(routes, start=1):
            page.route(route["url"], lambda route, request, response=route["response"]: route.fulfill(
                status=200,
                body=response
            ))

            page.goto("https://www.avito.ru/avito-care/eco-impact")
            context.set_default_timeout(30000)
            page.wait_for_selector(".desktop-wrapper-OutiE")

            # Скриншот счетчиков
            element = page.query_selector(".desktop-wrapper-OutiE")
            if element:
                element.screenshot(path=f"output/test_3_{i}.png")
            else:
                print(f"Элемент с классом 'desktop-wrapper-OutiE' не был найден после подмены {i}")

        browser.close()
