from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")

POSTGRES_USER = getenv("POSTGRES_USER")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
POSTGRES_DB = getenv("POSTGRES_DB")
POSTGRES_PORT = getenv("POSTGRES_PORT")
POSTGRES_HOST = getenv("POSTGRES_HOST")

POSTGRES_DATA = {
    "user": POSTGRES_USER,
    "password": POSTGRES_PASSWORD,
    "database": POSTGRES_DB,
    "port": POSTGRES_PORT,
    "host": POSTGRES_HOST
}

DATABASE_URL = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}".format(**POSTGRES_DATA)
TEST_DATABASE_URL = getenv("TEST_DATABASE_URL")
