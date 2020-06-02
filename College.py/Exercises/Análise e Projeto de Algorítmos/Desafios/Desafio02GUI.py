import tkinter as tk

HEIGHT = 640
WIDTH = 480

root = tk.Tk()

root.title('Desafio 2')

def criar_matriz(entry):
    imagem = []
    h, w = input('Digite o tamanho da imagem [HxW] -> ').split('x')
    h = int(h)
    w = int(w)
    if h > 20 or w > 20:
        print('A matriz não deve ultrapassar 20x20')
    else:
        print('Digite os valores da matriz:')
        imagem = [0] * h
        for i in range(h):
            imagem[i] = [0] * w
            cond = 0
            while cond < w:
                x = randint(0, 1)
                if x != 0 and x != 1:
                    print('Digite apenas 1 ou 0!')
                else:
                    imagem[i][cond] = x
                    cond += 1
    print('=' * len(imagem) * 2)        
    for i in range(h):
        for j in range(w):
            print(f'{imagem[i][j]}', end=' ')
            print()
    print('=' * len(imagem) * 2)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#baad65')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

inserir = tk.Button(frame, text="1 – Inserir a imagem (criar a matriz (max. 20x20)", bg='black', fg='white')
inserir.pack()

entry = tk.Entry(frame)
entry.pack()

compactar = tk.Button(frame, text='2 – Compactar a imagem', bg='black', fg='white')
compactar.pack()

descompactar = tk.Button(frame, text='3 – Descompactar a imagem', bg='black', fg='white')
descompactar.pack()

sair = tk.Button(frame, text='4 – Sair do programa', bg='black', fg='white', command=quit)
sair.pack()

upper_frame = tk.Frame(root, bg='#0bd46f', bd=10)
upper_frame.place(relx=0.5, rely=0.3, relheight=0.55, relwidth=0.75, anchor='n')

label = tk.Label(upper_frame, text='Matriz')
label.pack()


root.mainloop()