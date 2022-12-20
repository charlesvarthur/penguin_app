################
# Penguins App #
################

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Palmers Penguins")

#Data imports
penguins_df = pd.read_csv('https://raw.githubusercontent.com/charlesvarthur/Streamlit-for-Data-Science/main/penguin_app/penguins.csv')
#st.write(penguins_df.head())

#Opening paragraph   s
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')

#Create user input variables for the species and characteristics
selected_species = st.selectbox('What species would you like to visualise?', ['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox('What do you want the variable x to be?',['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])
selected_y_var = st.selectbox('What would you like the variable y to be?',['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])

#Create the scatter plot from the dataframe and the variables
penguins_df = penguins_df[penguins_df['species'] == selected_species]

fig, ax = plt.subplots()
ax = sns.scatterplot(x = penguins_df[selected_x_var], y = penguins_df[selected_y_var])
plt.title(selected_species)
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
st.pyplot(fig)