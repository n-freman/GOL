import os
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv('.env')


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", "5432")
    user = os.environ.get("DB_USER", "golAdmin")
    pwd = os.environ.get("DB_PWD", "db_pwd")
    db_name = os.environ.get("DB_NAME", "gol")
    return (
        f"postgresql://%s:%s@{host}:{port}/{db_name}"
        % (
            quote_plus(user), # escape username
            quote_plus(pwd) # escape password
    ))

