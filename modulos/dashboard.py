from cgitb import text
from tkinter import *
#from modulos.janela_about import *
import os
import pyperclip

 

def f_fechar_janela():
    v_tela.destroy()
    #f_about()

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
    
    # Propriedades do Dashboard
    v_largura = p_largura
    v_altura = p_altura
    v_tela.wm_resizable(width=False, height=False) 
    v_tela['bg'] = '#0e2634'
    v_tela.geometry('{}x{}'.format(v_largura, v_altura))
    v_tela.title("easyLink")
    # Calculos para centralizar a tela
    v_largura_screen = v_tela.winfo_screenwidth()
    v_altura_screen = v_tela.winfo_screenheight() 
    v_posx = v_largura_screen/2 - v_largura/2 
    v_posy = v_altura_screen/2 - v_altura/2
    v_tela.geometry("%dx%d+%d+%d"%(v_largura,v_altura,v_posx,v_posy))
    # Logo centralizada na tela
    Label(v_tela, image=v_img_logo,borderwidth=0).pack()

    def f_print():
        v_link_print = "http://www.bosontreinamentos.com.br/programacao-em-python/guia-basico-da-funcao-print-em-python/" 
        pyperclip.copy(v_link_print) 
        vs_print["text"] = "Link Copiado na Área de Transferência"
        return vs_print
    
    def f_tipos_dados():
        v_link_tipo_dados = "http://excript.com/python/tipos-de-dados-python.html"
        pyperclip.copy(v_link_tipo_dados)
        vs_tipos_dados["text"] = "Link Copiado na Área de Transferência"
        return vs_tipos_dados

    def f_variavel():
        v_link_variavel = "https://blog.ffelix.eti.br/como-criar-variaveis-em-python/"
        pyperclip.copy(v_link_variavel)
        vs_variavel["text"] = "Link Copiado na Área de Transferência"
        return vs_variavel

    def f_input():
        v_link_input = "http://www.bosontreinamentos.com.br/programacao-em-python/entrada-de-dados-em-python-com-funcao-input/"
        pyperclip.copy(v_link_input)
        vs_input["text"] = "Link Copiado na Área de Transferência"
        return vs_input

    # Botão PRINT
    bt_print = Button(v_tela, text= "Função print()", command= f_print)
    bt_print.place(relx= 0.09, rely= 0.30, relwidth= 0.4)
    vs_print = Label(v_tela, text= "")
    vs_print.place(relx= 0.18, rely=0.35)

    # Botão VARIÀVEL
    bt_variavel = Button(v_tela, text= "Variáveis", command= f_variavel)
    bt_variavel.place(relx= 0.09, rely= 0.40, relwidth= 0.4)
    vs_variavel = Label(v_tela, text= "")
    vs_variavel.place(relx= 0.18, rely=0.45)

    # Botão INPUT
    bt_input = Button(v_tela, text= "Variáveis", command= f_input)
    bt_input.place(relx= 0.52, rely= 0.40, relwidth= 0.4)
    vs_input = Label(v_tela, text= "")
    vs_input.place(relx= 0.6, rely=0.45)   

    # Botão TIPO DADOS
    bt_tipos_dados = Button(v_tela, text= "Tipos de Dados do Python", command= f_tipos_dados)
    bt_tipos_dados.place(relx= 0.52, rely=0.30, relwidth= 0.4)
    vs_tipos_dados = Label(v_tela, text= "")
    vs_tipos_dados.place(relx= 0.6, rely=0.35)

    # Ir para a janela about
    bt_about= Button(v_tela,image=v_img_interrogacao,command= f_fechar_janela,borderwidth=0)
    bt_about.pack(pady=30)
    bt_about.place(relx= 0.93, rely= 0.03)
    v_tela.mainloop()


    

    return
if __name__ == '__main__':
    v_tela = Tk()
    #f_about()
    f_dashboard()
