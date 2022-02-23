# Programador: Oliver Faustino
# Programa: Dashboard
# Versão: Alpha
# Data/criação: 07/02/2022

from tkinter import *
from tkinter import ttk
import os
import pyperclip
from functools import partial
import webbrowser


l_temas = ("Sobre o Python","Sintaxe","Variáveis","print()","input()","Comentarios em Python","Números em Python","Tipos de Dados", "Tipos de Dados: string", "Tipos de Dados: integer", "Tipos de Dados: boleanos", "Tipos de Dados: float","Conversão de Dados","Operadores de Comparação","Tuplas","Listas","Dicionários","Conjuntos","Loop","Funções","if e else","while")

dic_links = {
            "Sobre o Python":"https://olhardigital.com.br/2021/10/04/tira-duvidas/o-que-e-para-que-serve-o-python/",
            "print()":"http://www.bosontreinamentos.com.br/programacao-em-python/guia-basico-da-funcao-print-em-python/",
            "Sintaxe":"https://pt.m.wikipedia.org/wiki/Sintaxe_e_sem%C3%A2ntica_de_Python",
            "Comentarios em Python":"http://excript.com/python/comentarios-em-python.html",
            "Tipos de Dados":"http://excript.com/python/tipos-de-dados-python.html",
            "Números em Python":"https://algoritmosempython.com.br/cursos/programacao-python/tipos-basicos/",
            "Conversão de Dados":"https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3-pt",
            "Tipos de Dados: boleanos":"https://panda.ime.usp.br/pensepy/static/pensepy/06-Selecao/selecao.html",
            "Listas":"https://algoritmosempython.com.br/cursos/programacao-python/listas/",
            "Tuplas":"https://blog.betrybe.com/tecnologia/tuplas-em-python/",
            "Conjuntos":"https://pythonhelp.wordpress.com/2013/06/18/conjuntos-em-python/",
            "Dicionários":"https://kenzie.com.br/blog/dicionario-python/",
            "Loop":"https://blog.grancursosonline.com.br/python-loop/",
            "Funções":"https://panda.ime.usp.br/pensepy/static/pensepy/05-Funcoes/funcoes.html",
            "Variáveis":"https://blog.ffelix.eti.br/como-criar-variaveis-em-python/",
            "input()":"http://www.bosontreinamentos.com.br/programacao-em-python/entrada-de-dados-em-python-com-funcao-input/",
            "Tipos de Dados: string":"https://www.devmedia.com.br/tipos-de-dados-em-python-string/40669",
            "Tipos de Dados: float":"https://docs.python.org/pt-br/3/tutorial/floatingpoint.html",
            "Tipos de Dados: integer":"https://panda.ime.usp.br/pensepy/static/pensepy/02-Conceitos/conceitos.html",
            "while":"https://www.devmedia.com.br/python-estrutura-de-repeticao-while/38546",
            "if e else":"https://pt.m.wikipedia.org/wiki/Estrutura_de_sele%C3%A7%C3%A3o",  
            "Operadores de Comparação": "https://www.pythonprogressivo.net/2018/02/Operadores-Comparacao-Python.html?m=1"}





def f_fechar_janela():
    v_tela.destroy()
    f_about()


    # função para abrir o link no navegador
def f_abrir_link(p_link):
    webbrowser.open(p_link)

    # função para copiar o link para área de transferência
def f_copiar_link(p_link):
    pyperclip.copy(p_link)

    # Função que criará as configurações do que aparecerá no combobox.
