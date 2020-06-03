matriz2 = ''
    for i in range(len(arr)):
        elemento = str(arr[i])
        matriz2 += elemento
        matriz2 += '\n'
    descompactado = tk.Label(upper_frame, text=matriz2, bg='white')
    descompactado.pack()