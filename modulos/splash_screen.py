# Programador: Wender Brito
# Programa: Splash Screen
# Destino: easyLink
# Versão: Alpha
# Data/criação: 03/02/2022
# Data/término: ...


from tkinter import *
import os 

def f_splash_screen():
    #Localizar o programa e consequentemente a imagem
    v_pasta_tela=os.path.dirname(__file__)

    # dimensões da janela(vi)
    vi_largura = 700
    vi_altura = 350 

    #Criar a tela
    v_tela= Tk()
    v_tela.title("Splash Screen")
    # vs_tela.geometry("577x561")  
    v_tela.wm_resizable(width=False, height=False) 

    # resolução do nosso sistema (do meu pc )
    vi_largura_screen = v_tela.winfo_screenwidth()
    vi_altura_screen = v_tela.winfo_screenheight() 

    # posição da jav_janela (calculo para centralizar a jav_janela )
    v_posx = vi_largura_screen/2 - vi_largura/2 
    v_posy = vi_altura_screen/2 - vi_altura/2

    # definir geometry (utilizando o calculo para centralizar a jav_janela )
    v_tela.geometry("%dx%d+%d+%d"%(vi_largura,vi_altura,v_posx,v_posy))

    #Importa imagem
    vs_img_splash=PhotoImage(file=v_pasta_tela+"\\img_splash_screen.png")

    #Label
    vs_label_img=Label(v_tela,image=vs_img_splash)
    vs_label_img.place(x=0,y=0)
    mainloop()
    return 

f_splash_screen()

