# A notebook for different topics of Python learning path, with several pages for each topic

from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Arial', style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align='C')

    # add lines for parent pages
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # Set footer to parent pages
    pdf.ln(265)
    pdf.set_font(family='Arial', style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], border=0, ln=1, align='R')

    for i in range(1, row["Pages"]):
        pdf.add_page()

        # Set footer to children pages
        pdf.ln(277)
        pdf.set_font(family='Arial', style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], border=0, ln=1, align='R')

        # Add lines for parent pages
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
