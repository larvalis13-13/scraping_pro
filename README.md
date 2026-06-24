# 🕷️ Scraping Pro — Продвинутый парсинг сайтов

Коллекция скриптов для парсинга веб-сайтов с использованием Playwright. Включает обход блокировок, работу с JavaScript-сайтами и экспорт данных в Excel.

## 🚀 Возможности

- ✅ **Парсинг JavaScript-сайтов** — Playwright для сайтов с динамической загрузкой
- 🛡️ **Обход блокировок** — ротация User-Agent, случайные задержки, скрытие автоматизации
- 📊 **Экспорт в Excel** — красивое форматирование с автоподбором ширины колонок
-  **Пагинация** — автоматический переход по страницам каталога
- 🎯 **Работа с реальными сайтами** — пример парсера книжного магазина Labirint

## Установка

```bash
git clone <your-repo-url>
cd scraping_pro
python3 -m venv venv
source venv/bin/activate
pip install playwright beautifulsoup4 openpyxl requests
playwright install chromium