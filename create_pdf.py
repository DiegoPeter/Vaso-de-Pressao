from create_pdf2 import PDF
def create_pdf(nome,P,D,S,E,casco,tampo,t1,t2,Da):

    if casco == 1:
        casco = "Cilíndrico"
    else:
        casco = "Esférico"
    if tampo == 1:
        tampo = "Elipsóidal 2:1"
    elif tampo == 2:
        tampo = "Toro Esférico"
    elif tampo == 3:
        tampo = "Hemisférico"
    elif tampo == 4:
        tampo = "Cônico"
    else:
        tampo = "Toro Cônico"
    data1 = [
    ["Característica", "Valor", "Unidade",], # 'testing','size'],
    ["Pressão de Projeto", f"{P}", "MPa",], # 'testing','size'],
    ["Diâmetro Interno", f"{D}", "mm",], # 'testing','size'],
    ["Tensão Admissível do Material", f"{S}", "MPa",], # 'testing','size'],
    ["Eficiência de Junta", f"{E}", "-",], # 'testing','size'],
    ["Tipo de casco", casco,"-",],
    ["Tipo de Tampos", tampo,"-",],
    ]


    data2 = [
    ["Característica", "Valor", "Unidade",], # 'testing','size'],
    ["Espessura mínima do costado", f"{t1}", "mm",], # 'testing','size'],
    ["Espessura mínima dos tampos", f"{t2}", "mm",], # 'testing','size'],
    ["Diâmetro das aberturas", f"{Da}", "mm",], # 'testing','size'],     
    ]  
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=10)

    pdf.create_table(table_data = data1,title='Dados de Entrada', cell_width='even')
    pdf.ln()
    pdf.create_table(table_data = data2,title='Dados Calculados',cell_width='even',x_start=25)
    pdf.ln()
    pdf.output(f"{nome}.pdf")