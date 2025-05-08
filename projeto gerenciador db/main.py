from db_config import mycursor
from menu import Menu

if __name__ == "__main__":
    menu = Menu(mycursor)
    menu.exibir_menu_principal()