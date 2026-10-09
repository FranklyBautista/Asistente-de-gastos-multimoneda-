"""Arranque del bot: polling en dev, webhook en prod."""

from gastos.config import get_settings
from gastos.observability.logging import configure_logging, get_logger


def run() -> None:
    configure_logging()
    settings = get_settings()
    get_logger().info("startup", env=settings.env)


if __name__ == "__main__":
    run()
