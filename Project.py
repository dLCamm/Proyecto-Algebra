import customtkinter
import numpy as np
from tkinter import messagebox
from tkinter import *
from numpy.linalg import det, inv
from numpy import matrix, zeros, size
import random


def cifrado():
    root_cifrado = customtkinter.CTk()
    customtkinter.set_appearance_mode('Light')
    customtkinter.set_default_color_theme('blue')

    root_cifrado.title("Cifrado")

    lb_insertar = customtkinter.CTkLabel(master=root_cifrado, text='Matriz', font=("Arial", 15),
                                         text_color='Black')
    lb_insertar.pack(pady=12, padx=12)
    lb_insertar.place(x=280, y=85)

    bt_insertar = customtkinter.CTkEntry(master=root_cifrado, placeholder_text='Inserte el numero de columnas',
                                         width=300, fg_color='White')
    bt_insertar.pack(pady=12, padx=10)
    bt_insertar.place(x=280, y=112)



    def crear_matriz(frame, num):
        matriz = []
        for i in range(3):
            fila = []
            for j in range(num):
                entry = customtkinter.CTkEntry(master=frame, width=10)
                entry.grid(row=i, column=j)
                fila.append(entry)
            matriz.append(fila)




        return matriz


    def mostrar_matriz():
        global matriz_one

        num = int(bt_insertar.get())
        if num > 15:
            messagebox.showerror("Error", 'EXCEDIO', parent=root_cifrado)
        else:
            matriz_one = crear_matriz(frame, num)



    def calcular_llave(frame):
        llave = []
        for i in range(3):
            fila = []
            for j in range(3):
                entry = customtkinter.CTkEntry(master=frame, width=10)
                entry.grid(row=i, column=j)
                fila.append(entry)
            llave.append(fila)

        return llave

    def mostrar_matriz_llave():
        global matriz_two
        matriz_two = calcular_llave(frame)

    def calcular_cifrado():
        global result
        global llaves
        num_columnas = len(matriz_one[0])

        # Convertir las matrices de tkinter a numpy arrays para la multiplicación matricial
        matriz = np.array([[int(entry.get()) for entry in fila] for fila in matriz_one])
        llaves = np.array([[int(entry.get()) for entry in fila] for fila in matriz_two])

        # Multiplicar las matrices
        resultado = np.matmul(llaves, matriz)
        result = np.array(resultado)

        # Mostrar el resultado en un messagebox
        messagebox.showinfo("Cifrado", "El Cifrado es:\n" + str(resultado))

    def calcular_descifrado():
        global matriz_one
        global resultado

        # Obtener la matriz generada
        matriz_generada = result
        llaveee = np.array([[int(entry.get()) for entry in fila] for fila in matriz_two])

        # Obtener la llave

        # Calcular la inversa de la llave
        try:
            llave_inversa = inv(llaveee)
        except np.linalg.LinAlgError:
            messagebox.showerror("Error", "La matriz llave no es invertible")
            return

        # Multiplicar la inversa de la llave por la matriz generada
        resultado_descifrado = np.matmul(llave_inversa, matriz_generada)

        # Mostrar el resultado en un messagebox
        messagebox.showinfo("Descifrado", "El mensaje original es:\n" + str(resultado_descifrado))


    bt_c = customtkinter.CTkButton(master=root_cifrado, text='Crear matriz', command=mostrar_matriz)
    bt_c.pack(pady=12, padx=10)
    bt_c.place(x=280, y=175)

    bt_cif = customtkinter.CTkButton(master=root_cifrado, text='Calcular cifrado', command=calcular_cifrado)
    bt_cif.pack(pady=12, padx=10)
    bt_cif.place(x=500, y=175)

    bt_cif = customtkinter.CTkButton(master=root_cifrado, text='Mostrar llave', command=mostrar_matriz_llave)
    bt_cif.pack(pady=12, padx=10)
    bt_cif.place(x=800, y=175)

    bt_descif = customtkinter.CTkButton(master=root_cifrado, text='Calcular descifrado', command=calcular_descifrado)
    bt_descif.pack(pady=12, padx=10)
    bt_descif.place(x=650, y=175)


    frame = customtkinter.CTkFrame(master=root_cifrado, fg_color="White", width=1000, height=600)
    frame.pack(pady=10, padx=100, fill='both', expand=True, side='right')
    frame.place(y=250, x=280)


    return frame

















