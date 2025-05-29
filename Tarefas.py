import tkinter as tk
import json

with open('Atividades.json', 'r', encoding='utf-8') as N:
    data = json.load(N)

Atividades = data["atividades"]

def addatividades():
    while True:
        adicionarat = input("Digite o nome da nova atividade : ")
        cont = input(f"A atividade {adicionarat} será adicionada a lista de atividades, Você confirma? 1 - Sim / 0 - Não : ")
        if cont == "1":
            Atividades.append(adicionarat)
            break
        else:
            pass    

addatividades()



janela = tk.Tk()
janela.title("Atividades")
janela.geometry("200x600")

texto = tk.Label(janela, text= "\n".join(Atividades))
texto.pack() 

janela.mainloop()
