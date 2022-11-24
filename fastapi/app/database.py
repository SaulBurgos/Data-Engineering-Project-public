from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://my_user:my_password@docker_example_my_postgresql:5432/my_db"

engine = create_engine(
	SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
	db = SessionLocal()

	try:
		yield db
	except:
		db.close()