def crear_matriz(frame, num):
    matriz = []
    for i in range(num):
        fila = []
        for j in range(num):
            entry = customtkinter.CTkEntry(master=frame, width=10)
            entry.grid(row=i, column=j)
            fila.append(entry)
        matriz.append(fila)
    return matriz

def obtener_valores_matriz(matriz):
    valores = []
    for fila in matriz:
        fila_valores = []
        for entry in fila:
            fila_valores.append(float(entry.get()))
        valores.append(fila_valores)
    return valores

def mostrar_procedimiento_inversa(matriz):
    try:
        matriz_np = np.array(matriz)
        # Crear la matriz identidad del mismo tamaño
        matriz_identidad = np.identity(len(matriz))
        # Concatenar la matriz original y la identidad para formar la matriz
        matriz_extendida = np.concatenate((matriz_np, matriz_identidad), axis=1)

        # Limpiar el frame antes de mostrar el procedimiento
        for widget in frame.winfo_children():
            widget.destroy()

        # Mostrar la matriz con el metodo gauss
        texto_procedimiento = customtkinter.CTkLabel(master=frame, text="Matriz Extendida Inicial:")
        texto_procedimiento.pack()
        for fila in matriz_extendida:
            texto_procedimiento = customtkinter.CTkLabel(master=frame, text=str(fila))
            texto_procedimiento.pack()


        # Mostrar la matriz inversa
        matriz_inv = inv(matriz)
        texto_procedimiento = customtkinter.CTkLabel(master=frame, text="\nMatriz Inversa:")
        texto_procedimiento.pack()
        texto_procedimiento = customtkinter.CTkLabel(master=frame, text=str(matriz_inv))
        texto_procedimiento.pack()

    except np.linalg.LinAlgError:
        messagebox.showerror("Error", "La matriz no es invertible.", parent=root_inversa)

def inversa_interact():
    global root_inversa
    global frame


    root_inversa = customtkinter.CTk()
    customtkinter.set_appearance_mode('Light')
    customtkinter.set_default_color_theme('blue')

    root_inversa.title("Matriz inversa")

    lb_insertar = customtkinter.CTkLabel(master=root_inversa, text='Filas o columnas', font=("Arial", 15), text_color='Black')
    lb_insertar.pack(pady=12, padx=12)
    lb_insertar.place(x=280, y=85)

    bt_insertar = customtkinter.CTkEntry(master=root_inversa, placeholder_text='Inserte el numero de columnas o filas', width=300, fg_color='White')
    bt_insertar.pack(pady=12, padx=10)
    bt_insertar.place(x=280, y=112)

    def mostrar_matriz():
        num = int(bt_insertar.get())
        if num > 4:
            messagebox.showerror("Error", 'EXCEDIO', parent=root_inversa)
        else:
            matriz = crear_matriz(frame, num)
            global matriz_actual
            matriz_actual = matriz


    bt_crear = customtkinter.CTkButton(master=root_inversa, text='Crear matriz', command=mostrar_matriz)
    bt_crear.pack(pady=12, padx=10)
    bt_crear.place(x=280, y=175)

    def calcular_inversa():
        matriz = obtener_valores_matriz(matriz_actual)
        mostrar_procedimiento_inversa(matriz)

    bt_calc = customtkinter.CTkButton(master=root_inversa, text='Calcular inversa', command=calcular_inversa)
    bt_calc.pack(pady=12, padx=10)
    bt_calc.place(x=500, y=175)

    frame = customtkinter.CTkFrame(master=root_inversa, fg_color="White", width=1000, height=600)
    frame.pack(pady=10, padx=100, fill='both', expand=True, side='right')
    frame.place(y=250, x=280)



    return root_inversa


