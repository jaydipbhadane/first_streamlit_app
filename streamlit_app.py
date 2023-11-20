import streamlit
import pandas
streamlit.title("YashOne Fruit Shop")
streamlit.header("Get fruits at your Door step...")
streamlit.text("what fruits We delivers :")
food = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
food = food.set_index('Fruit')
streamlit.dataframe(food)
selected_fruits = streamlit.multiselect("Pick the Fruits you would like to it : ",list(food.index))
cart = food.loc[selected_fruits]
streamlit.text("Your Cart")
streamlit.dataframe(cart)