def f_cb_links(p_nome_bt, p_tema, p_relx, p_rely, p_relwidth, p_relheight):
    
    CAMINHO_ARQUIVO=os.path.dirname(__file__)
    v_img_navegar = CAMINHO_ARQUIVO+'/navegar.png'
    v_img_navegar = PhotoImage(file= v_img_navegar)

    # parâmetros em variáveis
    p_nome_bt = p_nome_bt
    p_tema = p_tema 
    p_relx = p_relx
    p_rely = p_rely
    p_relwidth = p_relwidth
    p_relheight = p_relheight
        
    # Chamar o tema dentro do dicionário e mostrar-lo na tela
    link = dic_links[p_tema]
    lb_link = Label(v_tela, text= link, font=('BatangChe 8 bold'), fg= '#ffffff', bg='#35879c')
    lb_link.place(relx= 0.10, rely=0.70, relwidth= 0.8, relheight= 0.05)

    # Botão para copiar o Link
    bt_copiar_link = Button(v_tela, text= "Copiar", command= partial(f_copiar_link, link), font=('BatangChe 10 bold'), fg= '#ffffff', bg='#0e2634')
    bt_copiar_link.place(relx= 0.15, rely= 0.80, relwidth= 0.3, relheight=0.07)

    # Botão para abrir o link no navegador
    bt_copiar_link = Button(v_tela, text= 'Navegar', command= partial(f_abrir_link, link), font=('BatangChe 10 bold'), fg= '#ffffff', bg='#0e2634')
    bt_copiar_link.place(relx= 0.55, rely= 0.80, relwidth= 0.3, relheight=0.07)

    return


def f_dashboard(p_largura= 800, p_altura= 600):

    global v_tela 
    v_tela = Tk()
    
    #  CONSTANT
    CAMINHO_ARQUIVO=os.path.dirname(__file__)
    v_img_interrogacao = CAMINHO_ARQUIVO+"/interrogacao.png"
    v_img_background= CAMINHO_ARQUIVO+ "/background_dashboard.png"
    v_img_dica_random= CAMINHO_ARQUIVO+ "/Random.png"
    v_img_dica_turtle= CAMINHO_ARQUIVO+ "/Turtle.png"
    v_img_dica_curso_python= CAMINHO_ARQUIVO+ "/Curso Python.png"
    # Imagens
    v_img_interrogacao=PhotoImage(file= v_img_interrogacao)
    v_img_background=PhotoImage(file= v_img_background)
    v_img_dica_random=PhotoImage(file= v_img_dica_random)
    v_img_dica_turtle=PhotoImage(file= v_img_dica_turtle)
    v_img_dica_curso_python=PhotoImage(file= v_img_dica_curso_python)
    # Propriedades do Dashboard
    v_largura = p_largura
    v_altura = p_altura
    v_tela.wm_resizable(width=False, height=False) 
    #v_tela['bg'] = '#0e2634'
    v_tela.geometry('{}x{}'.format(v_largura, v_altura))
    v_tela.title("easyLink")
    
    # Colocar as imgs
    Label(v_tela,image=v_img_background, borderwidth=0).pack()
    # Calculos para centralizar a tela
    v_largura_screen = v_tela.winfo_screenwidth()
    v_altura_screen = v_tela.winfo_screenheight() 
    v_posx = v_largura_screen/2 - v_largura/2 
    v_posy = v_altura_screen/2 - v_altura/2
    v_tela.geometry("%dx%d+%d+%d"%(v_largura,v_altura,v_posx,v_posy))


    def f_cb_resposta(event): 
        cb_dashboard_resposta = cb_dashboard.get()
        f_cb_links(cb_dashboard_resposta, cb_dashboard_resposta, 0.09, 0.30, 0.4, 0.05)
        return

    # Cria combo box
    cb_dashboard = ttk.Combobox(v_tela, values=l_temas)
    cb_dashboard.set('Sobre o Python')
    cb_dashboard.place(relx=0.35, rely=0.49, relwidth= 0.3, relheight=0.05)
    cb_dashboard.bind('<<ComboboxSelected>>' ,f_cb_resposta)

    # Ir para a janela about
    bt_about= Button(v_tela,image=v_img_interrogacao,command= f_fechar_janela,borderwidth=0, bg='#0e2634')
    bt_about.pack(pady=30)
    bt_about.place(relx= 0.93, rely= 0.03)
    

    # Botões das dicas
    img_dicas_1 = Label(v_tela, image = v_img_dica_random,bg='#0e2634', cursor="hand2")
    img_dicas_1.pack()
    img_dicas_1.place(relx= 0.12, rely=0.23, relwidth= 0.22, relheight= 0.22)
    img_dicas_1.bind("<Button-1>", lambda e:
    f_abrir_link("https://code.tutsplus.com/pt/tutorials/mathematical-modules-in-python-random--cms-27738"))
    img_dicas_2 = Label(v_tela, image = v_img_dica_turtle,bg='#0e2634', cursor="hand2")
    img_dicas_2.pack()
    img_dicas_2.place(relx= 0.39, rely=0.23, relwidth= 0.22, relheight= 0.22)
    img_dicas_2.bind("<Button-1>", lambda e:
    f_abrir_link("https://acervolima.com/python-turtle-comandos-de-teclado-grafico/"))
    img_dicas_3 = Label(v_tela, image = v_img_dica_curso_python,bg='#0e2634', cursor="hand2")
    img_dicas_3.pack()
    img_dicas_3.place(relx= 0.66, rely=0.23, relwidth= 0.22, relheight= 0.22)
    img_dicas_3.bind("<Button-1>", lambda e:
    f_abrir_link("https://www.youtube.com/playlist?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR"))

    
    v_tela.mainloop()
    return




