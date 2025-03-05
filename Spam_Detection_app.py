# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 20:14:59 2025

@author: Ramfis
"""

import streamlit as st
import pickle
import email
from email import policy
from email.parser import BytesParser

model=pickle.load(open('model.pkl','rb'))
vc=pickle.load(open('count_vect.pkl','rb'))
st.title("Verificar si un mail es spam o un e-mail normal (el texto debe estar en ingles)")

on = st.toggle("Ingresar correo o texto")

if on:
    
    text_mail=[st.text_input('Ingresa el texto de tu mail aqui')]
    
    if text_mail != '':
        vectorized_text=vc.transform(text_mail).toarray()
        result=model.predict(vectorized_text)
        st.write('Este mail se considera un spam' if result == 1 else 'Este mail se considera normal')
    else:
        st.info('Esperando ingresar el texto')
else:
    uploaded_file = st.file_uploader("O puedes subir tu e-mail", type=["eml"])

    if uploaded_file:
        msg=BytesParser(policy=policy.default).parse(uploaded_file)
        text_mail = [msg.get_body(preferencelist=('plain')).get_content()]
        st.info('Archivo recibido correctamente')
        st.write(text_mail[0])  
        vectorized_text=vc.transform(text_mail).toarray()
        result=model.predict(vectorized_text)
        st.write('Este mail se considera un spam' if result == 1 else 'Este mail se considera normal')
    else:
        st.info('Esperando ingresar el texto')
    


    