# Programador: Vítor
# Programa: Janela About
# Objetivo: Mostrar as informações sobre o EasyLink
# Destino: EasyLink
# Versão: Alpha
# Começo: 03/02/2022
# Fim: 06/02/2022

# ativar os comandos do Tkinter
from tkinter import *
import os
#from modulos.dashboard import f_dashboard

def f_fechar_janela():
    v_tela.withdraw()
    #f_dashboard()
    pass

def f_about(p_largura= 800, p_altura= 600, p_imagem= "/logo_easylink.png"):
    global v_tela
    v_tela = Tk()
    #  CONSTANT
    CAMINHO_ARQUIVO=os.path.dirname(__file__)

    # Propriedades do Splash Screen
    v_largura = p_largura
    v_altura = p_altura
    v_tela.wm_resizable(width=False, height=False) 
    v_tela['bg'] = '#0e2634'
    v_tela.geometry('{}x{}'.format(v_largura, v_altura))
    v_tela.title("About easyLink")
        # resolução do nosso sistema (do meu pc )
    v_largura_screen = v_tela.winfo_screenwidth()
    v_altura_screen = v_tela.winfo_screenheight() 

    # posição da jav_janela (calculo para centralizar a jav_janela )
    v_posx = v_largura_screen/2 - v_largura/2 
    v_posy = v_altura_screen/2 - v_altura/2

    # definir geometry (utilizando o calculo para centralizar a jav_janela )
    v_tela.geometry("%dx%d+%d+%d"%(v_largura,v_altura,v_posx,v_posy))
    
    # comandos para a importação e configuração da logo
    v_img_logo=PhotoImage(file=CAMINHO_ARQUIVO+"/logo_easylink.png")
    v_img_interrogacao=PhotoImage(file= CAMINHO_ARQUIVO+"/interrogacao.png")
    v_config_imagem = Label(v_tela, image=v_img_logo,borderwidth=0).pack()

    # comandos para a implementação do subtitulo "SOBRE"
    vs_subtitulo_sobre = Label(v_tela, text="SOBRE", bg='#0e2634', fg="white",font="Gabriela 24 bold")
    vs_subtitulo_sobre.config(anchor=CENTER)
    vs_subtitulo_sobre.pack(pady=10)
    
    # comandos para a implementação da descrição "SOBRE"
    vs_desc_sobre = Label(
    v_tela,
    wraplength=v_largura, 
    text="O Software 'EasyLink' é um pequeno programa que envolve conteúdos sobre programação, ainda está em fase de desenvolvimento e teste.\nO intuito do projeto é dar ao usuário o poder de tirar duvidas e adquirir conhecimento de forma mais rápida e objetiva, através de links de páginas confiáveis.\nNos links são  compartilhados ao usuário de forma rápida e clara a explicação do conteúdo desejado, sem risco de vírus em sua máquina, graças a filtragem feita pelo programa.\nNa plataforma contém assuntos sobre uma das principais linguagem de programação, o Python.\nO programa é  destinado para quem quer aprender à programar ou ter alguma noção da linguagem que contém do programa.", 
    bg='#0e2634', 
    fg="white",
    font="Gabriela 12 ")
    vs_desc_sobre.config(anchor=CENTER)
    vs_desc_sobre.pack()

    # Ir para o dashboard
    a_about= Button(v_tela,image=v_img_interrogacao,command=f_fechar_janela,borderwidth=0)
    a_about.pack(pady=30)
    a_about.place(relx= 0.93, rely= 0.03)
    #comando para manter a janela exibida
    v_tela.mainloop()
    return
if __name__ == '__main__':
    v_tela = Tk()
    f_about()