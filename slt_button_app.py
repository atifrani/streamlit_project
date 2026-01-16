import streamlit as st

st.header('streamlit button eaxample')

if st.button('say hello'):
     st.write('why hello?')
else:
     st.write('goodbye')
