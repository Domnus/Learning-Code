import tkinter as tk
from random import randint

HEIGHT = 768
WIDTH = 1024

root = tk.Tk()

root.title('Cores em RGB')

cores = []

def inserir():
    _cor = cor.get()
    _codigo = codigo.get()

    cores.append((_cor, _codigo))

def consulta():
    nomeCor = corConsulta.get()
    v = [("True", cor[1]) for cor in cores if cor[0] == nomeCor]
    return v

def _consulta():
    v = consulta()

    list = upper_frame.pack_slaves()
    for l in list:
        l.destroy()

    try:
        if v[0][0] == "True":
            elem = tk.Label(upper_frame, text=f"Código da cor: {v[0][1]}")
            elem.pack()
        else:
            elem = tk.Label(upper_frame, text="Cor inválida!")
            elem.pack()
    except:
        elem = tk.Label(upper_frame, text="Cor inválida!")
        elem.pack()

def listagem():
    list = upper_frame.pack_slaves()
    for l in list:
        l.destroy()

    if cores == []:
        elem = tk.Label(upper_frame, text="Lista vazia!")
        elem.pack()
    else:
        for i in range(len(cores)):
            elem = tk.Label(upper_frame, text=f"Cor: {cores[i][0]} | Código: {cores[i][1]}")
            elem.pack()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='gray')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

inserirB = tk.Button(frame, text='Inserir', command=inserir)
inserirB.pack()

tamanho = tk.Label(frame, text='Cor')
tamanho.place(rely=0.04, relx=0.37)

cor = tk.Entry(frame)
cor.pack()

tamanho2 = tk.Label(frame, text='Código')
tamanho2.place(rely=0.065, relx=0.36)

codigo = tk.Entry(frame)
codigo.pack()

consultaB = tk.Button(frame, text='Consulta', command=_consulta)
consultaB.pack()

corConsulta = tk.Entry(frame)
corConsulta.pack()

listagemB = tk.Button(frame, text='Listagem', command=listagem)
listagemB.pack()

sair = tk.Button(frame, text='Sair do programa', command=quit)
sair.pack()

upper_frame = tk.Frame(root, bg='#14b6c4', bd=10)
upper_frame.place(relx=0.5, rely=0.3, relheight=0.55,
                  relwidth=0.75, anchor='n')


root.mainloop()