def cadenas_markov():
    root_markov = customtkinter.CTk()
    customtkinter.set_appearance_mode('Light')
    customtkinter.set_default_color_theme('blue')

    root_markov.title('Cadena de Markov')

    lb_ins = customtkinter.CTkLabel(master=root_markov, text='Matriz', font=("Arial", 15), text_color='Black')
    lb_ins.pack(pady=12, padx=12)
    lb_ins.place(x=280, y=85)

    bt_insert = customtkinter.CTkEntry(master=root_markov, placeholder_text='Inserte el numero de columnas o filas', width=300, fg_color='White')
    bt_insert.pack(pady=12, padx=10)
    bt_insert.place(x=280, y=112)

    num = customtkinter.CTkEntry(master=root_markov, placeholder_text='Ingrese el periodo', width=300, fg_color='White')
    num.pack(pady=12, padx=10)
    num.place(x=1000, y=175)

    def crear_matriz(frame, num):
        matriz = []
        for i in range(num):
            fila = []
            for j in range(num):
                entry = customtkinter.CTkEntry(master=frame, width=10)
                entry.grid(row=i, column=j)
                fila.append(entry)
            matriz.append(fila)
        return matriz

    def mostrar_matriz():
        global matriz_one
        num = int(bt_insert.get())
        if num > 4:
            messagebox.showerror("Error", 'EXCEDIO', parent=root_markov)
        else:
            matriz_one = crear_matriz(frame, num)


    def crear_matrizinicial(frame, num):
        matriz = []
        for i in range(3):
            fila = []
            for j in range(1):
                entry = customtkinter.CTkEntry(master=frame, width=10)
                entry.grid(row=i, column=j)
                fila.append(entry)
            matriz.append(fila)
        return matriz

    def mostrar_matrizinicial():
        global matriz_two
        matriz_two = crear_matrizinicial(frame, num)

    def calcular_cadena():
        global matriz_one, matriz_two

        # Convertir las entradas de tkinter a matrices numpy para operaciones de matriz
        matriz_transicion = np.array([[float(entry.get()) for entry in row] for row in matriz_one])
        vector_estado_inicial = np.array([[float(entry.get()) for entry in row] for row in matriz_two])

        periodos = int(num.get())

        # Inicializar el resultado con el vector de estado inicial
        resultado = vector_estado_inicial

        # Multiplicar sucesivamente el resultado por la matriz de transición
        for _ in range(1, periodos + 1):
            resultado_iter = np.dot(matriz_transicion, vector_estado_inicial)
            vector_estado_inicial = resultado_iter
        rest = str(resultado_iter)

        # Mostrar el resultado en un messagebox
        messagebox.showerror("Resultado", f'Las probabilidades son: \n {rest}', parent=root_markov)

    bt_c = customtkinter.CTkButton(master=root_markov, text='Crear matriz', command=mostrar_matriz)
    bt_c.pack(pady=12, padx=10)
    bt_c.place(x=280, y=175)


    bt_c = customtkinter.CTkButton(master=root_markov, text='Crear matriz de estado inicial', command=mostrar_matrizinicial)
    bt_c.pack(pady=12, padx=10)
    bt_c.place(x=700, y=175)

    bt_suma = customtkinter.CTkButton(master=root_markov, text='Calcular', command=calcular_cadena)
    bt_suma.pack(pady=12, padx=10)
    bt_suma.place(x=700, y=120)

    frame = customtkinter.CTkFrame(master=root_markov, fg_color="White", width=1000, height=600)
    frame.pack(pady=10, padx=100, fill='both', expand=True, side='right')
    frame.place(y=250, x=280)

    return frame


