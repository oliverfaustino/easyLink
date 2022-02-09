from tkinter import *
from modulos.janela_about import *
import os


def f_fechar_janela():
    v_tela.destroy()
    f_about()

def f_dashboard(p_largura= 800, p_altura= 600):
    global v_tela 
    v_tela = Tk()
    #  CONSTANT
    CAMINHO_ARQUIVO=os.path.dirname(__file__)
    v_img_logo = CAMINHO_ARQUIVO+"\\logo_easylink.png"

    v_img_interrogacao = CAMINHO_ARQUIVO+"\\interrogacao.png"
    # Imagens

    v_img_logo=PhotoImage(file=v_img_logo)
    v_img_interrogacao=PhotoImage(file= v_img_interrogacao)
    # Propriedades do Splash Screen
    v_largura = p_largura
    v_altura = p_altura
    v_tela.wm_resizable(width=False, height=False) 
    v_tela['bg'] = '#0e2634'
    v_tela.geometry('{}x{}'.format(v_largura, v_altura))
    v_tela.title("easyLink")
    # resolução do nosso sistema (do meu pc )
    v_largura_screen = v_tela.winfo_screenwidth()
    v_altura_screen = v_tela.winfo_screenheight() 

    # posição da jav_janela (calculo para centralizar a jav_janela )
    v_posx = v_largura_screen/2 - v_largura/2 
    v_posy = v_altura_screen/2 - v_altura/2

    # definir geometry (utilizando o calculo para centralizar a jav_janela )
    v_tela.geometry("%dx%d+%d+%d"%(v_largura,v_altura,v_posx,v_posy))

    # Logo centralizada na imagem
    Label(v_tela, image=v_img_logo,borderwidth=0).pack()

    # Ir para a janela about
    a_about= Button(v_tela,image=v_img_interrogacao,command= f_fechar_janela,borderwidth=0)
    a_about.pack(pady=30)
    v_tela.mainloop()
    return
if __name__ == '__main__':
    v_tela = Tk()
    f_dashboard()