
# Programador: Vítor
# Programa: Janela About
# Objetivo: Mostrar as informações sobre o EasyLink
# Destino: EasyLink
# Versão: Alpha
# Começo: 03/02/2022
# Fim: 06/02/2022

# ativar os comandos do Tkinter
from tkinter import *
# ativar os comandos do os para as imagens
import os


def f_criacao_janela_about():

    # comandos para a criação e configuração da janela
    win_width, win_height = 800, 600
    v_janela_about = Tk()
    v_janela_about['bg'] = '#0e2634'
    v_janela_about.geometry('{}x{}'.format(win_width, win_height))
    v_janela_about.title("Janela About")
    # comandos para a importação e configuração da logo
    v_pastaApp=os.path.dirname(__file__)
    v_img_logo=PhotoImage(file=v_pastaApp+"\\lg.png")
    v_config_imagem = Label(v_janela_about, image=v_img_logo,borderwidth=0).pack()
    # comandos para a implementação do subtitulo "SOBRE"
    vs_subtitulo_sobre = Label(v_janela_about, text="SOBRE", bg='#0e2634', fg="white",font="Gabriela 24 bold")
    vs_subtitulo_sobre.config(anchor=CENTER)
    vs_subtitulo_sobre.pack(pady=10)
    # comandos para a implementação da descrição "SOBRE"
    vs_desc_sobre = Label(
    v_janela_about,
    wraplength=win_width, 
    text="O Software 'EasyLink' é um pequeno programa que envolve conteúdos sobre programação, ainda está em fase de desenvolvimento e teste.\nO intuito do projeto é dar ao usuário o poder de tirar duvidas e adquirir conhecimento de forma mais rápida e objetiva, através de links de páginas confiáveis.\nNos links são  compartilhados ao usuário de forma rápida e clara a explicação do conteúdo desejado, sem risco de vírus em sua máquina, graças a filtragem feita pelo programa.\nNa plataforma contém assuntos sobre uma das principais linguagem de programação, o Python.\nO programa é  destinado para quem quer aprender à programar ou ter alguma noção da linguagem que contém do programa.", 
    bg='#0e2634', 
    fg="white",
    font="Gabriela 12 ")
    vs_desc_sobre.config(anchor=CENTER)
    vs_desc_sobre.pack()

    # comando para manter a janela exibida
    v_janela_about.mainloop()

#chamando a funcao que executará os comando da janela
f_criacao_janela_about()