#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import streamlit as st
import openpyxl

# Read the CSV file
data = pd.read_excel('Matrice Afidium copie.xlsx', sheet_name='RAW DATA1')


# In[33]:

skills=data.columns[1:].tolist()
skills.sort()
column_name=st.selectbox('Select a skill', skills)
top3=data[column_name].sort_values(ascending=False)[:3].index
st.dataframe(data['Ton prénom/nom'].loc[top3])

