import pytest
from api_client import ApiClient
from generators.user_generation import DataGenerator
from generators.listing_generation import ListingGenerator
from endpoint_executions import delete_listing
import allure


@pytest.fixture
def data_generator():
    return DataGenerator()

@pytest.fixture
def api_client():
    return ApiClient()

@pytest.fixture
def listing_generator():
    return ListingGenerator()

@pytest.fixture(scope="session")
def listing_cleanup():
    list_to_cleanup = []
    yield list_to_cleanup
    for item in list_to_cleanup:
        for key, value in item.items():
            try:
                response = delete_listing(listing_id=key, headers=value)
            except Exception as e:
                message = f'Failed to delete listing with id: {key}, error: {e}'
                allure.attach(message, name='Error during cleanup', attachment_type=allure.attachment_type.TEXT)
                continue

            if response.status_code != 200:
                message = f'Failed to delete user, error: {response.status_code}, {response.text}'
                allure.attach(message, name='Error during cleanup', attachment_type=allure.attachment_type.TEXT)
