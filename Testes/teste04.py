import tkinter as tk
from random import randint as rd

HEIGHT = 640
WIDTH = 480

root = tk.Tk()

root.title('Desafio 2')

def inserir():
    global imagem
    global h
    global w
    h = 5
    w = 5
    if h < 20 or w < 20:
        imagem = [0] * h
        for i in range(h):
            imagem[i] = [0] * w
            cond = 0
            while cond < w:
                x = rd(0, 1)
                if x != 0 and x != 1:
                    print('Digite apenas 1 ou 0!')
                else:
                    imagem[i][cond] = x
                    cond += 1
    for i in range(h):
        elem = tk.Label(upper_frame, text=imagem[i], fg='red')
        elem.pack()
        

def compactar():
    compactacao = []
    for i in range(h):
        p, b = 0, 0
        for j in range(w):
            if(imagem[i][j] == 1):
                p += 1
            if(imagem[i][j] == 0):
                b += 1
            if j == w-1 or imagem[i][j] != imagem[i][j+1]:
                if(p>0):
                    compactacao.append(f'{p}P')
            elif(b>0):
                compactacao.append(f'{b}B')    
            p, b = 0, 0
        compactacao.append('0')
    compactacao.append('0')
    compactado = tk.Label(upper_frame, text=compactacao, bg='blue', fg='white')
    compactado.place(rely=0.8, relheight=0.1, relwidth=1)


def descompactar(entry):
    arr = [[]]
    cont = 0
    linhas = 1
    linha_w = 0
    for character in entry:
        if character.isdecimal():
            numero = int(character)
        else:
            letra = character
        if numero == 0:
            arr.append([])
            cont += 1
            linhas += 1
            continue
        try:
            if letra == 'B':
                for i in range(numero):
                    arr[cont].append(0)
            elif letra == 'P':
                for i in range(numero):
                    arr[cont].append(1)
            letra = ''
        except Exception:
            pass
        
    for i in range(1):
        arr.pop()

    for i in range(len(arr)):
        descompactado = tk.Label(upper_frame, text=arr[i], bg='white')
        descompactado.pack()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#baad65')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

inserir_1 = tk.Button(frame, text="1 – Inserir a imagem (criar a matriz (max. 20x20)", bg='black', fg='white', padx=30, command=inserir)
inserir_1.pack()

compactar_2 = tk.Button(frame, text='2 – Compactar a imagem', bg='black', fg='white', padx=40.5, command=compactar)
compactar_2.pack()

descompactar_3 = tk.Button(frame, text='3 – Descompactar a imagem', bg='black', fg='white', padx=30, command=lambda: descompactar(entry.get()))
descompactar_3.pack()

entry = tk.Entry(frame)
entry.pack()

sair_4 = tk.Button(frame, text='4 – Sair do programa', bg='black', fg='white', command=quit, padx=53)
sair_4.pack()

upper_frame = tk.Frame(root, bg='#0bd46f', bd=10)
upper_frame.place(relx=0.5, rely=0.3, relheight=0.55, relwidth=0.75, anchor='n')

label = tk.Label(upper_frame, text='Matriz')
label.pack()


root.mainloop()