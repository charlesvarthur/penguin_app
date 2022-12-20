################
# Penguins App #
################

import streamlit as st
import pandas as pd
st.title("Palmers Penguins")

#Data imports
penguins_df = pd.read_csv("https://github.com/charlesvarthur/Streamlit-for-Data-Science/blob/main/penguin_app/penguins.csv")
st.write(penguins_df.head())