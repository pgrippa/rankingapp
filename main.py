from pandas.core.algorithms import rank
import streamlit as st
import pandas as pd
import openpyxl as xl

header = st.container()
#workbook = xl.load_workbook('data/ranking.xlsx')


with header:
    st.title('Welcome to the CEFD ')
    cols = st.columns(2)
    cols[0].write('**Name**')
    cols[0].write('Gabriel')
    cols[0].write('Nicolas')
    cols[0].write('Philipe')
    cols[1].write('**Score**')
    cols[1].write('2')
    cols[1].write('0')
    cols[1].write('0')

    #ranking = pd.read_csv('data/ranking.csv', header=None)
    
    #ranking.columns = ['Name', 'Score']
    #st.write(ranking.head())
    #table = st.table(ranking);