# JANELA ABOUT





def f_about(p_largura= 800, p_altura= 600, p_imagem= "\\logo_easylink.png"):

    v_tela_about = Tk()
    #  CONSTANT
    CAMINHO_ARQUIVO=os.path.dirname(__file__)

    # Propriedades do Splash Screen
    v_largura = p_largura
    v_altura = p_altura
    v_tela_about.wm_resizable(width=False, height=False) 
    v_tela_about['bg'] = '#0e2634'
    v_tela_about.geometry('{}x{}'.format(v_largura, v_altura))
    v_tela_about.title("About easyLink")
    # resolução do nosso sistema (do meu pc )
    v_largura_screen = v_tela_about.winfo_screenwidth()
    v_altura_screen = v_tela_about.winfo_screenheight() 

    # posição da jav_janela (calculo para centralizar a jav_janela )
    v_posx = v_largura_screen/2 - v_largura/2 
    v_posy = v_altura_screen/2 - v_altura/2

    # definir geometry (utilizando o calculo para centralizar a jav_janela )
    v_tela_about.geometry("%dx%d+%d+%d"%(v_largura,v_altura,v_posx,v_posy))
    
    # comandos para a importação e configuração da logo
    v_img_logo=PhotoImage(file=CAMINHO_ARQUIVO+"/logo_easylink.png")
    v_img_background= PhotoImage(file= CAMINHO_ARQUIVO+ "/background_about.png")
    v_img_interrogacao=PhotoImage(file= CAMINHO_ARQUIVO+"/interrogacao.png")
    v_config_imagem = Label(v_tela_about, image=v_img_background).pack()

    # comandos para a implementação do subtitulo "SOBRE"
    vs_subtitulo_sobre = Label(v_tela_about, text="SOBRE", bg='#0e2634', fg="white",font="Gabriela 24 bold")
    vs_subtitulo_sobre.config(anchor=CENTER)
    vs_subtitulo_sobre.pack(pady=10)
    
    # comandos para a implementação da descrição "SOBRE"
    vs_desc_sobre = Label(
    v_tela_about,
    wraplength=v_largura, 
    text='''O Software "EasyLink" é um programa que envolve conteúdos sobre programação, que ainda está em fase de desenvolvimento e teste.
O intuito do projeto é dar ao usuário o poder de tirar dúvidas e adquirir conhecimento de forma mais rápida e objetiva, através de links de páginas confiáveis. Nos links são compartilhados ao usuário de forma rápida e clara a explicação do conteúdo desejado, sem risco de vírus em sua máquina, graças à filtragem feita pelo programa.
Na plataforma contém assuntos sobre uma das principais linguagens de programação, o Python.
O programa é destinado para quem quer aprender à programar ou ter alguma noção da linguagem que contém no programa.''', 
    bg='#0e2634', 
    fg="white",
    font="Gabriela 12 ")
    vs_desc_sobre.config(anchor=CENTER)
    vs_desc_sobre.pack()

    def f_fechar_janela():
        v_tela_about.destroy()
        f_dashboard()

    # Ir para o dashboard
    a_about= Button(v_tela_about,image=v_img_interrogacao,command=f_fechar_janela,borderwidth=0, bg='#0e2634')
    a_about.pack(pady=30)
    a_about.place(relx= 0.93, rely= 0.03)
    #comando para manter a janela exibida
    v_tela_about.mainloop()

    
    return


if __name__ == '__main__':
    v_tela = Tk()
    #f_random_l_temas()
    f_dashboard()

