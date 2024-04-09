from playwright.sync_api import sync_playwright


def test_equal_partitioning():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()

        page = context.new_page()

        # Список подмен
        routes = [
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":1,"energy":1,"materials":1,'
                            '"pineYears":1,"water":1}}},"isAuthorized":false},"status":"ok"}'
            },
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":999,"energy":999,"materials":999,'
                            '"pineYears":999,"water":999}}},"isAuthorized":false},"status":"ok"}'
            },
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":1000,"energy":1000,'
                            '"materials":1000,"pineYears":1000,"water":1000}}},"isAuthorized":false},"status":"ok"}'
            },
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":1001,"energy":1001,'
                            '"materials":1001,"pineYears":1001,"water":1001}}},"isAuthorized":false},"status":"ok"}'
            },
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":999499,"energy":999499,'
                            '"materials":999499,"pineYears":999499,"water":999499}}},"isAuthorized":false},'
                            '"status":"ok"}'
            },
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":999500,"energy":999500,'
                            '"materials":999500,"pineYears":999500,"water":999500}}},"isAuthorized":false},'
                            '"status":"ok"}'
            },
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":999999,"energy":999999,'
                            '"materials":999999,"pineYears":999999,"water":999999}}},"isAuthorized":false},'
                            '"status":"ok"}'
            },
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":1000000,"energy":1000000,'
                            '"materials":1000000,"pineYears":1000000,"water":1000000}}},"isAuthorized":false},'
                            '"status":"ok"}'
            },
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":1000001,"energy":1000001,'
                            '"materials":1000001,"pineYears":1000001,"water":1000001}}},"isAuthorized":false},'
                            '"status":"ok"}'
            },
            {
                "url": "**/web/1/charity/ecoImpact/init",
                "response": '{"result":{"blocks":{"personalImpact":{"data":{"co2":9999999,"energy":9999999,'
                            '"materials":9999999,"pineYears":9999999,"water":9999999}}},"isAuthorized":false},'
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
                element.screenshot(path=f"output/test_2_{i}.png")
            else:
                print(f"Элемент с классом 'desktop-wrapper-OutiE' не был найден после подмены {i}")

        browser.close()
