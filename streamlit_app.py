import streamlit

streamlit.title('My Parents New Healthy Diner')


streamlit.header('Breakfast menu')

streamlit.text('🍉🍓🥝🍅🍒🍑🍍🐔 🥑Poori Idly Dosa Chapathi Rava Dosa Uthappam Avacado toast')

streamlit.header('🍌🍍 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index),['Mango','Avacado'])

streamlit.dataframe(my_fruit_list)
