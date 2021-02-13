import streamlit as st
import numpy as np
import time
import datetime
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

st.beta_set_page_config(page_title='Dados financeiros - IBOV', layout = 'wide', initial_sidebar_state = 'auto')

st.title('Cotações IBOV')

option = st.sidebar.selectbox(
    'Selecione a empresa que deseja avaliar:',
     ['BBDC4','ITSA4','PETR4','MGLU3','TAEE11','VALE3','WEGE3'])

search= option + '.SA'

ticker_info = petr = yf.Ticker(search)
dividend_yield = ticker_info.info['dividendYield']
fiftyDayAverage = ticker_info.info['fiftyDayAverage']
website = ticker_info.info['website']
image = ticker_info.info['logo_url']
longName = ticker_info.info['longName']
fiftyTwoWeekHigh = ticker_info.info['fiftyTwoWeekHigh']
payout = ticker_info.info['payoutRatio']
previousClose = ticker_info.info['previousClose']

'Exibindo informações da empresa: **', longName, '**'

col1,col2, col3 = st.beta_columns(3)

with col1:
    st.image(image, width=None)
with col2:
    st.write('Último fechamento: ** R$',"{:.2f}".format(previousClose),'**')
    st.write('Dividend yield: **', "{:.2%}".format(dividend_yield),'**')
with col3:
    st.write('Preço médio últimos 50 dias: **', "R$ {:.2f}".format(fiftyDayAverage),'**')
    st.write('Máximo 52 semanas: **', "R$ {:.2f}".format(fiftyTwoWeekHigh),'**')


dados = yf.download(search, start='2016-01-02', end=datetime.datetime.today(),progress=False)
dados['rolling_mean'] = dados['Adj Close'].rolling(window=20).mean()
st.title('Valor de fechamento ajustado')
st.line_chart(dados['Adj Close'])
#st.line_chart(dados['rolling_mean'])
st.title('Volume diário')
st.bar_chart(dados['Volume'])

expander = st.sidebar.beta_expander("Informações")
expander.write("Dados: Yahoo Finance")
expander.write("Contato: Herivelton Andreassa")
expander.write("**handreassa@gmail.com**")
    