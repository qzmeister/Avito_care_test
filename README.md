# Инструкция по запуску тестов Avito Care

**Этот репозиторий содержит тесты для проверки функциональности счетчиков Avito Care.**

## Шаги по запуску:

1. **Установить Python**

   - Если у вас нет Python, скачайте и установите его с [официального сайта Python](https://www.python.org/). Рекомендуется использовать версию Python 3.7 или выше.

2. **Клонировать или скачать репозиторий**

   - Вы можете клонировать репозиторий с помощью команды git:
     ```
     git clone https://github.com/qzmeister/Avito_care_test.git
     ```
   - Или скачать архив с файлами репозитория, перейдя по ссылке: [Скачать ZIP](https://github.com/qzmeister/Avito_care_test/archive/refs/heads/master.zip)

3. **Установить зависимости**

   - Перейдите в каталог с репозиторием и выполните следующие команды в терминале (или командной строке):
     ```
     pip install -r requirements.txt
     ./post_install.sh
     ```
   - Это установит необходимые зависимости, включая Playwright, и выполнит скрипт для загрузки браузеров.

4. **Запустить тесты**

   - После успешной установки зависимостей выполните следующую команду для запуска тестов:
     ```
     python run_tests.py
     ```
   - Это запустит все тесты в репозитории по очереди.


