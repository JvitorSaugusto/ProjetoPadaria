from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from pathlib import Path
from datetime import datetime
from db_config import mycursor

BASE_PATH = Path(__file__).parent
RELATORIO_PDF_PATH = BASE_PATH / "relatorios_pdf"
RELATORIO_PDF_PATH.mkdir(exist_ok=True)

# Função que gera um relatório completo em PDF com os dados de uma tabela
def create_full_report_pdf(table):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        CANVAS_PATH = RELATORIO_PDF_PATH / f'{table}_relatorio_{timestamp}.pdf'
        
        pdf = canvas.Canvas(str(CANVAS_PATH), pagesize=landscape(A4))
        width, height = landscape(A4) 

        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(50, height - 50, f"Relatório da Tabela: {table}")
        
        mycursor.execute(f"SELECT * FROM {table}")
        data = mycursor.fetchall()
        columns = [col[0] for col in mycursor.description]  # Cabeçalhos das colunas
        
        x_start = 50
        y_start = height - 80
        current_y = y_start
        row_spacing = 18
        max_rows_per_page = 40
        row_count = 0

        pdf.setFont("Helvetica-Bold", 10)
        for i, column in enumerate(columns):
            pdf.drawString(x_start + i * 100, current_y, str(column))
        
        current_y -= row_spacing
        row_count += 1
        pdf.setFont("Helvetica", 10)

        for row in data:
            if row_count >= max_rows_per_page:
                pdf.showPage()
                current_y = height - 50
                row_count = 0
                
            for i, value in enumerate(row):
                pdf.drawString(x_start + i * 100, current_y, str(value))
            current_y -= row_spacing
            row_count += 1

        pdf.save()
        print("Relatório criado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao gerar relatório PDF da tabela '{table}': {e}")


# Gera relatórios com Querys livres, permitindo maior liberado para executar JOINS e consultas mais complexas.
def create_report_pdf_from_query(sql_query, report_name="relatorio"):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        CANVAS_PATH = RELATORIO_PDF_PATH / f'{report_name}_relatorio_{timestamp}.pdf'
        
        pdf = canvas.Canvas(str(CANVAS_PATH), pagesize=landscape(A4))
        width, height = landscape(A4) 

        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(50, height - 50, f"Relatório: {report_name}")
        
        mycursor.execute(sql_query)
        data = mycursor.fetchall()
        columns = [col[0] for col in mycursor.description]  # Cabeçalhos das colunas
        
        x_start = 50
        y_start = height - 80
        current_y = y_start
        row_spacing = 18
        max_rows_per_page = 40
        row_count = 0

        pdf.setFont("Helvetica-Bold", 10)
        for i, column in enumerate(columns):
            pdf.drawString(x_start + i * 100, current_y, str(column))
        
        current_y -= row_spacing
        row_count += 1
        pdf.setFont("Helvetica", 10)

        for row in data:
            if row_count >= max_rows_per_page:
                pdf.showPage()
                current_y = height - 50
                row_count = 0
                
            for i, value in enumerate(row):
                pdf.drawString(x_start + i * 100, current_y, str(value))
            current_y -= row_spacing
            row_count += 1

        pdf.save()
        print("Relatório criado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao gerar relatório PDF personalizado '{report_name}': {e}")
