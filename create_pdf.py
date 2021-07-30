from create_pdf2 import PDF
from tkinter import messagebox


def create_pdf(nome, data_in, data_out):

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=10)

    pdf.create_table(table_data=data_in,
                     title='Dados de Entrada', cell_width='even')
    pdf.ln()
    pdf.create_table(table_data=data_out,
                     title='Dados Calculados', cell_width='even')
    pdf.ln()
    pdf.output(f"{nome}.pdf")
    messagebox.showinfo("Aviso", "Relatório em PDF gerado com sucesso!")
