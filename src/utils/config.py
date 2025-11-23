from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST: str = os.getenv("DB_HOST", "localhost")
DB_PORT: int = int(os.getenv("DB_PORT", 5432))
DB_PASSWORD: str = os.getenv("DB_PASSWORD", "password")
DB_NAME: str = os.getenv("DB_NAME", "mydatabase")
DB_USERNAME: str = os.getenv("DB_USERNAME", "user")
DB_SSL_MODE: str = os.getenv("DB_SSL_MODE", "prefer")


def get_database_url() -> str:
    """Constructs the database URL from environment variables."""
    return f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode={DB_SSL_MODE}"
