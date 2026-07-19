from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)



class Base(DeclarativeBase):
    pass

# Session para rotas usarem
def get_db():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()



# # Apenas para teste de conexão bem sucedida
# from sqlalchemy import text

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT 1"))
#     print(result.scalar())