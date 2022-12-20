################
# Penguins App #
################

import streamlit as st
import pandas as pd
st.title("Palmers Penguins")

#Data imports
penguins_df = pd.read_csv("https://github.com/charlesvarthur/Streamlit-for-Data-Science/blob/24f999a9c033b0a84480999f6553cf59c783f4e8/penguin_app/penguins.csv")
st.write(penguins_df.head())