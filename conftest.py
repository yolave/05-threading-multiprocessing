from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def fixt_auth_client():
    return TestClient(app, headers={"Authorization": "Bearer valid-token"})


@pytest.fixture
def fixt_unauth_client():
    return TestClient(app)


@pytest.fixture
def get_user_service_mock():
    with patch('src.services.user_service.user_service') as mock_service:
        yield mock_service
