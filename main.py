from db_config import mycursor
from menu import Menu
from pathlib import Path

BASE_PATH = Path(__file__).parent
REPORT_PATH = BASE_PATH / "relatorios_xlsx"

if __name__ == "__main__":
    menu = Menu(mycursor)
    menu.show_main_menu()