def operaciones_matrices():
    root_opmat = customtkinter.CTk()
    customtkinter.set_appearance_mode('Light')
    customtkinter.set_default_color_theme('blue')

    root_opmat.title('Operaciones entre matrices')

    lb_ins = customtkinter.CTkLabel(master=root_opmat, text='Filas o columnas', font=("Arial", 15), text_color='Black')
    lb_ins.pack(pady=12, padx=12)
    lb_ins.place(x=280, y=85)

    matriz_one = None
    matriz_two = None

    def crear_matriz(frame, num):
        matriz = []
        for i in range(num):
            fila = []
            for j in range(num):
                entry = customtkinter.CTkEntry(master=frame, width=10)
                entry.grid(row=i, column=j)
                fila.append(entry)
            matriz.append(fila)
        return matriz

    def mostrar_matriz_one():
        nonlocal matriz_one
        num = int(bt_ins.get())
        if num > 4:
            messagebox.showerror("Error", 'EXCEDIO', parent=root_opmat)
        else:
            matriz_one = crear_matriz(frame, num)

    def mostrar_matriz_two():
        nonlocal matriz_two
        num = int(bt_ins.get())
        if num > 4:
            messagebox.showerror("Error", 'EXCEDIO', parent=root_opmat)
        else:
            matriz_two = crear_matriz(frame, num)

    def suma_matrices():
        if matriz_one and matriz_two:
            num = int(bt_ins.get())
            result = [[0 for _ in range(num)] for _ in range(num)]
            p = []
            for i in range(num):
                fila_proc = []
                for j in range(num):
                    val1 = int(matriz_one[i][j].get())
                    val2 = int(matriz_two[i][j].get())
                    result[i][j] = val1 + val2
                    fila_proc.append(f"{val1} + {val2} = {result[i][j]}")
                p.append(fila_proc)
            mostrar_resultado(result, p)
        else:
            messagebox.showerror("Error", 'No se han creado las matrices', parent=root_opmat)

    def resta_matrices():
        if matriz_one and matriz_two:
            num = int(bt_ins.get())
            result = [[0 for _ in range(num)] for _ in range(num)]
            p = []
            for i in range(num):
                fila_proc = []
                for j in range(num):
                    val1 = int(matriz_one[i][j].get())
                    val2 = int(matriz_two[i][j].get())
                    result[i][j] = val1 - val2
                    fila_proc.append(f"{val1} - {val2} = {result[i][j]}")
                p.append(fila_proc)
            mostrar_resultado(result, p)
        else:
            messagebox.showerror("Error", 'No se han creado las matrices', parent=root_opmat)

    def multiplicacion_matrices():
        if matriz_one and matriz_two:
            num = int(bt_ins.get())
            result = [[0 for _ in range(num)] for _ in range(num)]
            p = []
            for i in range(num):
                fila_proc = []
                for j in range(num):
                    calc_proc = []
                    for k in range(num):
                        val1 = int(matriz_one[i][k].get())
                        val2 = int(matriz_two[k][j].get())
                        calc = val1 * val2
                        result[i][j] += calc
                        calc_proc.append(f"{val1} * {val2} = {calc}")
                    fila_proc.append(" + ".join(calc_proc))
                p.append(fila_proc)
            mostrar_resultado(result, p)
        else:
            messagebox.showerror("Error", 'No se han creado las matrices', parent=root_opmat)

    def mostrar_resultado(result, procedure):
        for widget in frame.winfo_children():
            widget.destroy()

        # Display procedure horizontally
        if p:
            for i, fila_proc in enumerate(p):
                p_text = ", ".join(fila_proc)
                label = customtkinter.CTkLabel(master=frame, text=p_text, font=("Arial", 12), text_color='Black')
                label.grid(row=i, column=0, sticky="w")



        num_rows = len(result)
        num_cols = len(result[0])
        for i in range(num_rows):
            for j in range(num_cols):
                label = customtkinter.CTkLabel(master=frame, text=str(result[i][j]), font=("Arial", 12), text_color='Black')
                label.grid(row=i+ len(procedure), column=j, padx=5, pady=5)


    bt_ins = customtkinter.CTkEntry(master=root_opmat, placeholder_text='Inserte el numero de columnas o filas',
                                         width=300, fg_color='White')
    bt_ins.pack(pady=12, padx=10)
    bt_ins.place(x=280, y=112)

    bt_c = customtkinter.CTkButton(master=root_opmat, text='Crear matriz 1', command=mostrar_matriz_one)
    bt_c.pack(pady=12, padx=10)
    bt_c.place(x=280, y=175)

    bt_c2 = customtkinter.CTkButton(master=root_opmat, text='Crear matriz 2', command=mostrar_matriz_two)
    bt_c2.pack(pady=12, padx=10)
    bt_c2.place(x=280, y=210)

    bt_suma = customtkinter.CTkButton(master=root_opmat, text='Calcular Suma', command=suma_matrices)
    bt_suma.pack(pady=12, padx=10)
    bt_suma.place(x=500, y=175)

    bt_resta = customtkinter.CTkButton(master=root_opmat, text='Calcular resta', command=resta_matrices)
    bt_resta.pack(pady=12, padx=10)
    bt_resta.place(x=650, y=175)

    bt_multiplicacion= customtkinter.CTkButton(master=root_opmat, text='Calcular multiplicacion', command=multiplicacion_matrices)
    bt_multiplicacion.pack(pady=12, padx=10)
    bt_multiplicacion.place(x=800, y=175)

    frame = customtkinter.CTkFrame(master=root_opmat, fg_color="White", width=1000, height=600)
    frame.pack(pady=10, padx=100, fill='both', expand=True, side='right')
    frame.place(y=250, x=280)

    return frame


