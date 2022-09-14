"""
    Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

company_value = {
    'mail': 150,
    'yandex': 200,
    'google': 400,
    'aitat': 10,
    'sberbank': 300,
    'sovcombank': 250,
    'delivery club': 90
}


# Способ №1: O(N * log N)
def sorted_1(company):
    value_company = []  # O(1)
    for k, v in company.items():  # O(N)
        value_company.append(v)  # O(1)
        value_company.sort(reverse=True)  # O(N*log N)
    # print(''.join(str(value_company[0:3])[1:14]))
    return ''.join(str(value_company[0:3])[1:14])  # O(n)


# sorted_1(company_value)
print(sorted_1(company_value))


# Способ №2:
# Cложность: O(N*log N)  n + n*log n + 1
def sorted_2(company):
    list_company = list(company.items())  # O(n)
    list_company.sort(key=lambda i: i[1], reverse=True)  # O(N*log n)
    for i in range(3):  # O(1)
        print(f"{list_company[i][0]}: {list_company[i][1]}")


sorted_2(company_value)


# третий вариант - O(N)
def sorted_3(company):
    input_max = {}  # O(1)
    list_d = dict(company)  # O(n)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])  # 0(n) + 0(n)
        del list_d[maximum[0]]  # O(1)
        input_max[maximum[0]] = maximum[1]  # O(n)
    print(input_max)


sorted_3(company_value)
