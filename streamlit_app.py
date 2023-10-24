import streamlit
streamlit.title('My parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Blueberry oatmeal & Omega 3')
streamlit.text(' 🐔 Hard boiled Free Range Eggs')
streamlit.text(' 🥗 Kale, spinach & Rocket Smoothie')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
