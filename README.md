# Code Rocks

## В рамках хакатона Code Rocks мы делаем айти продукт

## [подробнее о задании](https://docs.google.com/document/d/1JBe4EZ_CvcwDvlbNHYeEvRC0xPRKnBhFJi78RvYGXxg/edit)

API Register

```
/api/auth/register/
data => {
    "name": "Alexey",
    "surname": "Ovchinnikov",
    "last_name": "allelleo",
    "phone":"2742131811217542",
    "email":"dev.11a2l1l1ell1eo@dfafd.daf",
    "password":"qwerty",
    "is_customer": true
}

return => 
errors:
{'error': 'Не все данные заполенены'}
{'error': 'Этот email уже используется'}
{'error': 'Этот телефон уже используется'}
good:
{'status': 'success', 'id' : 1234}
```

API Login

```
/api/auth/register/
data => {
    "email": "dev.allelleo@dfafd.daf",
    "password": "qwerty"
}

return => 
errors:
{'error': 'Не все данные заполенены'}
{'error': 'Нет пользователя с такой почтой'}
{'error': 'Неверный пароль'}
good:
{'token': token}
```

API account endpoint

```
/api/account/endpoint/
data => {
    "token": "BHGd0w3WzOo8RNxuNrqJG4HaX0oy35HYzks"
}

return => 
errors:
{'error': 'Не все данные заполенены'}
{'error': 'Токен не верный'}
{'error': 'Пользователь не найден'}
good:
{
    'username': 'res.username',
    'email': 'res.email',
}
```

API Login

```
/api/auth/register/
data => {
    "email": "dev.allelleo@dfafd.daf",
    "password": "qwerty"
}

return => 
errors:
{'error': 'Не все данные заполенены'}
{'error': 'Нет пользователя с такой почтой'}
{'error': 'Неверный пароль'}
good:
{'token': token}
```

API Create Task

```
/api/task/create/
data => {
    "title": "Task",
    "description": "hello hello",
    "price": 12312,
    "deadlines": "Today",
    "place": "Web",
    "category": [1,2,3],
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZXhwIjoxNjgzNzE0NDM2LCJpYXQiOjE2ODExMjI0MzZ9.jeQaN3kbBHGd0w3WzOo8RNxuNrqJG4HaX0oy35HYzks"
}

return => 
errors:
{'error': 'Нет токена'}
{'error': 'Токен не правильный'}
{'error': 'Пользователь не найден'}
{'error': 'Вы не заказчик, а исполнитель'}
{'error': 'Не все данные заполенены'}
good:
{
    'status': 'success',
    'task': str(task.id)
}
```

API account get user data

```
/api/account/endpoint/
data => {
    "token": "BHGd0w3WzOo8RNxuNrqJG4HaX0oy35HYzks"
}

return => 
errors:
{'error': 'Не все данные заполенены'}
{'error': 'Токен не верный'}
{'error': 'Пользователь не найден'}
good:
{
    'username': 'res.username',
    'email': 'res.email',
    ...
}
```

API chat start

```
/api/chat/start/
data => {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyd4lKQQc2I",
    "chat_to": 1,
    "task": 1
}

return => 
errors:
{'error': 'Не все данные заполенены'}
{'error': 'Токен не верный'}
{'error': 'Пользователь не найден'}
{'error': 'Нет такого пользователя'}
good:
{'success': True}
```

API chat all

```
/api/chat/all/
data => {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyd4lKQQc2I"
}

return => 
errors:
{'error': 'Не все данные заполенены'}
{'error': 'Токен не верный'}
{'error': 'Пользователь не найден'}

good:
{
    "0": {
        "chat_name": "Alexey Ovchinnikov",
        "last_message": "Вы:Вас пригласили в чат",
        "time": "2023-04-10 17:37:08.693438+00:00",
        "viewed": false,
        "id": 1
    },
    "1": {
        "chat_name": "Alexey Ovchinnikov",
        "last_message": "Вы:Вас пригласили в чат",
        "time": "2023-04-10 17:37:28.685184+00:00",
        "viewed": false,
        "id": 2
    },
    "2": {
        "chat_name": "Alexey Ovchinnikov",
        "last_message": "Вы:Вас пригласили в чат",
        "time": "2023-04-10 17:37:29.924180+00:00",
        "viewed": false,
        "id": 3
    },
    "3": {
        "chat_name": "Alexey Ovchinnikov",
        "last_message": "Вы:Вас пригласили в чат",
        "time": "2023-04-10 17:37:48.837796+00:00",
        "viewed": false,
        "id": 4
    }
}
```

