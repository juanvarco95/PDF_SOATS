from os import name
import tkinter as tk
from reportlab.pdfgen import canvas

raiz = tk.Tk()
raiz.title("Momentum Seguros SOAT")
raiz.geometry('400x200')


#creamos el componente frame
frame = tk.Frame(raiz)
frame.config(width=600,height=600)
frame.pack()


lbl = tk.Label(frame, text = "Nombre")
lbl.grid(column=0, row=0)

txt1 = tk.Entry(frame, width = 20)
txt1.grid(column = 1, row = 0)

lb2 = tk.Label(frame, text = "Placa")
lb2.grid(column=0, row=1)

txt2 = tk.Entry(frame, width = 20)
txt2.grid(column = 1, row = 1)

lb3 = tk.Label(frame, text = "Fecha")
lb3.grid(column=0, row=2)

txt3 = tk.Entry(frame, width = 20)
txt3.grid(column = 1, row = 2)

lb4 = tk.Label(frame, text = "Precio")
lb4.grid(column=0, row=3)

txt4 = tk.Entry(frame, width = 20)
txt4.grid(column = 1, row = 3)

lb5 = tk.Label(frame, text = "")
lb5.grid(column=1, row=11)


def generarPDF():
    
    lb5.configure(text = "Generando PDF")
    print(txt1.get() + ".pdf")
    pdf = canvas.Canvas("{name}_SOAT.pdf".format(name = txt1.get(), pagesize = [400,400]))
    pdf.setFillColorRGB(0/255, 86/255, 103/255)
    pdf.setFont("Helvetica", 15)

#Imagenes
    pdf.drawImage("plantilla.png", 0, 0, 600, 400)

#Textos
    pdf.drawString(305, 310, str(txt1.get()).upper())
    pdf.drawString(408, 250, str(txt2.get()).upper())
    pdf.drawString(273, 230, txt3.get())
    pdf.drawString(300, 150, txt4.get())

    pdf.save()

btn = tk.Button(frame, text = "Generar PDF", command = generarPDF)
btn.grid(column = 1, row = 10)




raiz.mainloop()