import pytest

from Test_data.Client.generator import Generator
from Helpers.Client.customers_handler import CustomerHandler
from Pages.add_customer_page import AddCustomerPage
from Pages.customers_page import CustomersPage
from Pages.manager_page import ManagerPage


@pytest.fixture()
def manager_page(driver) -> ManagerPage:
    return ManagerPage(driver)


@pytest.fixture()
def customers_page(driver):
    return CustomersPage(driver)


@pytest.fixture()
def add_customer_page(driver):
    return AddCustomerPage(driver)


@pytest.fixture()
def generate_client_data():
    return Generator.generate_client_data


@pytest.fixture()
def get_avg_len():
    return CustomerHandler.get_avg_len


@pytest.fixture()
def get_closest_avg():
    return CustomerHandler.get_closest_avg