from mysql.connector import connect
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("BD_ADMIN_USER"))

my_db = connect(
    host = os.getenv("BD_HOST"),
    user = os.getenv("BD_ADMIN_USER"),
    password = os.getenv("BD_PASSWORD")
)

print(my_db)