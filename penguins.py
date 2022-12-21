################
# Penguins App #
################

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Palmers Penguins")

#Data imports
penguin_file = st.file_uploader('Select your local penguins CSV (default provided)')
if penguin_file is not None:
    penguins_df=pd.read.csv(penguin_file)
else:
    #st.stop()
    penguins_df = pd.read_csv('https://raw.githubusercontent.com/charlesvarthur/Streamlit-for-Data-Science/main/penguin_app/penguins.csv')

#st.write(penguins_df.head())

#Opening paragraph   s
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')

#Create user input variables for the species and characteristics
#selected_species = st.selectbox('What species would you like to visualise?', ['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox('What do you want the variable x to be?',['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])
selected_y_var = st.selectbox('What would you like the variable y to be?',['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])

#User input for gender of the penguin
select_gender= st.selectbox('Which Gender would you like to analyse?', ['male','female','all genders'])
if select_gender == 'male':
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif select_gender == 'female':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
    pass

#Create the scatter plot from the dataframe and the variables
#penguins_df = penguins_df[penguins_df['species'] == selected_species]

sns.set_theme(style = 'darkgrid', palette='deep')
sns.axes_style("darkgrid")
markers = {"Adelie" : 'X', "Gentoo": 's', "Chinstrap":'o'}
fig, ax = plt.subplots()
ax = sns.scatterplot(data = penguins_df, x = selected_x_var, y = selected_y_var, hue ='species', markers = markers, style ='species')
plt.title('Characteristics of penguins')#.format(selected_species))
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
st.pyplot(fig)