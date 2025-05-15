from pathlib import Path
from db_config import mycursor
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from datetime import datetime

BASE_PATH = Path(__file__).parent
REPORT_PATH = BASE_PATH / "relatorios_xlsx"
REPORT_PATH.mkdir(exist_ok=True)
WORKBOOK_PATH = REPORT_PATH / 'workbook.xlsx'


def create_full_report_xlsx  (table):
    try:
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
        WORKBOOK_PATH = REPORT_PATH / f'{table}_relatorio_{timestamp}.xlsx'
        workbook.save(WORKBOOK_PATH)
        print(f"Relatório salvo em: {WORKBOOK_PATH}")
        
    except Exception as e:
        print(f"Erro ao gerar relatório XLSX da tabela '{table}': {e}")


def create_report_xlsx_from_query(sql_query, report_name="relatorio"):
    try:
        mycursor.execute(sql_query)
        
        columns = [col[0] for col in mycursor.description]
        data = mycursor.fetchall()
        
        workbook = Workbook()
        worksheet: Worksheet = workbook.active
    #    worksheet.title = sheet_name
        worksheet.append(columns)
        
        for line in data:
            worksheet.append(line)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        WORKBOOK_PATH = REPORT_PATH / f'{report_name}_relatorio_{timestamp}.xlsx'
        workbook.save(WORKBOOK_PATH)
        print(f"Relatório salvo em: {WORKBOOK_PATH}")
        
    except Exception as e:
        print(f"Erro ao gerar relatório XLSX personalizado '{report_name}': {e}")
