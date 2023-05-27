# import json
# import unittest
# import pytest
#
# from make_it.app import app
#
#
# @pytest.fixture
# def payload() -> dict:
#     return {"first_name": "Jan", "last_name": "Kowalski"}
#
#
# # def test_create_user_returns_user(payload: dict) -> None:
# #     with app.test_request_context(method="POST", path="/users", json=payload):
# #         result = create_user()
# #     assert result.json == payload
#
# #
# # def test_create_user_prints_user_on_console(payload: dict, capsys) -> None:
# #     with app.test_request_context(method="POST", path="/users", json=payload):
# #         create_user()
# #     actual = capsys.readouterr().out
# #     expected = json.dumps(payload) + "\n"
# #     assert actual == expected
# #
# # def test_update_user_returns_user(payload: dict) -> None:
# #     with app.test_request_context(method="PUT", path="/users", json=payload):
# #         result = update_user()
# #     assert result.json == payload
#
#
# def test_get_users_endpoint() -> None:
#     with app.test_client() as client:
#         response = client.get('/users/3')
#         assert response.status_code == 501
#
#
# def test_create_user_endpoint(payload: dict) -> None:
#     with app.test_client() as client:
#         response = client.post('/users', json=payload)
#         assert response.status_code == 201
#         assert response.get_json() == payload
#
#
# def test_update_user_endpoint(payload: dict) -> None:
#     with app.test_client() as client:
#         response = client.put('/users/1', json=payload)
#         assert response.status_code == 200
#         assert response.get_json() == payload
#
#
# def test_patch_user_endpoint(payload: dict) -> None:
#     with app.test_client() as client:
#         response = client.patch('/users/1', json=payload)
#         assert response.status_code == 200
#         key = next(iter(payload))
#         assert response.get_json() == {key: payload[key]}
#
#
# def test_delete_user_endpoint() -> None:
#     with app.test_client() as client:
#         response = client.delete('/users/1')
#         assert response.status_code == 204
#
#
# class TestEndpoints(unittest.TestCase):
#     def setUp(self):
#         self.app = app
#         self.client = app.test_client()
#
#
#     def test_get_users(self):
#         response = self.client.get('/users/1')
#         self.assertEqual(response.status_code, 501)
#
#     def test_create_user(self):
#         user = {'name': 'John', 'email': 'john@example.com'}
#         response = self.client.post('/users', json=user)
#         self.assertEqual(response.status_code, 201)
#         self.assertDictEqual(response.json, user)
#
#     def test_update_user(self):
#         user_id = 123
#         user = {'id': user_id, 'name': 'John', 'email': 'john@example.com'}
#         response = self.client.put(f'/users/{user_id}', json=user)
#         self.assertEqual(response.status_code, 200)
#         self.assertDictEqual(response.json, user)
#
#     def test_patch_user(self):
#         user_id = 12
#         user = {'name': 'John'}
#         response = self.client.patch(f'/users/{user_id}', json=user)
#         self.assertEqual(response.status_code, 200)
#         self.assertDictEqual(response.json, user)
#
#     def test_delete_user(self):
#         user_id = 123
#         response = self.client.delete(f'/users/{user_id}')
#         self.assertEqual(response.status_code, 204)
