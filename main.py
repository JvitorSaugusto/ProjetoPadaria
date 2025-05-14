from db_config import mycursor, mydb
from menu import Menu
from pathlib import Path

BASE_PATH = Path(__file__).parent
REPORT_PATH = BASE_PATH / "relatorios_xlsx"

def main():
    menu = Menu(mycursor)
    try:
        menu.show_main_menu()
    except Exception as e:
        print(f"Erro inesperado: {e}")
        print("Revertendo alterações não salvas...")
        mydb.rollback()
    finally:
        print("Fechando conexão com o banco de dados...")
        mydb.close()
    
if __name__ == "__main__":
    main()