def determinante():
    root_det = customtkinter.CTk()
    customtkinter.set_appearance_mode('Light')
    customtkinter.set_default_color_theme('blue')

    root_det.title('Determinante de una Matriz')

    lb_ins = customtkinter.CTkLabel(master=root_det, text='Matriz', font=("Arial", 15), text_color='Black')
    lb_ins.pack(pady=12, padx=12)
    lb_ins.place(x=280, y=85)

    bt_ins = customtkinter.CTkEntry(master=root_det, placeholder_text='Inserte el numero de columnas o filas',
                                    width=300, fg_color='White')
    bt_ins.pack(pady=12, padx=10)
    bt_ins.place(x=280, y=112)


    def crear_matriz(frame, num):
        matriz = []
        for i in range(num):
            fila = []
            for j in range(num):
                entry = customtkinter.CTkEntry(master=frame, width=10)
                entry.grid(row=i, column=j)
                fila.append(entry)
            matriz.append(fila)
        return matriz

    def mostrar_matriz():
        global matriz_one
        num = int(bt_ins.get())
        if num > 4:
            messagebox.showerror("Error", 'EXCEDIO', parent=root_det)
        else:
            matriz_one = crear_matriz(frame, num)

    def calcular_determinante():
        # Obtener la matriz ingresada por el usuario
        matriz = []
        for fila in matriz_one:
            valores_fila = [float(entry.get()) for entry in fila]
            matriz.append(valores_fila)
        matriz = np.array(matriz)

        # Verificar si la matriz es cuadrada
        if matriz.shape[0] != matriz.shape[1]:
            messagebox.showerror("Error", 'La matriz debe ser cuadrada', parent=root_det)
            return

        # Verificar si la matriz es de tamaño 2x2 o 3x3 para aplicar el método de Sarrus
        if matriz.shape[0] not in [2, 3]:
            messagebox.showerror("Error", 'El método de Sarrus solo se aplica a matrices 2x2 y 3x3', parent=root_det)
            return

        # Calcular la determinante utilizando el método de Sarrus
        if matriz.shape[0] == 2:
            det = matriz[0, 0] * matriz[1, 1] - matriz[0, 1] * matriz[1, 0]
            procedimiento = f'Determinante = ({matriz[0, 0]} * {matriz[1, 1]}) - ({matriz[0, 1]} * {matriz[1, 0]})\n' \
                            f'             = {matriz[0, 0] * matriz[1, 1]} - {matriz[0, 1] * matriz[1, 0]}\n' \
                            f'             = {det}'
        else:
            det = (matriz[0, 0] * matriz[1, 1] * matriz[2, 2] +
                   matriz[0, 1] * matriz[1, 2] * matriz[2, 0] +
                   matriz[0, 2] * matriz[1, 0] * matriz[2, 1] -
                   matriz[0, 2] * matriz[1, 1] * matriz[2, 0] -
                   matriz[0, 1] * matriz[1, 0] * matriz[2, 2] -
                   matriz[0, 0] * matriz[1, 2] * matriz[2, 1])
            procedimiento = f'Determinante = ({matriz[0, 0]} * {matriz[1, 1]} * {matriz[2, 2]}) + \n' \
                            f'              ({matriz[0, 1]} * {matriz[1, 2]} * {matriz[2, 0]}) + \n' \
                            f'              ({matriz[0, 2]} * {matriz[1, 0]} * {matriz[2, 1]}) - \n' \
                            f'              ({matriz[0, 2]} * {matriz[1, 1]} * {matriz[2, 0]}) - \n' \
                            f'              ({matriz[0, 1]} * {matriz[1, 0]} * {matriz[2, 2]}) - \n' \
                            f'              ({matriz[0, 0]} * {matriz[1, 2]} * {matriz[2, 1]})\n' \
                            f'             = {det}'

        # Limpiar el frame antes de mostrar el procedimiento
        for widget in frame.winfo_children():
            widget.destroy()

        # Mostrar el procedimiento en el frame
        procedimiento_label = customtkinter.CTkLabel(master=frame, text=procedimiento, font=("Arial", 12),
                                                     text_color='Black')
        procedimiento_label.pack(pady=5, padx=5, anchor='w')

        # Mostrar el resultado en un messagebox
        messagebox.showinfo("Resultado", f'La determinante de la matriz es: {det}', parent=root_det)


    bt_c = customtkinter.CTkButton(master=root_det, text='Crear matriz', command=mostrar_matriz)
    bt_c.pack(pady=12, padx=10)
    bt_c.place(x=280, y=175)

    bt_suma = customtkinter.CTkButton(master=root_det, text='Calcular determinante', command=calcular_determinante)
    bt_suma.pack(pady=12, padx=10)
    bt_suma.place(x=500, y=175)


    frame = customtkinter.CTkFrame(master=root_det, fg_color="White", width=1000, height=600)
    frame.pack(pady=10, padx=100, fill='both', expand=True, side='right')
    frame.place(y=250, x=280)

    return frame


