from unittest.mock import MagicMock

from src.models.user import UserIn, UserOut
from src.services.user_service import UserService


def test_create_user():
    # GIVEN
    user_in = UserIn(name="Alice", email="test@email.com")
    expected_user_out = UserOut(name="Alice", email="test@email.com", id=1)

    repo = MagicMock()
    repo.create.return_value = expected_user_out

    user_service = UserService(repo)

    # WHEN
    created_user = user_service.create_user(user_in)

    # THEN
    repo.create.assert_called_once_with(user_in)
    assert created_user == expected_user_out


def test_list_users():
    # GIVEN
    expected_users = [
        UserOut(name="Alice", email="alice@email.com", id=1),
        UserOut(name="Bob", email="bob@email.com", id=2)
    ]

    repo = MagicMock()
    repo.list.return_value = expected_users

    user_service = UserService(repo)

    # WHEN
    users = user_service.list_users()

    # THEN
    repo.list.assert_called_once()
    assert users == expected_users
