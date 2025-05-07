from mysql.connector import connect
from dotenv import load_dotenv
import os

load_dotenv()

print("HOST:", os.getenv("BD_HOST"))
print("USER:", os.getenv("BD_ADMIN_USER"))
print("PWD :", os.getenv("BD_PASSWORD"))

my_db = connect(
    host = os.getenv("BD_HOST"),
    user = os.getenv("BD_ADMIN_USER"),
    password = os.getenv("BD_ADMIN_PASSWORD")
)

print(my_db)