# Programador: Samuca 
# Programa: janela 
# Objetivo: Amostrar a janela das dicas e o link
# Destino: easyLink
# Versão:  alpha
# Começo: 03/02/2022
# Fim: 05/02/2022

#Invocando o modulo tk (pra janela grafica )
import tkinter as tk
import os

   #criando a função que enviara o link 
def f_meu_comando():
   v_texto.config(text="https://olhardigital.com.br/2021/10/04/tira-duvidas/o-que-e-para-que-serve-o-python/")

def f_img_link():

   #importando a v_imagem que será usada na jav_tela
   v_pasta_tela=os.path.dirname(__file__)
   v_imagem= tk.PhotoImage(file=v_pasta_tela+"\\Dica1.png")
   v_w = tk.Label(v_tela,image=v_imagem)

   #criando o botao (no caso ai a propria v_imagemsera o botao)
   v_botao= tk.Button(v_tela,image=v_imagem,command=f_meu_comando, orderwidth=0)
   v_botao.pack(pady=30)

   #Criando um texto que ficara embaixo da v_imagem
   v_texto= tk.Label(v_tela,text= "Clique naimagem")
   v_texto.pack(pady=30)
   return