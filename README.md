# Console phonebook
## _Django-приложение, которое позволяет работать со списком контактов через консоль_

[Техническое задание](https://docs.google.com/document/d/1dIH7lY05hNLSluZgOYsRyTrvLmyz4CnNEtJFFXBbS-c/edit)

## Особенности

> В проекте создана модель данных Contact и методы, 
> которые позволяют отображать данные, 
> добавлять их, редактировать и искать. 
> Также в проекте есть текстовый файл, 
> в котором хранятся данные, обрабатываемые методами модели.
> Для работы с программой через консоль написан скрипт.


## Стэк

- Python 3.9
- Django 4.2.10
- Docker

## Как использовать
Клонировать репозиторий:

```
git clone https://github.com/jisdtn/test-Effective_Mobile-phonebook.git
```
В корневой директории проекта 'test-Effective_Mobile-phonebook' введите команду:

```
make run
```
Помощник запустит оркестрацию docker compose, 
внутри будет смена рабочей директории и запуск скрипта.
Как только вы увидите в консоли приветственное сообщение и меню, 
утилитой можно пользоваться.

#### Чтобы удалить проект с машины, используйте команду:

```
docker compose down
```

## License

MIT


