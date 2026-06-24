from playwright.sync_api import sync_playwright
import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]

def check_card_structure():
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
            
            # Находим первую карточку товара
            title = page.locator(".product-title").first
            
            # Поднимаемся на несколько уровней вверх, чтобы найти всю карточку
            # Попробуем разные уровни родителей
            print("\n=== Ищем структуру карточки ===\n")
            
            for level in range(1, 6):
                parent = title.locator(f"xpath=ancestor::*[{level}]")
                if parent.count() > 0:
                    tag = parent.evaluate("el => el.tagName")
                    class_name = parent.evaluate("el => el.className")
                    print(f"Уровень {level}: <{tag}> class='{class_name}'")
                    
                    # Если нашли что-то похожее на карточку, покажем HTML
                    if "product" in class_name.lower() or "tile" in class_name.lower() or "item" in class_name.lower():
                        print(f"\n--- HTML карточки (уровень {level}) ---")
                        html = parent.inner_html()
                        print(html[:2000])  # Первые 2000 символов
                        print("\n")
                        break
            
            # Также попробуем найти все ссылки на странице и посмотреть, какие из них ведут на книги
            print("\n=== Все ссылки на книги (содержат /books/) ===")
            book_links = page.locator("a[href*='/books/']")
            count = min(5, book_links.count())
            
            for i in range(count):
                link = book_links.nth(i)
                href = link.get_attribute("href")
                text = link.inner_text().strip()
                print(f"{i+1}. {text[:60]}... -> {href}")
            
        except Exception as e:
            print(f"Ошибка: {e}")
            import traceback
            traceback.print_exc()
        
        browser.close()

if __name__ == "__main__":
    check_card_structure()