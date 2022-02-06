# Programador: Samuca 
# Programa: janela 
# Objetivo: Amostrar a janela das dicas e o link
# Destino: easyLink
# Versão:  alpha
# Começo: 03/02/2022
# Fim: 05/02/2022

#Invocando o modulo tk (pra janela grafica )
import tkinter as tk

#Criando uma janela inicial e dando um nome
v_janela = tk.Tk()
v_janela.title("Titulo")

# dimensões da janela(vi)
vi_largura = 500
vi_altura = 350

# resolução do nosso sistema (do meu pc )
vi_largura_screen = v_janela.winfo_screenwidth()
vi_altura_screen = v_janela.winfo_screenheight() 

# posição da jav_janela (calculo para centralizar a jav_janela )
v_posx = vi_largura_screen/2 - vi_largura/2 
v_posy = vi_altura_screen/2 - vi_altura/2

# definir geometry (utilizando o calculo para centralizar a jav_janela )
v_janela.geometry("%dx%d+%d+%d"%(vi_largura,vi_altura,v_posx,v_posy))

#importando a v_imagem que será usada na jav_janela
v_imagem= tk.PhotoImage(file="Dica1.png")
v_w = tk.Label(v_janela,image=v_imagem)

#criando a função que enviara o link 
def f_meu_comando():
   v_texto.config(text="https://olhardigital.com.br/2021/10/04/tira-duvidas/o-que-e-para-que-serve-o-python/")

#criando o botao (no caso ai a propria v_imagemsera o botao)
v_botao= tk.Button(v_janela,image=v_imagem,command=f_meu_comando,
borderwidth=0)
v_botao.pack(pady=30)

#Criando um texto que ficara embaixo da v_imagem
v_texto= tk.Label(v_janela,text= "Clique naimagem")
v_texto.pack(pady=30)

#Sem isso aqui não tem janela (vai invocar uma tela grafica)
v_janela.mainloop()
