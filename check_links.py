from playwright.sync_api import sync_playwright
import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]

def check_links():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent=random.choice(USER_AGENTS),
            viewport={'width': 1920, 'height': 1080},
        )
        page = context.new_page()
        
        try:
            print("Открываем Labirint...")
            page.goto("https://www.labirint.ru/genres/2308/", timeout=60000)
            page.wait_for_timeout(3000)
            
            # Находим первые 3 названия книг
            titles = page.locator(".product-title")
            count = min(3, titles.count())
            
            print(f"\n=== Проверяем первые {count} названий ===\n")
            
            for i in range(count):
                title_el = titles.nth(i)
                
                # Показываем HTML элемента
                html = title_el.inner_html()
                print(f"--- Название {i+1} ---")
                print(f"HTML: {html[:200]}")
                
                # Проверяем, есть ли атрибут href у самого элемента
                href = title_el.get_attribute("href")
                print(f"Атрибут href у .product-title: {href}")
                
                # Ищем ссылку ВНУТРИ элемента
                link_inside = title_el.locator("a").first
                if link_inside.count() > 0:
                    href_inside = link_inside.get_attribute("href")
                    print(f"Ссылка ВНУТРИ .product-title: {href_inside}")
                
                # Ищем ссылку РЯДОМ (в родительском элементе)
                parent = title_el.locator("xpath=..")  # Родитель
                link_nearby = parent.locator("a").first
                if link_nearby.count() > 0:
                    href_nearby = link_nearby.get_attribute("href")
                    print(f"Ссылка РЯДОМ (в родителе): {href_nearby}")
                
                print()
            
        except Exception as e:
            print(f"Ошибка: {e}")
        
        browser.close()

if __name__ == "__main__":
    check_links()