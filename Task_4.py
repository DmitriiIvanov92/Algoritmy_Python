"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

users_account = {
    'user1': {'password': '12345', 'activation': True},
    'user2': {'password': '123456789', 'activation': False},
    'user3': {'password': 'qwerty', 'activation': True}
}


def authorization_1(user, user_name, user_pass):
    for key, value in user.items():
        if key == user_name:
            if value['password'] == user_pass and value['activation']:
                return 'Доступ разрешен!'
            elif value['password'] == user_pass and not value['activation']:
                return 'Необходимо активировать учетную запись!'
            elif value['password'] != user_pass:
                return 'Не верный пароль!'

        return 'Пользователя не существует!'


def authorization_2(user, user_name, user_pass):
    if user.get(user_name):
        if user[user_name]['password'] == user_pass and user[user_name]['activation']:
            return 'Доступ разрешен!'
        elif user[user_name]['password'] == user_pass and not user[user_name]['activation']:
            return 'Необходимо активировать учетную запись!'
        elif user[user_name]['password'] != user_pass:
            return 'Не верный пароль!'

    else:
        return 'Пользователя не существует!'


print(authorization_1(users_account, 'user1', '12345'))
print(authorization_1(users_account, 'user6', '1111'))

print(authorization_2(users_account, 'user1', '12345'))
print(authorization_2(users_account, 'user6', '1111'))

