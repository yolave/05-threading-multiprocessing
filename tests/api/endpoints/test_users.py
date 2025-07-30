from unittest.mock import MagicMock

from models.user import UserOut


def test_create_user(fixt_auth_client, get_user_service_mock):
    # GIVEN
    input_json = {"name": "Alice", "email": "alice@example.com"}
    expected_user_out = UserOut(name="Alice", email="alice@example.com", id=1)

    get_user_service_mock.create_user = MagicMock(return_value=expected_user_out)

    # WHEN
    res = fixt_auth_client.post("/users/", json=input_json)

    # THEN
    assert res.status_code == 201
    assert res.json() == expected_user_out.model_dump()


def test_list_users(fixt_auth_client, get_user_service_mock):
    # GIVEN
    expected_users = [
        UserOut(name="Alice", email="alice@email.com", id=1),
        UserOut(name="Bob", email="bob@email.com", id=2)
    ]

    get_user_service_mock.list_users = MagicMock(return_value=expected_users)

    # WHEN
    res = fixt_auth_client.get("/users/")

    # THEN
    assert res.status_code == 200
    assert res.json() == [user.model_dump() for user in expected_users]


def test_create_user_unauthorized(fixt_unauth_client):
    # GIVEN
    input_json = {"name": "Alice", "email": "alice@example.com"}

    # WHEN
    res = fixt_unauth_client.post("/users/", json=input_json)

    # THEN
    assert res.status_code == 401


def test_list_users_unauthorized(fixt_unauth_client):
    # WHEN
    res = fixt_unauth_client.get("/users/")

    # THEN
    assert res.status_code == 401
