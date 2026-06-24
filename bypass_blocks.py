from playwright.sync_api import sync_playwright
import random
import time

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
]

def parse_with_stealth():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=['--disable-blink-features=AutomationControlled']
        )
        
        chosen_ua = random.choice(USER_AGENTS)
        
        context = browser.new_context(
            user_agent=chosen_ua,
            viewport={'width': 1920, 'height': 1080},
            locale='ru-RU',
            timezone_id='Europe/Moscow',
        )
        
        page = context.new_page()
        
        try:
            # Показываем, какой User-Agent мы установили (из Python)
            print(f"Мы установили User-Agent:\n{chosen_ua}\n")
            
            # Заходим на сайт, который показывает твой User-Agent
            page.goto("https://httpbin.org/user-agent", timeout=30000)
            page.wait_for_load_state("networkidle")
            
            # Получаем User-Agent, который реально видит сайт (через JavaScript)
            real_ua = page.evaluate("navigator.userAgent")
            print(f"Сайт видит нас как:\n{real_ua}")
            
            # Проверяем, совпадают ли они
            if real_ua == chosen_ua:
                print("\n✅ Отлично! Сайт видит тот User-Agent, который мы подставили.")
            else:
                print("\n⚠️  User-Agent не совпадает — возможно, сайт его переопределяет.")
            
            # Имитируем человеческое поведение
            print("\nСкроллим страницу вниз...")
            for _ in range(3):
                page.mouse.wheel(0, 300)
                time.sleep(random.uniform(0.5, 1.5))
            
            print("✅ Готово! Сайт не заблокировал нас.")
            
        except Exception as e:
            print(f"Ошибка: {e}")
        
        browser.close()

if __name__ == "__main__":
    parse_with_stealth()