import pytest
from pydantic import ValidationError

from gastos.config import Settings

REQUIRED = {
    "TELEGRAM_BOT_TOKEN": "123:abc",
    "ALLOWED_TELEGRAM_IDS": "[123456789]",
    "DATABASE_URL": "postgresql://localhost/test",
}


@pytest.fixture(autouse=True)
def clean_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in REQUIRED:
        monkeypatch.delenv(name, raising=False)


def test_settings_loads_required(monkeypatch: pytest.MonkeyPatch) -> None:
    for name, value in REQUIRED.items():
        monkeypatch.setenv(name, value)
    settings = Settings(_env_file=None)  # pyright: ignore[reportCallIssue]
    assert settings.allowed_telegram_ids == [123456789]
    assert settings.env == "dev"


@pytest.mark.parametrize("missing", list(REQUIRED))
def test_settings_fails_when_required_missing(
    monkeypatch: pytest.MonkeyPatch, missing: str
) -> None:
    for name, value in REQUIRED.items():
        if name != missing:
            monkeypatch.setenv(name, value)
    with pytest.raises(ValidationError, match=missing.lower()):
        Settings(_env_file=None)  # pyright: ignore[reportCallIssue]
