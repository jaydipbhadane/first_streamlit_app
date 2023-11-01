import streamlit
import pandas
streamlit.title("YashOne Online Fruit Stall")
streamlit.header("Get your fruits at your Door step...")
streamlit.text("what fruits We delivers :")
food = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(food)
selected_fruits = streamlit.multiselect("Pick the Fruits you would like to it : ",list(food['Fruit']))
streamlit.text("Your Cart")
streamlit.dataframe(selected_fruits.loc)
