# Programador: Wender Brito
# Programa: Splash Screen
# Versão: Alpha
# Data/criação: 03/02/2022

from tkinter import *
import os
import time

''' 
Função: f_splash_screen

Parâmetros:
    1: largura
    2: altura

Exemplo de uso:
f_splash_screen(300, 500)
''' 
v_tela = Tk()

def f_fechar_janela():
    v_tela.destroy()
    return

def f_splash_screen(p_largura= 700, p_altura= 350, p_imagem= "\\img_splash_screen.png", p_time= 6000):
    
    #  CONSTANT
    CAMINHO_ARQUIVO=os.path.dirname(__file__)

    # Propriedades do Splash Screen
    v_largura = p_largura
    v_altura = p_altura
    v_imagem=CAMINHO_ARQUIVO+p_imagem

    #Criar a tela
    v_tela.after(p_time, f_fechar_janela)
    v_tela.title("Splash Screen")
    v_tela.overrideredirect(True)
    v_tela.wm_resizable(width=False, height=False) 

    # resolução do nosso sistema (do meu pc )
    v_largura_screen = v_tela.winfo_screenwidth()
    v_altura_screen = v_tela.winfo_screenheight() 

    # posição da jav_janela (calculo para centralizar a jav_janela )
    v_posx = v_largura_screen/2 - v_largura/2 
    v_posy = v_altura_screen/2 - v_altura/2

    # definir geometry (utilizando o calculo para centralizar a jav_janela )
    v_tela.geometry("%dx%d+%d+%d"%(v_largura,v_altura,v_posx,v_posy))

    #Importa v_imagem
    v_img_splash=PhotoImage(file= v_imagem)

    #Label
    vs_label_img=Label(v_tela,image=v_img_splash, borderwidth=0)
    vs_label_img.place(x=0,y=0)
    mainloop()
    return
if __name__ == '__main__':
    v_tela = Tk()
    f_splash_screen()