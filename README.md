# Внесение правок в электронный дневник школы

Используйте скрипт для внесения правок в электронный дневник школы.
- Исправление оценок.
- Удаление замечаний.
- Добавление похвалы.

## Запуск
а) Если есть доступ к серверу сайта:
- Скачайте скрипт.
- Положите скрипт рядом с файлом `manage.py`
- См. пункт `Работа со скриптом`.<br>

б) Если нет доступа к серверу сайта необходимо развернуть сайт локально:
- Скачайте репозиторий. [Ссылка](https://github.com/devmanorg/e-diary.git)
- Скачайте архив с базой данных. [Ссылка](https://dvmn.org/filer/canonical/1562234129/166/)
- Cоздайте `.env` и укажите в `DATABASE_NAME ` путь к БД.
- Прочитайте раздел `Запуск` в репозитории сайта. [Ссылка](https://github.com/devmanorg/e-diary/tree/master#%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA)
- Следуйте пункту `а`.

## Работа со скриптом
- Запустите django shell:
```commandline
python manage.py shell
```
- Импортируйте скрипт в shell:
```python
from script import get_child, fix_marks, remove_chastisements, create_commendation
```
- Запустите функции исправления дневника.<br>

    Для исправления оценок:
    ```python
    fix_marks('Баранова Евфросиния Эльдаровна')
    ```
    Для удаления замечаний:
    ```python
    remove_chastisements('Баранова Евфросиния Эльдаровна')
    ```
    Для добавления похвалы:
    ```python
    create_commendation('Баранова Евфросиния Эльдаровна')
    ```

## Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/).