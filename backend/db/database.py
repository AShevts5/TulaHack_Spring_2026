import os
from dotenv import load_dotenv
from pony.orm import Database
load_dotenv()
db = Database()
def bind_database() -> None:
    db.bind(
        provider="postgres",
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        database=os.getenv("POSTGRES_DB", "t2db"),
        port=int(os.getenv("POSTGRES_PORT", "5432")),
    )
def init_db(*, create_tables: bool = False) -> None:
    import db.models 
    bind_database()
    db.generate_mapping(create_tables=create_tables)
