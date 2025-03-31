"""Отвечает за страницу списка клиентов."""
from typing import List

import allure
from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class CustomersPage(BasePage):
    """Класс страницы списка клиентов."""
    
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        self.__name_list = (By.XPATH, '//td[@class="ng-binding"][1]')
        self.__sort_names = (By.XPATH, '//a[normalize-space()="First Name"]')
        self.__delete_buttons = (By.XPATH, '//button[@ng-click="deleteCust(cust)"]')

    @allure.step("Нажать на кнопку имени для сортировки по алфавиту.")
    def sort_alphabetically(self, a_z_sort: bool) -> None:
        """
        Кликает на кнопку(ссылку) имен в таблице для сортировки.
        
        :param a_z_sort: Сортировать список по a->z или z->a
        """
        sort = self.find_element(*self.__sort_names)
        if a_z_sort: sort.click()
        sort.click()

    @allure.step("Получаем список имён.")
    def get_names(self) -> List[str]:
        """
        Находит имена по элементам таблицы на странице.
        
        :return: Список имён.
        """
        names = self.find_elements(*self.__name_list)
        names = [name.text for name in names]
        return names

    @allure.step("Удалить клиента по имени.")
    def delete_customer(self, names: List[str], name: str) -> None:
        """
        Находит кнопку удаления клиента по имени из списка.

        :param names: Список имён.
        :param name: Имя клиента.
        """
        buttons = self.find_elements(*self.__delete_buttons)
        position = names.index(name)
        buttons[position].click()
