from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from pathlib import Path
from datetime import datetime
from db_config import mycursor
from reportlab.pdfbase.pdfmetrics import stringWidth

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

        mycursor.execute(f"SELECT * FROM {table}")
        data = mycursor.fetchall()
        columns = [col[0] for col in mycursor.description]

        # Configurações
        font_name = "Helvetica"
        font_size = 10
        padding = 10
        x_start = 50
        y_start = height - 80
        current_y = y_start
        row_spacing = 16
        max_rows_per_page = 40
        row_count = 0

        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(x_start, height - 50, f"Relatório da Tabela: {table}")

        # Cálculo da largura das colunas
        col_widths = []
        max_width = width - 2 * x_start

        for i, col in enumerate(columns):
            max_text = col
            for row in data:
                value = str(row[i])
                if len(value) > len(max_text):
                    max_text = value
            col_width = stringWidth(str(max_text), font_name, font_size) + padding
            col_widths.append(col_width)

        total_width = sum(col_widths)
        if total_width > max_width:
            ratio = max_width / total_width
            col_widths = [w * ratio for w in col_widths]

        # Cabeçalhos
        pdf.setFont("Helvetica-Bold", font_size)
        x_pos = x_start
        for i, col in enumerate(columns):
            pdf.drawString(x_pos, current_y, str(col))
            x_pos += col_widths[i]

        current_y -= row_spacing
        row_count += 1
        pdf.setFont(font_name, font_size)

        # Linhas de dados
        for row in data:
            if row_count >= max_rows_per_page:
                pdf.showPage()
                current_y = height - 50
                row_count = 0
                pdf.setFont("Helvetica-Bold", font_size)
                x_pos = x_start
                for i, col in enumerate(columns):
                    pdf.drawString(x_pos, current_y, str(col))
                    x_pos += col_widths[i]
                current_y -= row_spacing
                pdf.setFont(font_name, font_size)

            x_pos = x_start
            for i, value in enumerate(row):
                text = str(value)
                pdf.drawString(x_pos, current_y, text[:50])  # Trunca se for muito longo
                x_pos += col_widths[i]
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

        mycursor.execute(sql_query)
        data = mycursor.fetchall()
        columns = [col[0] for col in mycursor.description]

        # Configurações iniciais
        font_name = "Helvetica"
        font_size = 10
        pdf.setFont(font_name, font_size)

        # Cálculo da largura de cada coluna com base no maior conteúdo
        col_widths = []
        max_width = width - 100  # Margens laterais
        padding = 10  # Espaço extra por coluna

        for i, col in enumerate(columns):
            max_text = col  # Começa com o nome da coluna
            for row in data:
                text = str(row[i])
                if len(text) > len(max_text):
                    max_text = text

            col_width = stringWidth(str(max_text), font_name, font_size) + padding
            col_widths.append(col_width)

        # Ajusta proporção caso a soma ultrapasse o tamanho da página
        total_width = sum(col_widths)
        if total_width > max_width:
            ratio = max_width / total_width
            col_widths = [w * ratio for w in col_widths]

        # Cabeçalho
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(50, height - 50, f"Relatório: {report_name}")

        x_start = 50
        y_start = height - 80
        current_y = y_start
        row_spacing = 16
        max_rows_per_page = 40
        row_count = 0

        # Cabeçalhos das colunas
        pdf.setFont("Helvetica-Bold", font_size)
        x_pos = x_start
        for i, col in enumerate(columns):
            pdf.drawString(x_pos, current_y, str(col))
            x_pos += col_widths[i]

        current_y -= row_spacing
        row_count += 1

        # Conteúdo
        pdf.setFont(font_name, font_size)
        for row in data:
            if row_count >= max_rows_per_page:
                pdf.showPage()
                current_y = height - 50
                row_count = 0
                pdf.setFont("Helvetica-Bold", font_size)
                x_pos = x_start
                for i, col in enumerate(columns):
                    pdf.drawString(x_pos, current_y, str(col))
                    x_pos += col_widths[i]
                current_y -= row_spacing
                pdf.setFont(font_name, font_size)

            x_pos = x_start
            for i, value in enumerate(row):
                text = str(value)
                pdf.drawString(x_pos, current_y, text[:50])  # Trunca se for muito longo
                x_pos += col_widths[i]
            current_y -= row_spacing
            row_count += 1

        pdf.save()
        print("Relatório criado com sucesso!")

    except Exception as e:
        print(f"Erro ao gerar relatório PDF personalizado '{report_name}': {e}")