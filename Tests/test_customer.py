"""Файл отвечающий за тест кейсы."""
import allure


@allure.title('Проверить функциональность добавления клиента.')
def test_adding_customer(manager_page, add_customer_page, customers_page, generate_client_data):
    manager_page.to_add_cust()

    with allure.step('Генерируем данные клиента.'):
        customer = generate_client_data()

    # Я не знаю как 'не хардкодить генерацию фамилии', по заданию не сказано генерить фамилию
    # но фамилия является обязятельной строкой поэтому я вставлю свою
    surname = 'Egorov'
    add_customer_page.add_customer(*customer, surname)
    success = add_customer_page.handle_alert()

    with allure.step('Смотрим если клиент добавился по выводу окна.'):
        assert 'Customer added successfully' in success, (
            f'Ошибка при добавлении клиента, "{success}".'
            )

    manager_page.to_cust()

    names = customers_page.get_names()

    with allure.step('Смотрим если клиент в списке.'):
        assert customer[0] in names, (
            f'Клиент "{customer[0]}" не найден в списке.'
        )


@allure.title('Проверить функциональность сортировки имен в списке клиентов.')
def test_sorting_customers(manager_page, customers_page) :
    manager_page.to_cust()

    # Сортируем список на странице, и смотрим если он отсортирован правильно
    a_z_sort = True
    customers_page.sort_alphabetically(a_z_sort)
    names = customers_page.get_names()

    sorted_names = sorted(names, key=str.lower)

    with allure.step(f'Смотрим если список был правильно отсортирован по алфавиту от {"a до z" if a_z_sort else "z до a"}.'):
        assert names == sorted_names if a_z_sort else reversed(sorted_names), (
            'Список не отсортирован по алфавиту.'
        )


@allure.title('Проверить функциональность удаления клиентов в списке.')
def test_deleting_customer(manager_page, customers_page, get_avg_len, get_closest_avg):
    manager_page.to_cust()

    name_list = customers_page.get_names()

    with allure.step('Находим среднее арифметическое длин имён клиентов.'):
        average = get_avg_len(name_list)

    with allure.step('Находим клиента у которого длина имени ближе к среднему арифметическому.'):  
        name = get_closest_avg(name_list, average)

    customers_page.delete_customer(name_list, name)

    name_list = customers_page.get_names()

    with allure.step('Смотрим если клиент удалился из списка.'):
        assert not (name in name_list), (
            'Клиент не удалился из списка.'
            )
