import os
from jogoteca import app


SECRET_KEY = "alura"

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + "/uploads"

SQLALCHEMY_DATABASE_URI = "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(
    SGBD="mysql+mysqlconnector",
    usuario="root",
    senha="",
    servidor="localhost",
    database="jogoteca",
)
