"""Этот файл помогает сгенерировать тестовые вводные данные."""
from random import randint
from typing import Tuple


class Generator:
    """Класс для генерации данных."""

    @staticmethod
    def generate_client_data() -> Tuple[str]:
        """
        Генерирует код из 10 цифр, по коду генерируется имя.

        :return: Кортеж из 3 строк: Имя, фамилия и код.
        """
        post_code = ''
        for _ in range(0, 10):
            post_code += str(randint(0, 9))

        first_name = ''
        for i in range(0, 10, 2):
            first_name += chr(97 + int(post_code[i:i+2]) % 26)

        return (first_name, post_code)