def rango():
    root_rango = customtkinter.CTk()
    customtkinter.set_appearance_mode('Light')
    customtkinter.set_default_color_theme('blue')

    root_rango.title('Rango de una matriz')

    lb_ins = customtkinter.CTkLabel(master=root_rango, text='Filas o columnas', font=("Arial", 15), text_color='Black')
    lb_ins.pack(pady=12, padx=12)
    lb_ins.place(x=280, y=85)

    bt_ins = customtkinter.CTkEntry(master=root_rango, placeholder_text='Inserte el numero de columnas o filas',
                                    width=300, fg_color='White')
    bt_ins.pack(pady=12, padx=10)
    bt_ins.place(x=280, y=112)

    def crear_matriz(frame, num):
        matriz = []
        for i in range(num):
            fila = []
            for j in range(num):
                entry = customtkinter.CTkEntry(master=frame, width=10)
                entry.grid(row=i, column=j)
                fila.append(entry)
            matriz.append(fila)
        return matriz

    def mostrar_matriz():
        global matriz_one
        num = int(bt_ins.get())
        if num > 4:
            messagebox.showerror("Error", 'EXCEDIO', parent=root_rango)
        else:
            matriz_one = crear_matriz(frame, num)

    def calcular_rango():
        matriz_numerica = []
        for fila in matriz_one:
            fila_numerica = []
            for entry in fila:
                try:
                    valor = float(entry.get())
                except ValueError:
                    valor = 0
                fila_numerica.append(valor)
            matriz_numerica.append(fila_numerica)
        matriz_np = np.array(matriz_numerica)
        rango = np.linalg.matrix_rank(matriz_np)
        messagebox.showinfo("Rango de la matriz", f'El rango de la matriz es: {rango}', parent=root_rango)


    bt_c = customtkinter.CTkButton(master=root_rango, text='Crear matriz', command=mostrar_matriz)
    bt_c.pack(pady=12, padx=10)
    bt_c.place(x=280, y=175)

    bt_suma = customtkinter.CTkButton(master=root_rango, text='Calcular el rango', command=calcular_rango)
    bt_suma.pack(pady=12, padx=10)
    bt_suma.place(x=500, y=175)

    frame = customtkinter.CTkFrame(master=root_rango, fg_color="White", width=1000, height=600)
    frame.pack(pady=10, padx=100, fill='both', expand=True, side='right')
    frame.place(y=250, x=280)

    return frame


