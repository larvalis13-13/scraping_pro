from playwright.sync_api import sync_playwright

def test_browser():
    with sync_playwright() as p:
        # Запускаем браузер
        browser = p.chromium.launch(headless=False)  # headless=False = видим окно браузера
        page = browser.new_page()
        
        # Открываем сайт
        page.goto("https://example.com")
        
        # Ждём загрузки
        page.wait_for_load_state("networkidle")
        
        # Получаем заголовок страницы
        title = page.title()
        print(f"Заголовок страницы: {title}")
        
        # Закрываем браузер
        browser.close()

if __name__ == "__main__":
    test_browser()