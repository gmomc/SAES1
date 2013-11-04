import os
RUTA_PROYECTO = os.path.dirname(os.path.abspath(__file__))
from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField,\
            BAND_WIDTH, Label,Image,Line,ReportGroup,DetailBand
from reportlab.lib.pagesizes import A5,A4,letter
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.lib.colors import navy, yellow, red, purple, orange,\
    green, white, blue

class reporteDeHorario(Report):
    class band_detail(DetailBand):
            height=0.7*cm
            elements=[
                ObjectValue(attribute_name='materia_grupo.grupo',        top=5*cm, left=0.2*cm, style={'fontName': 'Helvetica', 'fontSize':8}),
                ObjectValue(attribute_name='materia_grupo.materia.nombre',top=5*cm, left=1.2*cm, style={'fontName': 'Helvetica', 'fontSize':8}),
                ObjectValue(attribute_name='materia_grupo.horario.lunes',top=5*cm, left=6.0*cm, style={'fontName': 'Helvetica', 'fontSize':8}),
                ObjectValue(attribute_name='materia_grupo.horario.martes',top=5*cm, left=8.0*cm, style={'fontName': 'Helvetica', 'fontSize':8}),
                ObjectValue(attribute_name='materia_grupo.horario.miercoles',top=5*cm, left=10*cm, style={'fontName': 'Helvetica', 'fontSize':8}),
                ObjectValue(attribute_name='materia_grupo.horario.jueves',top=5*cm, left=12*cm, style={'fontName': 'Helvetica', 'fontSize':8}),
                ObjectValue(attribute_name='materia_grupo.horario.viernes',top=5*cm, left=14*cm, style={'fontName': 'Helvetica', 'fontSize':8}),
                ]
    class band_begin(ReportBand):
            height = 1*cm
            elements = [
                Label(text='Escuela Superior de Computo', top=0.1*cm,width=BAND_WIDTH,
                    style={'fontName': 'Helvetica-Bold', 'fontSize': 10, 'alignment': TA_CENTER} ),
            ]
    class band_page_footer(ReportBand):
            height = 0.5*cm
            elements = [
                    Label(text='Documento sin validez oficial', top=0.1*cm),
                    ] 
    class band_summary(ReportBand):
            height = 1.5*cm
            elements = [
                Label(text='Comprobante de Horario', top=0.1*cm,width=BAND_WIDTH,
                    style={'fontName': 'Helvetica-Bold', 'fontSize': 10, 'alignment': TA_CENTER} ),
                     ]    
    class band_page_header(ReportBand):
            height = 1.5*cm
            elements = [ 
                        Label(text="Escuela Superior de Computo", top=0.8*cm, left=0,width=BAND_WIDTH,
                            style={'fontName': 'Helvetica-Bold', 'fontSize': 16, 'alignment': TA_CENTER}),
                        Label(text="Grupo", top=6.8*cm, left=0.2*cm, width=1.5*cm, style={'fontName': 'Helvetica-Bold', 'fontSize':8}),
                        Label(text="Materia", top=6.8*cm, left=1.2*cm, width=1.5*cm, style={'fontName': 'Helvetica-Bold', 'fontSize':8}),
                        Label(text="Lunes", top=6.8*cm, left=6.0*cm, width=1.5*cm, style={'fontName': 'Helvetica-Bold', 'fontSize':8}),
                        Label(text="Martes", top=6.8*cm, left=8.0*cm, width=1.5*cm, style={'fontName': 'Helvetica-Bold', 'fontSize':8}),
                        Label(text="Miercoles", top=6.8*cm, left=10*cm, width=1.5*cm, style={'fontName': 'Helvetica-Bold', 'fontSize':8}),
                        Label(text="Jueves", top=6.8*cm, left=12*cm, width=1.5*cm, style={'fontName': 'Helvetica-Bold', 'fontSize':8}),
                        Label(text="Viernes", top=6.8*cm, left=14*cm, width=1.5*cm, style={'fontName': 'Helvetica-Bold', 'fontSize':8}),

                        #Label(text="Boleta", top=7*cm, left=0.5*cm,width=1.5*cm,style={'fontName': 'Helvetica-Bold', 'fontSize':8}),
                        ]
           
