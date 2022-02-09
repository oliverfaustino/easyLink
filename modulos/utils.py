from tkinter import *

'''
Função: p_tela

Parâmetros:
    1: título da janela
    2: largura da janela
    3: altura da janela

Exemplo de uso:

f_tela('easyLink', 800, 600)
'''

'''def f_tela(p_titulo= "Sem Nome", p_largura= 800, p_altura= 600, p_tela = Tk()):

    p_tela.title(p_titulo)
    v_largura = p_largura
    v_altura = p_altura
    p_tela.wm_resizable(width=False, height=False)

    # resolução do nosso sistema (do meu pc )
    v_largura_screen = p_tela.winfo_screenwidth()
    v_altura_screen = p_tela.winfo_screenheight()
    
    # posição da jav_janela (calculo para centralizar a jav_janela )
    v_posx = v_largura_screen/2 - v_largura/2 
    v_posy = v_altura_screen/2 - v_altura/2
    
    # definir geometry (utilizando o calculo para centralizar a jav_janela )
    p_tela.geometry("%dx%d+%d+%d"%(v_largura,v_altura,v_posx,v_posy))
    mainloop()
    return p_tela'''

def f_fechar_janela():
    v_tela.destroy()
    return