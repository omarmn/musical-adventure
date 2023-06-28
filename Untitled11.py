#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import streamlit as st
import openpyxl

# Read the CSV file (change dir below)
data = pd.read_excel('Matrice Afidium copie.xlsx', sheet_name='RAW DATA1')


# In[33]:

skills=data.columns[1:].tolist()
skills.sort()
column_name=st.selectbox('Select a skill', skills)
top3=data[column_name].sort_values(ascending=False)[:3].index
df=data[['Ton prénom/nom',column_name]].loc[top3]
# df.rename(columns={column_name:'Score'}, inplace=True)
df.columns=['prénom/nom', 'Score']

st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
