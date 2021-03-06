""" coding:utf-8 """
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
import requests
import pandas as pd
from datetime import datetime
import numpy as np

# ================ Variaveis ===============================
LINK_1 = 'https://economia.awesomeapi.com.br/json/all'
requisicao = requests.get(LINK_1)
dicionario_moedas = requisicao.json()
lista_moedas = list(dicionario_moedas.keys())


# ================ Funcões ===============================


def pegar_cotacao():
    """A dummy docstring."""
    moeda = combobox_selecionarmoeda.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link_2 = f'https://economia.awesomeapi.com.br/{moeda}-BRL/10?'\
             f'start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    requisicao_moeda = requests.get(link_2)
    cotacao = requisicao_moeda.json()
    valor_moeda = cotacao[0]['bid']
    label_textocotacao['text'] = f'A cotação da {moeda}' \
                                 f' no dia {data_cotacao} foi de: R$ {valor_moeda}'


def selecionar_arquivo():
    """A dummy docstring."""
    caminho_arquivo = askopenfilename(title='Seleione o arquivo de moeda')
    var_caminhoarquivo.set(caminho_arquivo)
    if caminho_arquivo:
        label_arquivoselecionado['text'] = f'Arquivo Selecionado: {caminho_arquivo}'


def atualizar_cotacoes():
    """A dummy docstring."""
    try:
        df = pd.read_excel(var_caminhoarquivo.get())
        moedas = df.iloc[:, 0]
        data_inicial = calendario_datainicial.get()
        data_final = calendario_datafinal.get()

        ano_inicial = data_inicial[-4:]
        mes_inicial = data_inicial[3:5]
        dia_inicial = data_inicial[:2]

        ano_final = data_final[-4:]
        mes_final = data_final[3:5]
        dia_final = data_final[:2]

        for moeda in moedas:
            link_3 = f'https://economia.awesomeapi.com.br/{moeda}-BRL/10?'\
                f'start_date={ano_inicial}{mes_inicial}{dia_inicial}'\
                f'&end_date={ano_final}{mes_final}{dia_final}'
            requisicao_moeda = requests.get(link_3)
            cotacoes = requisicao_moeda.json()
            for cotacao in cotacoes:
                bid = float(cotacao['bid'])
                timestamp = int(cotacao['timestamp'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d/%m/%Y')
                if data not in df:
                    df[data] = np.nan

                df.loc[df.iloc[:, 0] == moeda, data] = bid
        df.to_excel('moedas.xlsx')
        label_atualizarcotacoes['text'] = 'Arquivo Atualizado com Sucesso'
    except:
        label_atualizarcotacoes['text'] = 'Selecione um Arquivo Excel em um formato correto'


root = tk.Tk()
# =============== centralizando root ======================
# dimensão da root
LARGURA = 530
ALTURA = 490

# achar dimensão da nossa tela
LARGURA_SCREEN = root.winfo_screenwidth()
ALTURA_SCREEN = root.winfo_screenheight()
print(LARGURA_SCREEN, ALTURA_SCREEN)

# posicao root
POSX = LARGURA_SCREEN/2 - LARGURA/2
POSY = ALTURA_SCREEN/2 - ALTURA/2

# definir geometria
root.geometry('%dx%d+%d+%d' % (LARGURA, ALTURA, POSX, POSY))

# =============== LAYOUT =============================================
# =============== selecionar 1 moeda ==================================
root.title('Ferramenta de Cotação de Moedas')
root.iconbitmap("images/moeda.ico")

label_cotacaomoedas = tk.Label(text='Cotação de 1 moeda especifica',
                               borderwidth=2,
                               relief='solid')
label_cotacaomoedas.grid(row=0, column=0, padx=10,
                         pady=10, sticky='nswe', columnspan=3)

label_selecionarmoeda = tk.Label(
    text='Selecionar moeda que deseja consultar', anchor='e')
label_selecionarmoeda.grid(row=1, column=0, padx=10,
                           pady=10, sticky='nswe', columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10,
                              pady=10, sticky='nswe')

label_selecionardia = tk.Label(
    text='Selecione o dia que deseja pegar a cotação', anchor='e')
label_selecionardia.grid(row=2, column=0, padx=10,
                         pady=10, sticky='nswe', columnspan=2)

calendario_moeda = DateEntry(year=2022, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10,
                      pady=10, sticky='nswe')

label_textocotacao = tk.Label(text='',
                              bg='#5F6062',
                              fg='#C9DCB3',
                              font='Roboto 9 bold',
                              width=30)
label_textocotacao.grid(row=3, column=0, padx=10,
                        pady=10, sticky='nswe', columnspan=2)

btn_pegarcotacao = tk.Button(text='Pegar cotação', command=pegar_cotacao,
                             bg='#5F6062',
                             fg='#fff',
                             font='Roboto 10 bold')
btn_pegarcotacao.grid(row=3, column=2, padx=10,
                      pady=10, sticky='nswe')

# =============== selecionar varias moedas ==================================

label_variasmoedas = tk.Label(
    text='Cotação de multiplas moedas', borderwidth=2, relief='solid')
label_variasmoedas.grid(row=4, column=0, padx=10,
                        pady=10, sticky='nswe', columnspan=3)

label_selecionararquivo = tk.Label(
    text='Selecione um arquivo em Excel com as moedas na colana A')
label_selecionararquivo.grid(row=5, column=0, padx=10,
                             pady=10, sticky='nswe', columnspan=2)

var_caminhoarquivo = tk.StringVar()

btn_selecionararquivo = tk.Button(text='Clique para selecionar', command=selecionar_arquivo,
                                  bg='#5F6062',
                                  fg='#fff',
                                  font='Roboto 10 bold')
btn_selecionararquivo .grid(row=5, column=2, padx=10,
                            pady=10, sticky='nswe')

label_arquivoselecionado = tk.Label(
    text='Nenhum arquivo selecionado', anchor='e')
label_arquivoselecionado.grid(row=6, column=0, padx=10,
                              pady=10, sticky='nswe', columnspan=3)

label_datainicial = tk.Label(text='Data Inicial', anchor='e')
label_datainicial.grid(row=7, column=0, padx=10,
                       pady=10, sticky='nswe')

label_datafinal = tk.Label(text='Data Final', anchor='e')
label_datafinal.grid(row=8, column=0, padx=10,
                     pady=10, sticky='nswe')

calendario_datainicial = DateEntry(year=2022, locale='pt_br')
calendario_datainicial.grid(row=7, column=1, padx=10,
                            pady=10, sticky='nswe')

calendario_datafinal = DateEntry(year=2022, locale='pt_br')
calendario_datafinal.grid(row=8, column=1, padx=10,
                          pady=10, sticky='nswe')


btn_atualizarcotacoes = tk.Button(text='Atualizar cotações', command=atualizar_cotacoes,
                                  bg='#5F6062',
                                  fg='#fff',
                                  font='Roboto 10 bold')
btn_atualizarcotacoes.grid(row=9, column=0, padx=10,
                           pady=10, sticky='nswe')

label_atualizarcotacoes = tk.Label(text='',
                                   bg='#5F6062',
                                   fg='#C9DCB3',
                                   font='Roboto 9 bold',
                                   width=30)
label_atualizarcotacoes.grid(row=9, column=1, padx=10,
                             pady=10, sticky='nswe', columnspan=2)

btn_fechar = tk.Button(text='Fechar', command=root.quit,
                       bg='#5F6062',
                       fg='#fff',
                       font='Roboto 10 bold')
btn_fechar.grid(row=10, column=2, padx=10,
                pady=10, sticky='nswe')

root.mainloop()
