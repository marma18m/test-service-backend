from sqlmodel import SQLModel, create_engine


class DatabaseService:
    def __init__(self, sqlite_file_name="database.db"):
        self.sqlite_url = f"sqlite:///{sqlite_file_name}"
        self.engine = create_engine(self.sqlite_url)

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)