def operaciones_vectores():
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode('Light')
    customtkinter.set_default_color_theme('blue')

    root.title('Operaciones entre vectores')

    lb_ins = customtkinter.CTkLabel(master=root, text='Vectores', font=("Arial", 15), text_color='Black')
    lb_ins.pack(pady=12, padx=12)
    lb_ins.place(x=280, y=85)

    bt_ins = customtkinter.CTkEntry(master=root, placeholder_text='Inserte el numero de columnas',
                                    width=300, fg_color='White')
    bt_ins.pack(pady=12, padx=10)
    bt_ins.place(x=280, y=112)

    def crear_vectores():
        try:
            num_columnas = int(bt_ins.get())
            if num_columnas <= 0:
                raise ValueError("El número de columnas debe ser mayor que cero.")

            # Limpiar el frame antes de crear los nuevos vectores
            for widget in frame.winfo_children():
                widget.destroy()

            # Crear etiquetas y campos de entrada para los elementos de los vectores
            for i in range(num_columnas):
                lb_vector1 = customtkinter.CTkLabel(master=frame, text=f'Vector 1 - Elemento {i + 1}:', width=100)
                lb_vector1.grid(row=i, column=0, padx=10, pady=5)
                entry_vector1 = customtkinter.CTkEntry(master=frame, placeholder_text='Inserte un número')
                entry_vector1.grid(row=i, column=1, padx=10, pady=5)

                lb_vector2 = customtkinter.CTkLabel(master=frame, text=f'Vector 2 - Elemento {i + 1}:', width=100)
                lb_vector2.grid(row=i, column=2, padx=10, pady=5)
                entry_vector2 = customtkinter.CTkEntry(master=frame, placeholder_text='Inserte un número')
                entry_vector2.grid(row=i, column=3, padx=10, pady=5)

            # Función para obtener los valores ingresados por el usuario
            def guardar():
                vector1 = [float(entry_vector1.get()) for entry_vector1 in frame.winfo_children() if
                           isinstance(entry_vector1, customtkinter.CTkEntry) and entry_vector1.grid_info()[
                               'column'] == 1]
                vector2 = [float(entry_vector2.get()) for entry_vector2 in frame.winfo_children() if
                           isinstance(entry_vector2, customtkinter.CTkEntry) and entry_vector2.grid_info()[
                               'column'] == 3]
                print("Vector 1:", vector1)
                print("Vector 2:", vector2)
                bt_calcular.destroy()

            bt_calcular = customtkinter.CTkButton(master=root, text='Guardar', command=guardar)
            bt_calcular.pack(pady=12, padx=10)
            bt_calcular.place(x=280, y=210)


        except ValueError as e:
            # Manejar el caso en que el usuario ingrese un valor no válido
            messagebox.showerror("Error", str(e))

    def sumar_vectores():
        try:
            vector1 = [float(entry_vector1.get()) for entry_vector1 in frame.winfo_children() if
                       isinstance(entry_vector1, customtkinter.CTkEntry) and entry_vector1.grid_info()['column'] == 1]
            vector2 = [float(entry_vector2.get()) for entry_vector2 in frame.winfo_children() if
                       isinstance(entry_vector2, customtkinter.CTkEntry) and entry_vector2.grid_info()['column'] == 3]

            if len(vector1) != len(vector2):
                raise ValueError("Los vectores deben tener la misma longitud para poder sumarlos.")

            suma = [v1 + v2 for v1, v2 in zip(vector1, vector2)]
            print("Resultado de la suma:", suma)

            # Mostrar el procedimiento y el resultado en el frame
            for widget in frame.winfo_children():
                widget.destroy()

            lb_procedimiento = customtkinter.CTkLabel(master=frame, text="Procedimiento para la suma:",
                                                      font=("Arial", 12), width=100)
            lb_procedimiento.pack(pady=5, padx=10)

            for i, (v1, v2) in enumerate(zip(vector1, vector2)):
                lb_paso = customtkinter.CTkLabel(master=frame, text=f'Paso {i + 1}: {v1} + {v2} = {v1 + v2}', width=100)
                lb_paso.pack(pady=5, padx=10)

            lb_resultado = customtkinter.CTkLabel(master=frame, text=f'Resultado de la suma: {suma}',
                                                  font=("Arial", 12), width=100)
            lb_resultado.pack(pady=5, padx=10)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def producto_punto():

        try:
            vector1 = [float(entry_vector1.get()) for entry_vector1 in frame.winfo_children() if
                       isinstance(entry_vector1, customtkinter.CTkEntry) and entry_vector1.grid_info()['column'] == 1]
            vector2 = [float(entry_vector2.get()) for entry_vector2 in frame.winfo_children() if
                       isinstance(entry_vector2, customtkinter.CTkEntry) and entry_vector2.grid_info()['column'] == 3]

            if len(vector1) != len(vector2):
                raise ValueError("Los vectores deben tener la misma longitud para calcular el producto punto.")

            producto = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
            print("Resultado del producto punto:", producto)

            # Mostrar el procedimiento y el resultado en el frame
            for widget in frame.winfo_children():
                widget.destroy()

            lb_procedimiento = customtkinter.CTkLabel(master=frame, text="Procedimiento para el producto punto:",
                                                      font=("Arial", 12), width=100)
            lb_procedimiento.pack(pady=5, padx=10)

            for i, (v1, v2) in enumerate(zip(vector1, vector2)):
                lb_paso = customtkinter.CTkLabel(master=frame, text=f'Paso {i + 1}: {v1} * {v2} = {v1 * v2}', width=100)
                lb_paso.pack(pady=5, padx=10)

            lb_resultado = customtkinter.CTkLabel(master=frame, text=f'Resultado del producto punto: {producto}',
                                                  font=("Arial", 12), width=100)
            lb_resultado.pack(pady=5, padx=10)

        except ValueError as e:
            messagebox.showerror("Error", str(e))


    bt_c = customtkinter.CTkButton(master=root, text='Crear vectores', command=crear_vectores)
    bt_c.pack(pady=12, padx=10)
    bt_c.place(x=280, y=175)

    bt_suma = customtkinter.CTkButton(master=root, text='Calcular Suma', command=sumar_vectores)
    bt_suma.pack(pady=12, padx=10)
    bt_suma.place(x=500, y=175)

    bt_resta = customtkinter.CTkButton(master=root, text='Calcular producto punto', command=producto_punto)
    bt_resta.pack(pady=12, padx=10)
    bt_resta.place(x=665, y=175)


    frame = customtkinter.CTkFrame(master=root, fg_color="White", width=1000, height=600)
    frame.pack(pady=10, padx=100, fill='both', expand=True, side='right')
    frame.place(y=250, x=280)

    return frame


