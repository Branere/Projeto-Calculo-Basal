import tkinter as tk
from tkinter import messagebox

def calcular_consumo_basal(genero, idade, altura, peso):
    if genero == "Masculino":
        resultado = 66 + (13.75 * peso) + (5 * altura) - (6.75 * idade)
    else:
        resultado = 665 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
    
    resultado_arredondado = round(resultado, 4)
    return resultado_arredondado

def calcular_e_mostrar():
    genero = genero_var.get()
    nome = nome_entry.get()
    idade = float(idade_entry.get())
    altura = float(altura_entry.get())
    peso_input = peso_entry.get()
    
    try:
        peso = float(peso_input.replace(',', '.'))
    except ValueError:
        messagebox.showerror("Erro", "Valor de peso inválido.")
        return
    
    resultado = calcular_consumo_basal(genero, idade, altura, peso)
    genero_str = "Masculino" if genero == "Masculino" else "Feminino"
    resultado_label.config(text=f"Muito bem, {nome}. Seu consumo basal diário como {genero_str} é de:\n{resultado} Calorias por dia")

# Configuração da janela
window = tk.Tk()
window.title("Cálculo Basal")

# Widgets
nome_label = tk.Label(window, text="Nome:")
nome_label.pack()
nome_entry = tk.Entry(window)
nome_entry.pack()

idade_label = tk.Label(window, text="Idade:")
idade_label.pack()
idade_entry = tk.Entry(window)
idade_entry.pack()

altura_label = tk.Label(window, text="Altura (cm):")
altura_label.pack()
altura_entry = tk.Entry(window)
altura_entry.pack()

peso_label = tk.Label(window, text="Peso:")
peso_label.pack()
peso_entry = tk.Entry(window)
peso_entry.pack()

genero_var = tk.StringVar()
genero_var.set("Masculino")
genero_label = tk.Label(window, text="Gênero:")
genero_label.pack()
genero_menu = tk.OptionMenu(window, genero_var, "Masculino", "Feminino")
genero_menu.pack()

calcular_button = tk.Button(window, text="Calcular", command=calcular_e_mostrar)
calcular_button.pack()

resultado_label = tk.Label(window, text="")
resultado_label.pack()

# Inicia a interface
window.mainloop()