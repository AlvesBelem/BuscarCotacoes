""" coding:utf-8 """
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

# ================ Variaveis ===============================
lista_moedas = ['USD', 'EUR']

# ================ Funcões ===============================


def pegar_cotacao():
    """A dummy docstring."""


root = tk.Tk()

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
    text='Selecionar moeda que deseja consultar')
label_selecionarmoeda.grid(row=1, column=0, padx=10,
                           pady=10, sticky='nswe', columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10,
                              pady=10, sticky='nswe')

label_selecionarmoeda = tk.Label(
    text='Selecione o dia que deseja pegar a cotação')
label_selecionarmoeda.grid(row=2, column=0, padx=10,
                           pady=10, sticky='nswe', columnspan=2)

calendario_moeda = DateEntry(year=2022, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10,
                      pady=10, sticky='nswe')

label_textocotacao = tk.Label(text='',
                              bg='#5F6062',
                              fg='#C9DCB3',
                              font='Roboto 15 bold',
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

root.mainloop()