def main_interact():
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode('Light')
    customtkinter.set_default_color_theme('blue')

    titulo_enventana = customtkinter.CTkLabel(root, text='ALGEBRA LINEAL', font=('Times New Roman', 20))
    titulo_enventana.pack()
    titulo_enventana.place(x=750, y=150)

    root.title("MENU")
    button_1 = customtkinter.CTkButton(master=root, text='Operaciones entre matrices', height=125, width=250,
                                       font=("Arial", 15),
                                       fg_color="#3E4446", command=operaciones_matrices)
    button_2 = customtkinter.CTkButton(master=root, text='Matriz Inversa', height=125, width=250, font=("Arial", 15),
                                       fg_color="#3E4446", command=inversa_interact)
    button_3 = customtkinter.CTkButton(master=root, text='Determinante de una matriz', height=125, width=250,
                                       font=("Arial", 15),
                                       fg_color="#3E4446", command=determinante)
    button_4 = customtkinter.CTkButton(master=root, text='Rango de una matriz', height=125, width=250,
                                       font=("Arial", 15),
                                       fg_color="#3E4446", command=rango)
    button_5 = customtkinter.CTkButton(master=root, text='Cifrado por matrices', height=125, width=250,
                                       font=("Arial", 15),
                                       fg_color="#3E4446", command=cifrado)
    button_6 = customtkinter.CTkButton(master=root, text='Cadenas de markov', height=125, width=250,
                                       font=("Arial", 15),
                                       fg_color="#3E4446", command=cadenas_markov)
    button_7 = customtkinter.CTkButton(master=root, text='Operaciones con vectores', height=125, width=250,
                                       font=("Arial", 15),
                                       fg_color="#3E4446", command=operaciones_vectores)

    button_1.pack()
    button_1.place(x=300, y=250)
    button_2.pack()
    button_2.place(x=300, y=500)
    button_3.pack()
    button_3.place(x=715, y=250)
    button_4.pack()
    button_4.place(x=715, y=500)
    button_5.pack()
    button_5.place(x=1100, y=250)
    button_6.pack()
    button_6.place(x=1100, y=500)
    button_7.pack()
    button_7.place(x=715, y=750)


    root.geometry('700x650')
    root.mainloop()


main_interact()



