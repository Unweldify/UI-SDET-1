"""Этот файл отвечает за нахождение элементов страницы."""
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Класс базовой страницы."""

    def __init__(self, driver, timeout=10):
        self.__driver = driver
        self.__timeout = int(timeout)
        self.__wait = WebDriverWait(driver, timeout)

    def find_element(self, by: By, value: str) -> WebElement:
        """
        Находит один элемент страницы по XPATH, id и тд.

        :params by: Тип элемента страницы
        :params value: Уточнение для нахождения определённого элемента
        :return: Элемент страницы
        """
        return self.__wait.until(expected_conditions.visibility_of_element_located((by, value)),
                               message=f'Элемент {by, value} не найден')

    def find_elements(self, by: By, value: str) -> List[WebElement]:
        """
        Находит несколько элементов страницы.

        :params by: Тип элемента страницы
        :params value: Уточнение для нахождения определённого элемента
        :return: Список элементов страницы
        """
        return self.__wait.until(expected_conditions.visibility_of_all_elements_located((by, value)),
                               message=f'Элементы {by, value} не найдены')
