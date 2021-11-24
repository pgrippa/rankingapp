from pandas.core.algorithms import rank
import streamlit as st

header = st.container()
with header:
    st.title('Welcome to the CEFD Fucking Ranking')
    cols = st.columns(2)
    cols[0].write('**Name**')
    cols[0].write('Gabriel')
    cols[0].write('Nicolas')
    cols[0].write('Philipe')
    cols[1].write('**Score**')
    cols[1].write('2') 
    cols[1].write('0')
    cols[1].write('0')

