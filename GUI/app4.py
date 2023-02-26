import streamlit as st
from random import choice

st.title(" Random Name generator")

fnames = ['Alex', 'Bob', 'Charlie']

lnames = ['Xu', 'King', 'Robert']

btn = st.button("Generate name")
if btn:
    fn = choice(fnames)
    ln = choice(lnames)
    fullname = f"{fn} {ln}"
    st.success(fullname)

#streamlit run gui/app4.py   to run the streamlit code 