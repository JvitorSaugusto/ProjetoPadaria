from pathlib import Path
from db_config import mycursor
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from datetime import datetime

BASE_PATH = Path(__file__).parent
RELATORIO_PATH = BASE_PATH / "relatorios_xlsx"
RELATORIO_PATH.mkdir(exist_ok=True)
WORKBOOK_PATH = RELATORIO_PATH / 'workbook.xlsx'


def criar_relatorio_completo  (table):
    sql = f"SELECT * FROM {table}"
    mycursor.execute(sql)
    
    columns = [col[0] for col in mycursor.description]
    data = mycursor.fetchall()
    
    workbook = Workbook()
    worksheet: Worksheet = workbook.active
#    worksheet.title = sheet_name
    worksheet.append(columns)
    
    for line in data:
        worksheet.append(line)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    WORKBOOK_PATH = RELATORIO_PATH / f'{table}_relatorio_{timestamp}.xlsx'
    workbook.save(WORKBOOK_PATH)
    print(f"Relatório salvo em: {WORKBOOK_PATH}")
    
criar_relatorio_completo("cliente")