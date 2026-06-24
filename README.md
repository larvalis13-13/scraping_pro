# 🕷️ Scraping Pro — Продвинутый парсинг сайтов

Коллекция скриптов для парсинга веб-сайтов с использованием Playwright. Включает обход блокировок, работу с JavaScript-сайтами и экспорт данных в Excel.

## 🚀 Возможности

- ✅ **Парсинг JavaScript-сайтов** — Playwright для сайтов с динамической загрузкой
- 🛡️ **Обход блокировок** — ротация User-Agent, случайные задержки, скрытие автоматизации
- 📊 **Экспорт в Excel** — красивое форматирование с автоподбором ширины колонок
-  **Пагинация** — автоматический переход по страницам каталога
- 🎯 **Работа с реальными сайтами** — пример парсера книжного магазина Labirint

## 📦 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <your-repo-url>
   cd scraping_pro

   
2. Создайте виртуальное окружение:
   python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

3. Установите зависимости:
pip install playwright beautifulsoup4 openpyxl requests
playwright install chromium

Скрипты
test_playwright.py — тест браузера
bypass_blocks.py — обход блокировок (User-Agent, задержки)
parse_js_to_excel.py — парсинг цитат в Excel
parse_ecommerce.py — парсер Labirint (книги, цены, ссылки)
Технологии
Playwright, BeautifulSoup, OpenPyXL