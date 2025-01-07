from .model import *
import os

sqlite_file_name = os.path.join(os.path.dirname(__file__), '..', 'database.db')
sqlite_url = f'sqlite:///{sqlite_file_name}'


engine = create_engine(sqlite_url, echo=True)

if __name__ == '__main__':
    SQLModel.metadata.create_all(engine)
