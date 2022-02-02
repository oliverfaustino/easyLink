# Programador: Wender Brito
# Programa: Splash Screen
# Destino: easyLink
# Versão: Alpha
# Data/criação: 03/02/2022
# Data/término: ...


from tkinter import *
import os 

#Localizar o programa e consequentemente a imagem
vs_pasta_tela=os.path.dirname(__file__)

#Criar a tela
vs_tela= Tk()
vs_tela.title("Splash Screen")
vs_tela.geometry("577x561")  
vs_tela.wm_resizable(width=False, height=False) 

#Importa imagem
vs_img_splash=PhotoImage(file=vs_pasta_tela+"\\imagem.png")

#Label
vs_label_img=Label(vs_tela,image=vs_img_splash)
vs_label_img.place(x=0,y=0)

mainloop()




