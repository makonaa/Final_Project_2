from endpoint_executions import create_listing, update_listing, delete_listing
import allure


class TestListingInteractions:
    @allure.title('Тест - создаем объявление')
    def test_create_listing(self, api_client, listing_generator, listing_cleanup):
        headers = api_client.get_auth_headers()
        payload = listing_generator.get_listing_multipart_data()
        response = create_listing(files=payload, headers=headers)
        listing_cleanup.append({
            response.json()["id"]: headers
        })
        assert response.status_code == 201

    @allure.title('Тест - изменяем объявление зарегистрированным юзером')
    def test_edit_listing_for_registered_user(self, api_client, listing_generator, listing_cleanup):
        listing_id, headers = api_client.get_listing_id_and_auth_headers()
        new_listing_data = listing_generator.get_listing_multipart_data()
        response = update_listing(listing_id=listing_id, files=new_listing_data, headers=headers)
        listing_cleanup.append({
            listing_id: headers
        })
        assert response.status_code == 200

    @allure.title('Тест - изменяем объявление другим юзером, не создававшим объявление')
    def test_edit_listing_by_another_user(self, api_client, listing_generator, listing_cleanup):
        listing_id, headers = api_client.get_listing_id_and_auth_headers()
        new_listing_data = listing_generator.get_listing_multipart_data()
        new_user_auth_headers = api_client.get_auth_headers()
        response = update_listing(listing_id=listing_id, files=new_listing_data, headers=new_user_auth_headers)
        listing_cleanup.append({
            listing_id: headers
        })
        assert response.status_code == 401

    @allure.title('Тест - удаляем объявление')
    def test_delete_listing(self, api_client, listing_generator):
        listing_id, headers = api_client.get_listing_id_and_auth_headers()
        response = delete_listing(listing_id=listing_id, headers=headers)
        assert response.status_code == 200
