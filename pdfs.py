from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from pathlib import Path
from datetime import datetime

BASE_PATH = Path(__file__).parent
RELATORIO_PDF_PATH = BASE_PATH / "relatorios_pdf"
RELATORIO_PDF_PATH.mkdir(exist_ok=True)




def criar_relatorio_completo_pdf(table):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    CANVAS_PATH = RELATORIO_PDF_PATH / f'{table}_relatorio_{timestamp}.pdf'
    
    arquivo = canvas.Canvas(str(CANVAS_PATH), pagesize=A4)
    w, h = A4
    arquivo.drawString(50, h - 50, f"Relatório referente a {table}")
    
    
    
    

    arquivo.save()
    
    
criar_relatorio_completo_pdf("produto")