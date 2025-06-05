from unittest.mock import patch

import pytest

from app.core import firebase_app, firestore_client
from app.core.config import settings
from app.core.errors import FirebaseCredentialFileNotFound


@pytest.fixture(autouse=True)
def reset_singletons():
    firebase_app._app = None
    firestore_client._db = None
    yield
    firebase_app._app = None
    firestore_client._db = None


def test_get_firebase_app_valid(tmp_path):
    cred_file = tmp_path / "cred.json"
    cred_file.write_text("{}")
    settings.FIREBASE_CREDENTIALS = str(cred_file)

    with patch("app.core.firebase_app.credentials.Certificate") as cert, patch(
        "app.core.firebase_app.initialize_app"
    ) as init:
        cert.return_value = "cert"
        init.return_value = "app"

        app = firebase_app.get_firebase_app()

        assert app == "app"
        cert.assert_called_with(str(cred_file))
        init.assert_called_with("cert")


def test_get_firebase_app_invalid(tmp_path):
    settings.FIREBASE_CREDENTIALS = str(tmp_path / "missing.json")
    with patch(
        "app.core.firebase_app.credentials.Certificate",
        side_effect=FileNotFoundError,
    ):
        with pytest.raises(FirebaseCredentialFileNotFound):
            firebase_app.get_firebase_app()


def test_get_firestore_client_valid(tmp_path):
    cred_file = tmp_path / "cred.json"
    cred_file.write_text("{}")
    settings.FIREBASE_CREDENTIALS = str(cred_file)

    with patch(
        "app.core.firestore_client.service_account.Credentials.from_service_account_file"
    ) as from_file, patch("app.core.firestore_client.firestore.Client") as client:
        from_file.return_value = "creds"
        client.return_value = "db"

        db = firestore_client.get_firestore_client()

        assert db == "db"
        from_file.assert_called_with(str(cred_file))
        client.assert_called_with(credentials="creds")


def test_get_firestore_client_invalid(tmp_path):
    settings.FIREBASE_CREDENTIALS = str(tmp_path / "missing.json")
    with patch(
        "app.core.firestore_client.service_account.Credentials.from_service_account_file",
        side_effect=FileNotFoundError,
    ):
        with pytest.raises(FirebaseCredentialFileNotFound):
            firestore_client.get_firestore_client()
