from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


URL_DATABASE='postgresql://postgres:12345678@localhost/emotion_db'


engine =create_engine(URL_DATABASE)
sessionlocal=sessionmaker(autocommit=False, autoflush= False, bind=engine)    #  Flush = vider 
Base = declarative_base()